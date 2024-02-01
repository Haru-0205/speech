---
theme: seriph
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shikiji
lineNumbers: false
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
drawings:
  persist: false
transition: slide-left
title: Welcome to Slidev
mdc: true
aspectRatio: '16:10'
canvasWidth: 980
fonts:
  sans: 'Klee One'
  serif: 'Shippori Mincho'
  mono: 'Fira Code , Noto Sans JP'
---

# <span class="text-slate-100">女の子になりたい/まふまふ</span>

## <span class="text-slate-400">～かわいらしい歌詞に込められた考え方～</span>

---
transition: slide-left
---

# 紹介する詩歌のメタデータ

| 項目 |  |
| --- | --- |
| 曲名 | 女の子になりたい (I wanna be a girl) |
| 作詞 | まふまふ |
| 作曲 | まふまふ |
|  | 田中秀和(Monaca) |

<!--
「女の子になりたい」：2019年の誕生日(10/18)にニコニコ動画・YouTubeで発表  
現在の再生回数は4500万回を超える  


作詞者：まふまふ  
他の代表曲として「1.2.3」(2019/12/5, ただしそらるとのユニット「After the Rainとして」), 「すーぱーぬこになりたい」(2016), 「リア充になりたい」(2020)など。  
1.2.3 はアニメ「ポケットモンスター」の主題歌として約3年間歌い継がれた。  
「まぬんちゃん」として「チョコっとの答え」(共同作曲：田中秀和), 「まふゆちゃん」として「魔法少女 あふた～☆ざれいん」というユニットで「恋の魔法はメロルリラ」など  

共同作曲者：田中秀和  
代表曲として、「Silent Star」「Transforming」(ウマ娘),「Star!!」,「M@GIC☆」(読み：マジック)(アイドルマスター), 「カレンダーガール!」「Move on now!」(アイカツ!) をはじめとする多くのゲーム・アニメ主題・挿入歌および「女の子になりたい」「チョコっとの答え」「すーぱーぬこになれんかった」(田中秀和×まぬんちゃん名義)などのアーティストの楽曲の作編曲に携わる。  
ただし、2022年に公然わいせつ罪で逮捕・懲役1年6ヶ月・執行猶予3年の判決  
彼は、未成年の女の子たちが奮闘するようなストーリーの楽曲を多く手掛けていたにもかかわらず、未成年に手を出したため、ネット上でかなり叩かれた。
-->

---
transition: slide-up
---

# 曲全体について

![形態素解析結果](wordcloud-i_wanna_be_a_girl.png)

↑Janomeによる形態素解析の結果をWordCloudで可視化した図

---
transition: slide-left
---

```python{all|1-4|5-12|13-23|24-26|27-31|all}
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
  if re.compile("^助詞").search(token.part_of_speech) or re.compile("^助動詞")(token.part_of_speech) :
      print(token)
  else:
      words.append(token.base_form)
      print(token)
# 各単語の出現回数をカウント&出力
count_words = collections.Counter(words)
print(count_words)
# WordCloudで可視化
fpath = 'C:/Windows/Fonts/YuGothM.ttc'
text = ' '.join(words)
wordcloud = WordCloud(background_color='white', font_path=fpath, width=600, height=450).generate(text)
wordcloud.to_file('./wordcloud.png')
```

---
transition: slide-up
---



# 詩歌の一節

<div class="px-5 border-2 border-indigo-800/75 border-dashed">

大人になれど下がらない 可笑しな声のトーンと  
何しても何しても うまく行かない今日だ  
ならば!  
束の間でも夢の中に ボクを見つけてみようかな  
少しだけ少しだけ 変われる気がする

</div>

<br>

<v-clicks>

> 大人になれど下がらない 可笑しな声のトーンと

↑「ボク」の**コンプレックス**(=「**理想の自分**とのギャップ」)  
「可笑しな」と**自嘲的**に表現  
ここで「ボク」の「理想の自分」  
  ＝「男性らしい」低い声をもつ(↔現在の自分)

> 何しても何しても うまく行かない今日だ

コンプレックスに足を引っ張られ、色々なものがうまくいかない(日常生活に支障が出てる)

</v-clicks>

<!--
「大人になれど下がらない」＝「男性らしい低い声」を望んでいた  
↔「可笑しな声のトーン」＝理想と現実のギャップを感じている  

「何しても何しても うまくいかない」  
- コンプレックスの方に引っ張られすぎてマイナス思考(≒自暴自棄)になってしまっている  
- 日常生活にも支障をきたしている
-->

---
transition: slide-up
---

<div class="px-5 border-2 border-indigo-800/75 border-dashed">

大人になれど下がらない 可笑しな声のトーンと  
何しても何しても うまく行かない今日だ  
ならば!  
束の間でも夢の中に ボクを見つけてみようかな  
少しだけ少しだけ 変われる気がする

</div>

<br>

<v-clicks>

> ならば!

「ボク」は視点・発想を転換する

> 束の間でも夢の中に ボクを見つけてみようかな  

「夢の中」＝「現実とは切り離された」状態  
そこでみつけた「ボク」＝「声の高さ」も「**自分らしさ**」にできる「**女の子**」

> 少しだけ 少しだけ 変われる気がする

「少しだけ 少しだけ」(反復)＝**希望**  
変われる＝現在の自分の**悩み**から脱却する

</v-clicks>

<!--
「ならば」：転換の接続詞  
「束の間」＝そう長くはいれない≠現実?  
「夢の中」＝非現実  
「ボクを見つけてみようかな」：  
先述のとおり「本当の自分」を見失っていたと考えられる  
→「本当の」ボクをみつける  

## 「本当のボク」とは?

- 自分の高い声がコンプレックスではなく「自分らしさ」として表現できる存在
- 世間から隠していた「本当の自分」の好きなことや希望・思い

「少しだけ 少しだけ」：反復  
「少しでも変わるだろう」という強い希望?  

「変われる」：「今の自分」から「変われる」  
→自分のコンプレックスによる悩み・病んだ状態からの脱却
-->

---
transition: slide-left
---

> **ナイショの気持ち ホントの気持ち**  
> **ちょっと話しちゃおう**  
> ワンツースリー 魔法をかけて  
> **新しいボクに なりたいのです お願い!**  
> （「女の子になりたい」より）

<v-click>

> 学ランよりセーラー服のほうが着たいし ドレスだって すっごく楽しみにしてて ハイヒールだってはきたかった…  
> 何度もやめようと思った 男の子なのにかわいいものが好きなのは変だから  
> でも **僕は 好きなものを ちゃんと好きって言いたい**<br>
> <br>
> 満足なんかしてないよ...  
> 蒼井さんが僕にしてくれたように  
> **僕も本当の僕を あきらめたくない!**  
> （「先輩はおとこのこ」第16話「王子様とお姫様」より）

</v-click>


<v-click>

> 父さん僕に聞いたよね  
> **男の子として生きたいのか 女の子として生きたいのか**  
> **やっと**わかったんだ **どっちでもない**って  
> **僕は 僕のままで生きたい**  
> **男の子だけど女の子みたいなものが好きで 母さんが求める子供じゃないけど** 認めてほしいんだ  
> （「先輩はおとこのこ」第76話「帰宅」より）

</v-click>

<!--
女の子になりたいの1番の歌詞より抜粋。  
> ナイショの気持ち ホントの気持ち  
> ちょっと話しちゃおう  
> ワンツースリー 魔法をかけて  
> 新しいボクに なりたいのです お願い!

その具体例として、まんが「先輩はおとこのこ」より抜粋。

> 僕は 好きなものを ちゃんと好きって言いたい  
> 僕も 本当の僕を あきらめたくない!

なお、性別の在り方として「どっちでもない」というのも一つの選択であることを示すために、まんが「先輩はおとこのこ」より抜粋。

> やっとわかったんだ どっちでもないって  
> 僕は 僕のままで生きたい  
> 男の子だけど女の子みたいなものが好きで 母さんが求める子供じゃないけど 認めてほしいんだ
-->

---
layout: end
---

# ご清聴 ありがとうございました

\# 先程のPythonファイルはGitHub(https://github.com/Haru-0205/speech/blob/main/wordcloud.py)上に掲載しますので、使いたい方はご自由にお使いください。
