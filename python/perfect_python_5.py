### 5-1 関数の定義
"""
def 関数名(引数1,引数2,引数3, ...):
    ステートメント1
    ステートメント2

defの文の最後はコロン「:」で終わり、
次の行から1段落インデントして処理内容を既述します
定義した関数は、関数名に小カッコをつけて呼び出します
"""

def test_func(arg1, arg2):
    print("test_func", arg1, arg2)

test_func("aaa", "bbb")

"""
なにの処理もしない、空の関数を書く場合は、passだけを記述する
"""

def spam():
    pass

spam()

### 5-2 引数の指定
"""
関数を呼び出すとき、引数の指定には、引数の位置による指定と、キーワードによる指定がある
位置による指定はC言語などで一般的に使われる指定方法で、引数が定義された順番によって対応する引数の値を割り当てる
キーワードによる指定とは、「引数名＝値」の形式で、位置に関係なく引数を指定する方法です
"""

def spam(arg1, arg2,arg3):
    print(arg1, arg2, arg3)

spam(1,2,arg3=3) # arg1,arg2は位置による指定。arg3はキーワードによる指定

"""
引数を１つずつ記述するのではなく、位置指定引数をシーケンスオブジェクト、
キーワード引数を辞書オブジェクトにまとめて呼び出す方法がある
この場合、位置指定引数のシーケンスは「*」、キーワード引数の辞書は「**」を指定する
"""

def spam(arg1,arg2,arg3,arg4,arg5):
    print(arg1,arg2,arg3,arg4,arg5)

spam(1,2,3,arg4=4,arg5=5)

args = (2,3)
keyward = {'arg5': 5, 'arg4': 4}

spam(1, *args, **keyward)

### 5-3 デフォルト引数
"""
関数の定義にデフォルト値を設定すると、その引数を省略可能にできる

def 関数名(引数1、省略可能引数 2 = デフォルト値、省略可能引数 3 = デフォルト値):
    ステートメント
"""

def spam(arg1,arg2="arg2が省略されました"):
    print(arg1, arg2)

spam(1,2)
spam(1)

### 5-4 可変長引数
"""
引数の数を事前に決めずに、任意の数の引数を指定できる関数

def 関数名(引数1、引数2、*引数シーケンス、**引数辞書):
    ステートメント


引数シーケンスには、呼び出すときに指定された引数のリストが渡され、
引数辞書には、呼び出すときに「引数名＝値」の形式で指定したキーワードの引数の辞書が渡される
"""

def spam(arg1, *args, **keyward):
    print(arg1,args,keyward)

spam(1, 2, 3, 4, 5, arg6=6, arg7=7)

### 5-5 return文
"""
関数の戻り値は、return文で指定する
戻り値を省略した場合、Noneが戻り値となる

return 【戻り値】
"""

### 5-6 global宣言
"""
関数定義の内部で定義した変数をローカル変数、関数定義の外側で定義した変数をグローバル変数という
グローバル変数は関数の中でもそのまま参照できる
"""

var1 = 'グローバル変数'

def spam():
    var2 = 'ローカル変数'
    return (var1, var2)

print(spam())

def spam():
    global var1

    var1 = 'ローカルで変更'
    var2 = 'ローカル変数'
    return (var1, var2)

print(spam())

### 5-7 nonlocal宣言
"""
関数の内部にも、また別の関数を書くことができます
内側で定義した関数では、外側の関数のローカル変数を参照できます
"""

def outer():
    var1 = '外側の変数'
    def inner():
        var2 = '内側の変数'
        return (var1, var2)
    return inner()

print(outer())

"""
内側の関数で、外側にあるローカル変数の変更が必要な場合、
nonlocal文で変数が外側の関数で定義されたローカル変数であると宣言してから、値を設定します

nonlocal 変数名1, 変数名2, ...
"""

def outer():
    var1 = '外側の変数'
    var2 = 'これも外側の変数'

    def inner():
        nonlocal var1 #var1を外側の関数の変数と宣言し、値を変更できるようにする
        var1 = '内側で変更'
        var3 = '内側の変数'
        return var1, var2, var3
    return inner(), var1

print(outer())

#### 5-7-1 クロージャ
"""
この例のように、関数の内部で定義され、かつ外側の関数のローカル変数を参照している関数のことを
クロージャと呼ぶことがある
outer()は戻り値としてinner()を返して処理を終了しますが、
終了してしまったあとでも、クロージャであるinner()はouter()のローカル変数であるvar1やvar2を参照できる
"""

### 5-8 ジェネレータ関数
"""
ジェネレータ関数は、イテレータの一種である、ジェネレータオブジェクトを作成する関数です
ジェネレータ関数はyield式を含み、ジェネレータオブジェクトの__next__()メソッドが
呼び出されるたびにyield式までが実行され、yield式で指定された値を返す
"""

def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(fib())

items = []
for v in fib():
    items.append(v)
    if len(items) > 10:
        break

print(items)

#### 5-8-1 send()メソッド
"""
再開待ちのジェネレータに、値を送出します。
send()メソッドで指定した値は、yield式の値となります。
"""

def gen(step):
    val = 0
    while True:
        val = val + step
        step = yield val

g = gen(3)
print(g.__next__())

print(g.send(10))
print(g.send(5))


#### 5-8-2 throw()メソッド
"""
再開待ちのジェネレータに、例外を送出します。
"""

#def gen():
#    for i in range(10):
#        yield i
#
#g = gen()
#
#for v in g:
#    print(v)
#    if v > 2:
#        g.throw(ValueError("Invalid value"))

#### 5-8-3 close()メソッド
"""
再開待ちのジェネレータに、GeneratorExit例外を送出して、ジェネレータを正常終了します
"""

def gen2():
    for i in range(10):
        yield i

g = gen2()
for v in g:
    print(v)
    if v > 2:
        g.close()

#### 5-8-4 サブジェネレータ
"""
ジェネレータが他のジェネレータを呼び出してその値を呼び出し元に返す場合、
単純に値を返すだけなら以下のようになる
"""

#def generator():
#    for value in sub_generator():
#        yield value

"""
しかし、このgenerator()をsub_generator()のラッパーとして、呼び出し元からみれば
sub_generator()を呼び出しているように見える実装が必要な場合には、かなり複雑な処理になります
呼び出し元からsend()やthrow()などのジェネレータメソッドを呼ぼ出された時、
その呼出しがあったことをサブジェネレータに渡さなければならない
こういったラッパーが必要となるケースはかなり多く、python 3.3からyield fromという専用の文法が用意された
"""

#def generator():
#    yield from sub_generator()

"""
yield fromは、指定されたサブジェネレータが終了するまで値を呼び出し元に渡し続け、
この間、send()などジェネレータメソッドが呼び出された場合にはsub_generator()のジェネレータメソッドが呼び出される
また、yield fromで呼び出されたジェネレータは、return文で値を返すことができ、
その値はyield fromの式の値となります
"""

def sub_generator():
    yield 1
    yield 2
    return "これは戻り値です"

def generator():
    ret = yield from sub_generator()
    yield ret

for v in sub_generator():
    print(v)

for value in generator():
    print(value)

### 5-9 高階関数とlambda式
"""
pythonでは、関数は数値や文字列と同様な、オブジェクトの一種にすぎない
数値と同様に、変数に格納したり、リストに格納したりできる
"""

def spam():
    pass

my_spam = spam # my_spamという名前でもspamを参照できる
my_spam()

funcs = [spam] # リストに関数オブジェクト格納
funcs[0]()     # リスト内の関数を呼び出す

def ham(arg):
    pass

def egg():
    ham(spam)
    return spam

"""
このように、関数を引数としてとったり、戻り値として返す関数を高階関数という
pythonでのコーディングテクニックとして広く使われている
例えば。シーケンスの全要素から、奇数の要素のみを抽出する処理を考えてみましょう
高階関数を使わない場合は、シーケンスの全要素にアクセスして、奇数の要素を抽出する関数を作成することになる
"""
def pick_odd(seq):
    ret = []
    for item in seq:
        if item % 2 == 1:
            ret.append(item)
    return ret

"""
高階関数を使う方法では、以下のようにシーケンスの全要素にアクセスする関数と、
値が奇数であるかを判定する関数の2つに分けて作成できる
"""

def is_odd(item):
    return item % 2 == 1

def filter(pred, seq):
    ret = []
    for item in seq:
        if pred(item):
            ret.append(item)
    return ret

def pick_odd(seq):
    return filter(is_odd, seq)

"""
このように関数を細分化することで、例えば偶数値のみを抽出するように変更された場合でも、
新しくis_even()関数を用意すれば対応できるようになる
また、is_odd()のような評価関数はlambda式という無名関数を利用する事もある
"""

def pick_odd(seq):
    return filter(lambda item: item % 2 == 0, seq)

### 5-10 関数デコレータ
"""
関数デコレータは、関数の情報をわかりやすく明示し、機能を追加・変更するための便利な機能です
例えば、いくつかの関数に、呼び出された時にログメッセージを出力する必要があるとします
簡単な方法としては、事前に用意したメッセージ出力関数を、それぞれの関数内部で呼び出すという方法がある
"""

def show_message():
    print("function called")

def func1():
    show_message()
    ...
    do_func1()

def func2():
    show_message()
    ...
    do_func2()

"""
このコードはデコレータを使うと次のようにかけます
"""

def show_message(f):
    """関数 f を受け取り、ログを出力してから関数 f を呼び出す関数 wrapperを返す"""
    def wrapper():
        print("function called")
        return f()

    return wrapper

@show_message
def spam1():
    do_spam1

@show_message
def spam2():
    do_spam2

"""
この書き方では、関数spam1が定義されると、その関数オブジェクトを引数としてshow_messageが呼び出され
その戻り値がspam1という名前の関数として登録される
この流れを擬似的に書くと
"""

def spam1():
    do_spam1

spam1 = show_message(spam1)

"""
このように、関数の内部には手を入れずに、関数定義で宣言的に機能を指定する場合には
関数デコレータを使用します
また、機能の追加だけでなく、関数の宣言としてデコレータを使う場合もある
例えば、atexitモジュールのregister()関数をデコレータとして使用すると、
その関数はプロセス終了時に呼び出される関数として登録される
"""

import atexit

@atexit.register
def spam():
    #プロセス終了時に呼ばれる
    do_something_to_do_at_exit()

"""
関数デコレータは複数個指定することができる
複数個指定した場合は、一番下のデコレータが最初に適用される
この例では、
spam = show_message(print_result(spam))
とかいた場合と同等になる
"""

@show_message
@print_result
def spam():
    do_spam()

### 5-11 ドキュメンテーション文字列
"""
関数定義の先頭には、関数を説明するドキュメンテーション文字列を書くことができる
"""

def add(left, right):
    """
    2つの引数の和を返します
    キーワード引数：
    left --  加算の左項
    right -- 加算の右項
    """

    return left + right

"""
ドキュメンテーション文字列は、pythonのヘルプ機能で参照できる
"""

>>> help(add)


### 5-12 関数アノテーション
"""
python3では、ドキュメンテーション文字列以外でも、関数の定義部分に引数の説明や
戻り値を注釈として記述できるようになった
注釈は単なる式で、"これは注釈です"のような文字列や、100 + 200のような数値、intのような形名など
通常のpython式を記述します
"""

def add(left: '左項', right: '右項') -> '和':
    return left + right

"""
戻り値の注釈は
関数ヘッダ行の「:」の前に、「-> 注釈式」の形式でしていする
引数の注釈は
「引数名:注釈式[=デフォルト値]」で指定します
"""
