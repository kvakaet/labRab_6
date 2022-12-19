#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    word = 'килбайот'
    correct_word = "килобайт"

    for i, letter in enumerate(word):
        correct_letter = correct_word[i]
        if letter != correct_letter:
            word = word[:i] + word[i:].replace(letter, correct_letter, 1)

    print(word)
