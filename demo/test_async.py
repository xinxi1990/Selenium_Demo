#!/usr/bin/env python
# -*- coding: utf-8 -*-

import asyncio,time,requests

# async def main():
#      print('hello')
#      await asyncio.sleep(1)
#      print('world')
#
#
#
# async def async_double(x):
#     return 2 * x
#
#
# async def print_double(x):
#     print(await async_double(x))   # <-- OK!


# import asyncio
# import time
#
# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(what)
#
# async def main():
#     print(f"started at {time.strftime('%X')}")
#
#     await say_after(1, 'hello')
#     await say_after(2, 'world')
#
#     print(f"finished at {time.strftime('%X')}")
#
# asyncio.run(main())
#
#
# asyncio.run(main())


# async def foo():
#     time.sleep(3)
#     print("这是一个协程")
#     return "返回值"
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         print("开始运行协程")
#         coro = foo()
#         print("进入事件循环")
#         result = loop.run_until_complete(coro)
#         print(f"run_until_complete可以获取协程的{result}，默认输出None")
#     finally:
#         print("关闭事件循环")
#         loop.close()


# async def requests_baidu():
#     time.sleep(3)
#     r = requests.get("http://www.baidu.com")
#     print(r.status_code)
#     return r.status_code
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         print("开始运行协程")
#         coro = requests_baidu()
#         print("进入事件循环")
#         result = loop.run_until_complete(coro)
#         print(f"run_until_complete可以获取协程的{result}，默认输出None")
#     finally:
#         print("关闭事件循环")
#         loop.close()
#

# import asyncio
#
#
# async def main():
#     print("主协程")
#     print("等待result1协程运行")
#     res1 = await result1()
#     print("等待result2协程运行")
#     res2 = await result2(res1)
#     print("等待result2协程运行。。。。")
#     return (res1,res2)
#
#
# async def result1():
#     await asyncio.sleep(3)
#     print("这是result1协程")
#     return "result1"
#
#
# async def result2(arg):
#     await asyncio.sleep(3)
#     print("这是result2协程")
#     return f"result2接收了一个参数,{arg}"
#
#
# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     try:
#         print("开始运行协程")
#         coro = main()
#         print("开始运行协程。。。。。")
#         result = loop.run_until_complete(coro)
#         print(f"获取返回值:{result}")
#     finally:
#         print("关闭事件循环")
#         loop.close()
#





import asyncio


def callback(n):
    print(f"callback {n} invoked")


async def main(loop):
    print("注册callbacks")
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)
    await asyncio.sleep(0.4)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()