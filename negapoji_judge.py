import sys
from negapoji import feeling

sentence = input("Please enter your sentence: ")
negapoji = feeling.feeling()

print(negapoji.judge(sentence))