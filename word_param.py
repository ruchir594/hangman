#!/usr/bin/env python
import random

class HangmanGame(object):
    def __init__(self):
        self.word = []
        self.display = []
        self.missed = set()
        self.status = False

    def get_word(self):
        f = open('words.txt', 'r')
        a = []
        for e in f.readlines():
            a.append(e[:-1])
        temp = random.choice(a)
        self.word = [e for e in temp]
        self.display = ['_' for e in temp]
        return temp
