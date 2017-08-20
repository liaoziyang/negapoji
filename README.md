# negapoji
Japanese negative positive classification.
日本語文書のネガポジを判定する。

### Usage

```
git clone git@github.com:liaoziyang/negapoji.git
python3 negapoji_judge.py
```
### Sample

```
$ python3 negapoji_judge.py
Please enter your sentence: おはようございます。
positive
```
```
$ python3 negapoji_judge.py
Please enter your sentence: 痛いです。
negative
```

### Reference

dataset:

1. 日本語評価極性辞書（用言編）ver.1.0（2008年12月版）/ Japanese Sentiment Dictionary (Volume of Verbs and Adjectives) ver. 1.0
  * 著作者: 東北大学 乾・岡崎研究室 / Author(s): Inui-Okazaki Laboratory, Tohoku University
  
2. 日本語評価極性辞書（名詞編）ver.1.0（2008年12月版）/ Japanese Sentiment Dictionary (Volume of Nouns) ver. 1.0
  * 著作者: 東北大学 乾・岡崎研究室 / Author(s): Inui-Okazaki Laboratory, Tohoku University
  
paper:

1.小林のぞみ，乾健太郎，松本裕治，立石健二，福島俊一. 意見抽出のための評価表現の収集. 自然言語処理，Vol.12, No.3, pp.203-222, 2005. / Nozomi Kobayashi, Kentaro Inui, Yuji Matsumoto, Kenji Tateishi. Collecting Evaluative Expressions for Opinion Extraction, Journal of Natural Language Processing 12(3), 203-222, 2005.

2.東山昌彦, 乾健太郎, 松本裕治, 述語の選択選好性に着目した名詞評価極性の獲得, 言語処理学会第14回年次大会論文集, pp.584-587, 2008. / Masahiko Higashiyama, Kentaro Inui, Yuji Matsumoto. Learning Sentiment of Nouns from Selectional Preferences of Verbs and Adjectives, Proceedings of the 14th Annual Meeting of the Association for Natural Language Processing, pp.584-587, 2008.
