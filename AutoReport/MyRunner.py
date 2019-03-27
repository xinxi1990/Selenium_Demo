# -*- coding: utf-8 -*-
import os
import time
import sys
import unittest
import datetime
from libs.logger import init_logger

sys.path.append("..")
from functools import wraps
from driver.wdriver import WDriver

PY3K = (sys.version_info[0] > 2)
if PY3K:
    import io as StringIO
else:
    import StringIO
import copy


__author__ = "xinxi"
__version__ = "1.0.0"

TestResult = unittest.TestResult
class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """

    def __init__(self, fp):
        self.fp = fp

    def write(self, s):
        self.fp.write(s)

    def writelines(self, lines):
        self.fp.writelines(lines)

    def flush(self):
        self.fp.flush()


stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)




class _TestResult(TestResult):
    # note: _TestResult is a pure representation of results.
    # It lacks the output and reporting ability compares to unittest._TextTestResult.

    def __init__(self, verbosity=1, retry=0, save_last_try=True):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.success_count = 0
        self.failure_count = 0
        self.error_count = 0
        self.verbosity = verbosity

        # result is a list of result in 4 tuple
        # (
        #   result code (0: success; 1: fail; 2: error),
        #   TestCase object,
        #   Test output (byte string),
        #   stack trace,
        # )
        self.result = []
        self.retry = retry
        self.trys = 0
        self.status = 0
        self.save_last_try = save_last_try
        self.outputBuffer = StringIO.StringIO()
        self.total_image = []
        self.total_reuslt = {}
        self.test_result_list = []



    def gen_totoal_reuslt(self):
        '''
        组装总的测试结果
        :return:
        '''
        self.total_reuslt["testName"] = "autotest"
        self.total_reuslt["testAll"]  = self.success_count +  self.failure_count + self.error_count
        self.total_reuslt["testPass"] = self.success_count
        self.total_reuslt["testFail"] = self.failure_count
        self.total_reuslt["testSkip"] = self.error_count
        self.total_reuslt["beginTime"] = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime())
        self.total_reuslt["totalTime"] = "100ms"
        self.total_reuslt["testResult"] = self.test_result_list
        return self.total_reuslt




    def startTest(self, test):
        test.imgs = []
        # test.imgs = getattr(test, "imgs", [])
        TestResult.startTest(self, test)
        self.outputBuffer.seek(0)
        self.outputBuffer.truncate()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector

    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()

    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        if self.retry:
            if self.status == 1:
                self.trys += 1
                if self.trys <= self.retry:
                    if self.save_last_try:
                        t = self.result.pop(-1)
                        if t[0] == 1:
                            self.failure_count -= 1
                        else:
                            self.error_count -= 1
                    test = copy.copy(test)
                    sys.stderr.write("Retesting... ")
                    sys.stderr.write(str(test))
                    sys.stderr.write('..%d \n' % self.trys)
                    doc = test._testMethodDoc or ''
                    if doc.find('_retry') != -1:
                        doc = doc[:doc.find('_retry')]
                    desc = "%s_retry:%d" % (doc, self.trys)
                    if not PY3K:
                        if isinstance(desc, str):
                            desc = desc.decode("utf-8")
                    test._testMethodDoc = desc
                    test(self)
                else:
                    self.status = 0
                    self.trys = 0
        self.complete_output()


    def gen_case_info(self,className,status,log):
        '''
        组装测试结果
        :return:
        '''
        self.test_result = {}
        self.test_result["className"] = className
        self.test_result["methodName"] = className
        self.test_result["description"] = className + "," + status
        self.test_result["spendTime"] = "100ms"
        self.test_result["status"] = status
        self.test_result["log"] = log
        return self.test_result



    def addSuccess(self, test):
        self.success_count += 1
        self.status = 0
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        self.test_result_list.append(self.gen_case_info(str(test),"Success","Success"))
        if self.verbosity > 1:
            sys.stderr.write('ok ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('.')

    def addError(self, test, err):
        self.error_count += 1
        self.status = 1
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        # if not getattr(test, "driver",""):
        #     pass
        # else:
        #     try:
        #         driver = getattr(test, "driver")
        #         test.imgs.append(driver.get_screenshot_as_base64())
        #     except Exception:
        #         pass
        try:
            driver = WDriver().get_driver()
            my_log = init_logger()
            my_log.info("****addError****")
            fail_image = "<img src=\"data:image/png;base64,{}\"/>".format(driver.get_screenshot_as_base64())
            log = [str(err), fail_image]
            self.test_result_list.append(self.gen_case_info(str(test), "addError", log))
        except Exception:
            pass

        if self.verbosity > 1:
            sys.stderr.write('E  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('E')

    def addFailure(self, test, err):
        self.failure_count += 1
        self.status = 1
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        # if not getattr(test, "driver",""):
        #     pass
        # else:
        #     try:
        #         driver = getattr(test, "driver")
        #         test.imgs.append(driver.get_screenshot_as_base64())
        #     except Exception as e:
        #         pass
        try:
            driver = WDriver().get_driver()
            my_log = init_logger()
            my_log.info("****addFailure****")
            fail_image = "<img src=\"data:image/png;base64,{}\"/>".format(driver.get_screenshot_as_base64())
            log = [str(err), fail_image]
            self.test_result_list.append(self.gen_case_info(str(test), "addFailure", log))
        except Exception as e:
            print(e)
        if self.verbosity > 1:
            sys.stderr.write('F  ')
            sys.stderr.write(str(test))
            sys.stderr.write('\n')
        else:
            sys.stderr.write('F')





class HTMLTestRunner():
    def __init__(self, stream=sys.stdout, verbosity=1, title=None, description=None, retry=0, save_last_try=False):
        self.stream = stream
        self.retry = retry
        self.save_last_try = save_last_try
        self.verbosity = verbosity
        if title is None:
            self.title = "自动测试报告"
        else:
            self.title = title
        if description is None:
            self.description = "自动测试报告"
        else:
            self.description = description

        self.startTime = datetime.datetime.now()

    def run(self, test):
        "Run the given test case or test suite."
        result = _TestResult(self.verbosity, self.retry, self.save_last_try)
        test(result)
        self.stopTime = datetime.datetime.now()
        # self.generateReport(test, result)
        if PY3K:
            # for python3
            # print('\nTime Elapsed: %s' % (self.stopTime - self.startTime),file=sys.stderr)
            output = '\nTime Elapsed: %s' % (self.stopTime - self.startTime)
            sys.stderr.write(output)
        else:
            print >> sys.stderr, '\nTime Elapsed: %s' % (self.stopTime - self.startTime)
        return result

    # def sortResult(self, result_list):
    #     # unittest does not seems to run in any particular order.
    #     # Here at least we want to group them together by class.
    #     rmap = {}
    #     classes = []
    #     for n, t, o, e in result_list:
    #         cls = t.__class__
    #         if not cls in rmap:
    #             rmap[cls] = []
    #             classes.append(cls)
    #         rmap[cls].append((n, t, o, e))
    #     r = [(cls, rmap[cls]) for cls in classes]
    #     return r

    # def getReportAttributes(self, result):
    #     """
    #     Return report attributes as a list of (name, value).
    #     Override this to add custom attributes.
    #     """
    #     startTime = str(self.startTime)[:19]
    #     duration = str(self.stopTime - self.startTime)
    #     status = []
    #     if result.success_count:
    #         status.append(u'<span class="tj passCase">Pass</span>%s' % result.success_count)
    #     if result.failure_count:
    #         status.append(u'<span class="tj failCase">Failure</span>%s' % result.failure_count)
    #     if result.error_count:
    #         status.append(u'<span class="tj errorCase">Error</span>%s' % result.error_count)
    #     if status:
    #         status = ' '.join(status)
    #     else:
    #         status = 'none'
    #     return [
    #         (u'开始时间', startTime),
    #         (u'耗时', duration),
    #         (u'状态', status),
    #     ]

    # def generateReport(self, test, result):
    #     report_attrs = self.getReportAttributes(result)
    #     generator = 'HTMLTestRunner %s' % __version__
    #     stylesheet = self._generate_stylesheet()
    #     heading = self._generate_heading(report_attrs)
    #     report = self._generate_report(result)
    #     ending = self._generate_ending()
    #     output = self.HTML_TMPL % dict(
    #         title=saxutils.escape(self.title),
    #         generator=generator,
    #         stylesheet=stylesheet,
    #         heading=heading,
    #         report=report,
    #         ending=ending,
    #     )
    #     if PY3K:
    #         self.stream.write(output.encode())
    #     else:
    #         self.stream.write(output.encode('utf8'))
    #
    # def _generate_stylesheet(self):
    #     return self.STYLESHEET_TMPL
    #
    # def _generate_heading(self, report_attrs):
    #     a_lines = []
    #     for name, value in report_attrs:
    #         line = self.HEADING_ATTRIBUTE_TMPL % dict(
    #             name=name,
    #             value=value,
    #         )
    #         a_lines.append(line)
    #     heading = self.HEADING_TMPL % dict(
    #         title=saxutils.escape(self.title),
    #         parameters=''.join(a_lines),
    #         description=saxutils.escape(self.description),
    #     )
    #     return heading
    #
    # def _generate_report(self, result):
    #     rows = []
    #     sortedResult = self.sortResult(result.result)
    #     for cid, (cls, cls_results) in enumerate(sortedResult):
    #         # subtotal for a class
    #         np = nf = ne = 0
    #         for n, t, o, e in cls_results:
    #             if n == 0:
    #                 np += 1
    #             elif n == 1:
    #                 nf += 1
    #             else:
    #                 ne += 1
    #
    #         # format class description
    #         if cls.__module__ == "__main__":
    #             name = cls.__name__
    #         else:
    #             name = "%s.%s" % (cls.__module__, cls.__name__)
    #         doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
    #         desc = doc and '%s: %s' % (name, doc) or name
    #         if not PY3K:
    #             if isinstance(desc, str):
    #                 desc = desc.decode("utf-8")
    #
    #         row = self.REPORT_CLASS_TMPL % dict(
    #             style=ne > 0 and 'errorClass' or nf > 0 and 'failClass' or 'passClass',
    #             desc=desc,
    #             count=np + nf + ne,
    #             Pass=np,
    #             fail=nf,
    #             error=ne,
    #             cid='c%s' % (cid + 1),
    #         )
    #         rows.append(row)
    #
    #         for tid, (n, t, o, e) in enumerate(cls_results):
    #             self._generate_report_test(rows, cid, tid, n, t, o, e)
    #
    #     report = self.REPORT_TMPL % dict(
    #         test_list=u''.join(rows),
    #         count=str(result.success_count + result.failure_count + result.error_count),
    #         Pass=str(result.success_count),
    #         fail=str(result.failure_count),
    #         error=str(result.error_count),
    #     )
    #     return report
    #
    # def _generate_report_test(self, rows, cid, tid, n, t, o, e):
    #     # e.g. 'pt1.1', 'ft1.1', etc
    #     has_output = bool(o or e)
    #     tid = (n == 0 and 'p' or 'f') + 't%s.%s' % (cid + 1, tid + 1)
    #     name = t.id().split('.')[-1]
    #     if self.verbosity > 1:
    #         doc = t._testMethodDoc or ''
    #     else:
    #         doc = ""
    #
    #     desc = doc and ('%s: %s' % (name, doc)) or name
    #     if not PY3K:
    #         if isinstance(desc, str):
    #             desc = desc.decode("utf-8")
    #     tmpl = has_output and self.REPORT_TEST_WITH_OUTPUT_TMPL or self.REPORT_TEST_NO_OUTPUT_TMPL
    #
    #     # o and e should be byte string because they are collected from stdout and stderr?
    #     if isinstance(o, str):
    #         # uo = unicode(o.encode('string_escape'))
    #         if PY3K:
    #             uo = o
    #         else:
    #             uo = o.decode('utf-8', 'ignore')
    #     else:
    #         uo = o
    #     if isinstance(e, str):
    #         # ue = unicode(e.encode('string_escape'))
    #         if PY3K:
    #             ue = e
    #         elif e.find("Error") != -1 or e.find("Exception") != -1:
    #             es = e.decode('utf-8', 'ignore').split('\n')
    #             es[-2] = es[-2].decode('unicode_escape')
    #             ue = u"\n".join(es)
    #         else:
    #             ue = e.decode('utf-8', 'ignore')
    #     else:
    #         ue = e
    #
    #     script = self.REPORT_TEST_OUTPUT_TMPL % dict(
    #         id=tid,
    #         output=saxutils.escape(uo + ue),
    #     )
    #     if getattr(t, 'imgs', []):
    #         # 判断截图列表，如果有则追加
    #         tmp = u""
    #         for i, img in enumerate(t.imgs):
    #             if i == 0:
    #                 tmp += """ <img src="data:image/jpg;base64,%s" style="display: block;" class="img"/>\n""" % img
    #             else:
    #                 tmp += """ <img src="data:image/jpg;base64,%s" style="display: none;" class="img"/>\n""" % img
    #         imgs = self.IMG_TMPL % dict(imgs=tmp)
    #     else:
    #         imgs = u"""无截图"""
    #
    #     row = tmpl % dict(
    #         tid=tid,
    #         Class=(n == 0 and 'hiddenRow' or 'none'),
    #         style=n == 2 and 'errorCase' or (n == 1 and 'failCase' or 'passCase'),
    #         desc=desc,
    #         script=script,
    #         status=self.STATUS[n],
    #         img=imgs,
    #     )
    #     rows.append(row)
    #     if not has_output:
    #         return
    #
    # def _generate_ending(self):
    #     return self.ENDING_TMPL


##############################################################################
# Facilities for running tests from the command line
##############################################################################

# Note: Reuse unittest.TestProgram to launch test. In the future we may
# build our own launcher to support more specific command line
# parameters like test title, CSS, etc.
class TestProgram(unittest.TestProgram):
    """
    A variation of the unittest.TestProgram. Please refer to the base
    class for command line parameters.
    """

    def runTests(self):
        # Pick HTMLTestRunner as the default test runner.
        # base class's testRunner parameter is not useful because it means
        # we have to instantiate HTMLTestRunner before we know self.verbosity.
        if self.testRunner is None:
            self.testRunner = HTMLTestRunner(verbosity=self.verbosity)
        unittest.TestProgram.runTests(self)


main = TestProgram

##############################################################################
# Executing this module from the command line
##############################################################################

if __name__ == "__main__":
    main(module=None)