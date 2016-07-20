#!/usr/bin/env python

import os


def prompt():
    print " % ",


def main():
    while True:
        prompt()
        cmd = raw_input().split(' ')
        if cmd[0] == 'exit':
            break
        else:
            print "Running program " + cmd[0] + "with args " + str(cmd[1:])

if __name__ == "__main__":
    main()
