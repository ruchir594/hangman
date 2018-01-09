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
        print 'word to be guessed ', temp
        self.word = [e for e in temp]
        self.display = ['_' for e in temp]
        self.missed = set()
        self.buffwrite()
        return temp

    def hand(self, key):
        flag = False
        for i in range(len(self.word)):
            if self.word[i] == key:
                self.display[i] = key
                flag = True
        if not flag:
            self.missed.add(key)
            if len(self.missed) > 9:
                self.losewrite()
                return
        if self.word == self.display:
            self.winwrite()
            return
        self.buffwrite()


    def buffwrite(self):
        f = open('buffer.html', 'w')
        f.write("<html><body><h2>")
        f.write(' '.join(self.display) + '\n')
        f.write("</h2>")
        f.write("<form method=\"POST\" action=\"/guessAlpha\">")
        f.write("<select name=\"gword\">\
          <option value=\"a\">a</option>\
          <option value=\"b\">b</option>\
          <option value=\"c\">c</option>\
          <option value=\"d\">d</option>\
          <option value=\"e\">e</option>\
          <option value=\"f\">f</option>\
          <option value=\"g\">g</option>\
          <option value=\"h\">h</option>\
          <option value=\"i\">i</option>\
          <option value=\"j\">j</option>\
          <option value=\"k\">k</option>\
          <option value=\"l\">l</option>\
          <option value=\"m\">m</option>\
          <option value=\"n\">n</option>\
          <option value=\"o\">o</option>\
          <option value=\"p\">p</option>\
          <option value=\"q\">q</option>\
          <option value=\"r\">r</option>\
          <option value=\"s\">s</option>\
          <option value=\"t\">t</option>\
          <option value=\"u\">u</option>\
          <option value=\"v\">v</option>\
          <option value=\"w\">w</option>\
          <option value=\"x\">x</option>\
          <option value=\"y\">y</option>\
          <option value=\"z\">z</option>\
        </select>")
        f.write("<input type=\"submit\" value=\"Submit\"></form>")
        f.write('alphabets you have guessed so far - ' + ', '.join(list(self.missed)) + '\n')
        f.write("<a href=\"/newGame\"<button onclick=\"\"> New Game </button></a></body></html>")

    def losewrite(self):
        f = open('buffer.html', 'w')
        f.write("<html><body><h2>")
        f.write(' '.join(self.display) + '\n')
        f.write("</h2>")
        f.write('alphabets you have guessed so far - ' + ', '.join(list(self.missed)) + '\n')
        f.write("<h1>You lost !!!! Play a new game. The word was " + ''.join(self.word) + "</h1>" )
        f.write("<a href=\"/newGame\"<button onclick=\"\"> New Game </button></a></body></html>")

    def winwrite(self):
        f = open('buffer.html', 'w')
        f.write("<html><body><h2>")
        f.write(' '.join(self.display) + '\n')
        f.write("</h2>")
        f.write('alphabets you have guessed so far - ' + ', '.join(list(self.missed)) + '\n')
        f.write("<h1>Correct !!!! You win. Play again?</h1>")
        f.write("<a href=\"/newGame\"<button onclick=\"\"> New Game </button></a></body></html>")
