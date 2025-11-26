#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from WH_FRONTING.main import askLoki


def main():
    """"""
    return None


if __name__ == "__main__":
    inputSTR = "陳淑樺摔破了花瓶"
    refDICT = {"FT":[]}
    resultDICT = askLoki(inputSTR, refDICT=refDICT)
    print(resultDICT)