import sys
import MeCab as mc
import numpy as np
import os
import codecs

class dictionary:
  pn_wago_verbs_and_adjectives = {}
  pn_wago_nouns = {}

  def __init__(self):
    self.pn_wago_verbs_and_adjectives = self.create_pn_wago_verbs_and_adjectives()
    self.pn_wago_nouns = self.create_pn_wago_nouns()

  def create_pn_wago_verbs_and_adjectives(self):
    point = np.empty(0)
    word = np.empty(0)
    f = codecs.open("dataset/wago.121808.pn", 'r', 'utf-8')
    lines = f.readlines()
    for line in lines:
      content = line.split(',')
      point = np.append(point, content[0])
      word = np.append(word, content[2].rstrip())
    return {'word': word, 'point': point}

  def create_pn_wago_nouns(self):
    point = np.empty(0)
    word = np.empty(0)
    f = codecs.open('dataset/pn.csv.m3.120408.trim', 'r', 'utf-8')
    lines = f.readlines()
    for line in lines:
      content = line.split(',')
      word = np.append(word, content[0])
      point = np.append(point, content[1])
    return {'word': word, 'point': point}
