#!/opt/homebrew/bin/python3

# import lesson_package
# import lesson_package.utils
from operator import imod
from re import S
from lesson_package import utils # 推奨
# from lesson_package.utils import say_twice # こちらの使い方は非推奨、どこから読み込まれているか不明になる。

# from lesson_package.talk import human
# from lesson_package.talk import animal
from lesson_package.talk import * # アスタリスクを使うときは、__init__.py にallを書く。ただし、どのパッケージを読んでいるかわからなくなるので非推奨
from termcolor import colored

import config

#########################################################################

# r = lesson_package.utils.say_twice("hello")
r = utils.say_twice("hello")
q = human.say_twice("hello")

print(r)
print(q)
print(animal.cry())
print(animal.sing())

# 73.組み込み関数 - dictの並び替え
ranking = {"A" : 40, "B":400, "C" :140}
print(sorted(ranking, key=ranking.get, reverse=True))

# 74,標準ライブらい
## defaultdict - 例：でたらめな数値をカウント
s = "asdfasdfadsdk4oojdikoajmfdofadfjieim" 
d = {}
for c in s:
    if c not in d:
        d[c] = 0 #初回にdictがないとエラーで落ちるのでデフォルトでセットしている だるい
    d[c] += 1
print(d)

from collections import defaultdict

dd = defaultdict(int)
for c in s:
    dd[c] += 1
print(dd)


## 75 termcolored
# print(help(colored))  #メソッドのhelp表示
print (colored("aaasdfdasafds", "red"))
print(__name__)