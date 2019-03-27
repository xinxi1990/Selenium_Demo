#!/usr/bin/env python3.5
import getopt
import sys

# https://www.jianshu.com/p/a877e5b46b2d

opts,args = getopt.getopt(sys.argv[1:],'-h-f:-v-o:',['help','filename=','version'])
for opt_name,opt_value in opts:
    if opt_name in ('-h','--help'):
        print("[*] Help info")
        exit()
    if opt_name in ('-v','--version'):
        print("[*] Version is 0.01 ")
        exit()
    if opt_name in ('-f','--filename'):
        fileName = opt_value
        print("[*] Filename is ",fileName)
        # do something
        exit()
if opt_name in ('-o', '--over'):
    fileName = opt_value
    print("[*] Over is ", fileName)
    # do something
    exit()