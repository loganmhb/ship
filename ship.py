#!/usr/bin/env python

import os
import parser


def prompt():
    print " % ",


def main():
    while True:
        prompt()
        cmd = parser.parse_args(raw_input())
        if cmd[0] == 'exit':
            break
        elif cmd[0] == 'cd':
            os.chdir(cmd[1])
        else:
            os.spawnvp(os.P_WAIT, cmd[0], cmd)

if __name__ == "__main__":
    main()
