#-- encoding:utf-8 --#

name = input("お名前は？ ")
"""
直接文字列を入力すると以下のエラー
""で入力文字をくくるとエラーでない

Traceback (most recent call last):
  File "input.py", line 3, in <module>
    name = input("お名前は？ ")
  File "<string>", line 1, in <module>
"""
age  = input("何歳ですか？ ")
print("こんにちは！ %sさん (%s歳)" % (name, age))

