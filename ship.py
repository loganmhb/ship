#!/usr/bin/env python

import os
import shlex



def prompt():
    print " % ",


def main():
    while True:
        prompt()
        cmd = shlex.split(raw_input())
        if cmd[0] == 'exit':
            break
        elif cmd[0] == 'cd':
            try:
                os.chdir(cmd[1])
            except OSError as e:
                print e
        else:
            os.spawnvp(os.P_WAIT, cmd[0], cmd)

if __name__ == "__main__":
    main()
