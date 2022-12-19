#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    string = input("введите предложение\n")
    words = string.split(" ")

    for i in words:
        if string.count(i) == 1:
            print(i)
