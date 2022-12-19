#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    word = input("")
    N = int(input("")) - 1
    M = int(input("")) - 1

    word = word[:N] + word[M] + word[N + 1:M] + word[N] + word[M + 1:]

    print(word)
