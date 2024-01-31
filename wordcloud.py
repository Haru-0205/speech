# imports
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
import collections
# lyrics.txtを読み込み
f = open('lyrics.txt', 'r', encoding='utf-8')
data = f.read()
f.close()
# lyrics.txtから空白と改行を除去
lyrics = data.replace("\n", "")
lyrics = lyrics.replace(" ", "")
lyrics = lyrics.replace("　", "")
# Tokenizerを初期化
t = Tokenizer()
# 形態素解析して、結果を出力しつつ、自立語を抽出
import re
words=[]
for token in t.tokenize(lyrics):
    if re.compile("^助詞").search(token.part_of_speech) or re.compile("^助動詞").search(token.part_of_speech) or re.compile("^記号").search(token.part_of_speech) :
        print(token)
    else:
        words.append(token.base_form)
        print(token)
# 各単語の出現回数をカウント
count_words = collections.Counter(words)
# WordCloudで可視化
fpath = 'C:/Windows/Fonts/YuGothM.ttc'
text = ' '.join(words)
wordcloud = WordCloud(background_color='white', font_path=fpath, width=600, height=450).generate(text)
wordcloud.to_file('./wordcloud.png')
# 出現回数を出力
print(count_words)