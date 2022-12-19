#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    string1 = input("введите предложение без пробелов в начале и конце строки\n")
    string2 = input("введите предложение с пробелами в начале и конце строки\n")

    print(len(string1.split(" ")))
    print(len(string2.strip().split(" ")))
