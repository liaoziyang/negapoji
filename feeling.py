import sys
import MeCab as mc
import numpy as np
import os
import re
import codecs
import dictionary


class feeling:
  
  def __init__(self):
    
    self.pn_wago_verbs_and_adjectives = self.set_pn_wago_verbs_and_adjectives()
    self.pn_wago_nouns = self.set_pn_wago_nouns()
    self.hinshi_collected = ['名詞', '形容詞', '副詞', '動詞']

  def pointing(self, sentence):
    sentence_chomped = self.remove_kaigyo(sentence)
    point = self.simple_voting(self.inui_okazaki(sentence_chomped))

  def inui_okazaki(self, sentence):
    word_point_list = np.empty(0)
    tagger = mc.Tagger('mecabrc')
    sentences_parsed = tagger.parse(sentence).split('\n')
    for sentence_parsed in sentences_parsed:
      if not (sentence_parsed == 'EOS' or sentence_parsed == ''):
        feature = sentence_parsed.split('\t')[1].split(',')
        if feature[0] in self.hinshi_collected:
          pn = self.pn_wago_nouns if feature[0] == "名詞" else self.pn_wago_verbs_and_adjectives
          index = np.where(pn['word']==feature[6])
          if index != None:
            word_point_list = np.append(word_point_list, {"word": feature[6], "point": pn['point'][index]})
    return word_point_list

  def set_pn_wago_verbs_and_adjectives(self):
    d = dictionary.dictionary()
    return d.pn_wago_verbs_and_adjectives

  def set_pn_wago_nouns(self):
    d = dictionary.dictionary()
    return d.pn_wago_nouns

  def simple_voting(self, word_point_list):
    the_day_point = 0
    for word_point in word_point_list:
      the_day_point += float(word_point[point])
    return the_day_point if the_day_point == 0 else the_day_point/int(word_point_list.count)

  def remove_kaigyo(self, sentence):
    return re.sub('/(\r\n|\r|\n|\f)/', "",sentence)