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
