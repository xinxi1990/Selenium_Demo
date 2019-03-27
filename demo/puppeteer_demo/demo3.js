var log4js = require('log4js');
var logger = log4js.getLogger();
logger.level = 'debug';
logger.debug("******************开始测试******************");

// const puppeteer = require('puppeteer');
// (async () => {
//   const browser = await puppeteer.launch({headless:false, slowMo:250});
//   const page = await browser.newPage();
//   await page.goto('http://rennaiqian.com');
//   await page.screenshot({path: 'example.png'});
//   await page.pdf({path: 'example.pdf', format: 'A4'});
//   await browser.close();
// })();
//
// logger.debug("******************结束测试******************");