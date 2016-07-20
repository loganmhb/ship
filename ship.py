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
        else:
            os.spawnvp(os.P_WAIT, cmd[0], cmd)

if __name__ == "__main__":
    main()
