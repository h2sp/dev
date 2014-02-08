### 4-1 条件文
"""
ifステートメントは渡された値の真偽を評価し、フロー制御を行います
pythonで偽として扱われる値は次のものです

None
False
ゼロとして認識できる数値型(0や0.0や0j)
空のシーケンス([]や())
空のマップ型({})
空のセット(set())
__nonezero__メソッドが定義されているクラスでFalseを返すもの
__len__メソッドが定義されているクラスで0を返すもの

上記以外の値は真として扱われる
"""

if True:
    print("True")

if 1:
    print("True")

if []:
    print("True")
else:
    print("False")

"""
ifのブロックではelifとelseキーワードでフローの制御を変えられる
elifは他の言語では、else ifと表現される事もある制御キーワードで、
前の条件文が偽と評価された後に別の条件を評価できる
elseは前の条件文が偽だった場合に通る制御キーワード
"""

#### 4-1-1 and or not
"""
条件式に複数の条件を指定したい場合にand, orを用います
"""

if True and False:
    print("false")

if True or False:
    print("true")

def get_true():
    print("call get_true")
    return True

def get_false():
    print("call get_false")
    return False

"""
andで繋がれた条件は、左から順に評価し、すべてが真だった場合にその条件式のブロックが実行される
"""
if get_true() and get_true():
    print("True")

"""
orで繋がれた条件は、左から順に評価し最初に真のものが見つかった時点でその条件式のブロックが実行される
それ以降のorでつながれた式は評価しない
"""
if get_true() or get_false():
    print("True")

if get_false() or get_true():
    print("True")

"""
条件式を否定したい場合にはnotを使う
"""

if not 0:
    print("true")

if not 1:
    print("false")

"""
andやorは少しおもしろい動きをしている
andは、左辺が真だった場合には右辺を返し、左辺が偽だった場合には左辺を返す
orは左辺が真だった場合には左辺を返し、左辺が偽だった場合には右辺を返す
"""
print(1 and 2)
print(0 and 1)
print(1 or 2)
print(0 or 1 )

### 4-2 比較演算子
"""
比較演算子<,>で値の大小を比較できる
ifやwhileループの条件としてよく使われる

数値     ： 数学的に比較して大小を判断
bytes    ： 辞書順に比較して大小を判断
文字列   ： 各文字をordして、順に比較して大小を判断
リスト   ： 各要素を順に比較し、要素について大小を判断。要素数が違い、存在する要素に関しては同じだった場合には要素数の少ないほうが小さいものとして判断される
map型    ： 比較演算はTypeErrorを出す
set      ： 大小ではなく、スーパーセットやサブセットの判断に利用する
"""

print(1 > 0)
print(1 > 1)
print(1.0 > 1)
print('t' > 'c')

"""
比較演算子は次のように同時にかける
"""
print(0 < 1 < 2 < 3)

"""
通常、他の言語では次のように書くことが多い
"""
print(0 < 1 and 1 < 2 and 2 < 3)

#### 4-2-1 等価
"""
等価をテストするオペレータは「==」です
オブジェクトが同じ値であると言える場合に等価という

数値     ： 数値として同じ値であれば等価
文字列   ： 同じ文字列であれば等価
リスト   ： 含んでいるオブジェクトが順序も含めて等価であれば等価
map型    ： 含んでいるキーと値のセットがすべて同じであれば等価
"""

print("hoge" == "hoge")
print("hoge" == "roge")
print(1==1)
print([1,2,3] == [1,2,3])

"""
オブジェクトの値が同じであれば等価とはいえ、型をまたがった比較は等価とはなりません
オブジェクトの型が違うものを自動で合わせて比較することはありません
"""
print(1 == "1")

"""
数値同士であれば、整数と浮動小数点のように方が違っても思ったとおりの比較ができる
"""
print(1.0 == 1)
print(1.1 == 1)

x = [1,2,3]
y = [1,2,3]
print(id(x))
print(id(y))
print(x == y)

#### 4-2-2 オブジェクトID
"""
各オブジェクトは、メモリ上に自身の場所を持っています
インタプリタがオブジェクトを管理できるようにidがあります
2つのオブジェクトが同一かどうかは、isキーワードで確認できます
isキーワードは2つのオブジェクトが完全に同一かどうかを判断します
"""

print(x is y)
xx = "hoge"
yy = "hoge"

"""
stringやintegerのようなイミュータブル型に関しては、シングルトンでオブジェクトが生成されてメモリ上に保持される
Noneもシングルトンで生成され、どこでも同じIDです
"""

print(xx is yy)
print(1 is 1)
print(None is None)

### 4-3 ループ
#### 4-3-1 for
"""
for文はシーケンスオブジェクトの各要素に同じ処理を実行できる
for ループ内変数名 in コンテナ
"""

for i in ["apple", "orange", "lemon"]:
    print(i)

"""
forループで任意の回数処理を繰り返したい場合には、range()ビルトイン関数で繰り返したい回数を指定するといい
"""

for i in range(5):
    print(i)

"""
リストの要素を順に処理しつつ、インデックス番号も知りたい場合にはenumerate()ビルトイン関数を使う
"""

for index, name in enumerate(["apple", "orange", "lemon"]):
    print(index, name)

"""
ループが終わった後に実行したいプログラムがある場合には、elseを使います
elseブロックは、forループをしなかった場合にも実行されます
ただし、ループを途中で中断するbreakを使った場合には、elseブロックは実行されない
"""
for i in range(3):
    print(i)
else:
    print("done")

for i in range(0):
    print(i)
else:
    print("done")

for i in range(1,4):
    print(i)
    if i == 2:
        break
else:
    print("loop finished")

"""
ループ内のブロックを途中で終了し、次のループへ処理を飛ばす場合にはcontinueを使います
"""

for i in range(1,4):
    print(i)
    if i == 2:
        continue
    print(i)
else:
    print("loop finished")

#### 4-3-2 while
"""
条件が真の間ループし続け、条件が変わった時に終了したい場合に使用する
whileはifと同様に評価される式をとります
whileは続くブロックを実行する前に毎回条件を評価し、条件が真の場合にのみループを続けます
"""

#done = False
#while not done:
#    echo_text = input("echo > ")
#    if echo_text == "bye":
#        done = True
#        print("さようなら")
#    elif echo_text == "done":
#        done = True
#    else:
#        print(echo_text)

"""
whileループにもelseを書けばループの最後に続くブロックが実行されます
このelseはループの終了ポイントが複数あり、最後にかならず実行したいコードがある場合に有用です
for文のelseと同様、whileのelseも、whileループが回らなかった時にも実行されるので注意が必要
for文と同様に、breakでループを抜けた場合にはelseは実行されない
"""
#done = False
#
#while not done:
#    echo_text = input("echo > ")
#    if echo_text == "bye":
#        done = True
#    elif echo_text == "done":
#        done = True
#    else:
#        print(echo_text)
#else:
#    print("さようなら")
#

### 4-4 リスト内包表記
"""
リスト内包表記(List Comprehensions)は既存のリストやジェネレータから新しいリストを作るものです
例えば、1から10までの数値をそれぞれ2乗した数値のリストを作る場合は、リスト内包表記では以下のように書ける
"""
result = [x**2 for x in range(1,11)]
print(result)

"""
リスト内包表記は、既存のリストから取り出した要素に対して処理をするだけでなく、
条件にマッチした場合だけ新しいリストに追加したい場合にも使える
"""

result2 = [x**2 for x in range(1,11) if x%2 == 0]
print(result2)

"""
forを続けて2重ループと同じこともできます
"""

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

#### 内包表記のメリット
"""
内包表記は処理を簡潔にかけるほかに、
新しいリストなどへの追加メソッドの呼び出しにかかるコストを軽減できるメリットもある
"""

### 4-5 その他の内包表記
"""
リスト内包表記のほか、セットと辞書を生成する内包表記がある
"""
print({x**2 for x in range(1,11)})
print({x*2:x**2 for x in range(1,11)})

"""
リスト内包表記をジェネレータとして、処理を遅延することもできる
リスト内包表記の[]の替わりに()を使います
"""
res = (x**2 for x in range(1,11))
res = (x**2 for x in range(1,11))
print(next(res))
print(next(res))

### 4-6 例外処理
"""
制御フローの1つに、例外処理がある
例外処理はエラー処理ととらえられがちですが、
必ずしもすべてエラーに対する処理とは限らない
例外処理の基本は、例外が発生する可能性のある箇所をtryのブロックに記述し、exceptで例外を捕捉します
"""

try:
    10/0
except ZeroDivisionError:
    print('ZeroDivisionError occured')

"""
当然ですが、別のエラーで待ち構えている場合には例外は捕捉されず、
インタラクティブシェルの例外処理まで例外がとんでいってしまいます
"""

#try:
#    10/0
#except ValueError:
#    print('ValueError occured')

#### 4-6-1 例外オブジェクトを捕捉して利用する
"""
as 一時変数名
"""

try:
    10/0
except ZeroDivisionError as e:
    print(type(e))

"""
捕捉した例外オブジェクトには例外発生時のtracebackやメッセージが保持されています。
例えば、tracebackは__traceback__に格納されています
tracebackモジュールのformat_tb関数を用いて参照してみましょう
"""

from traceback import format_tb
try:
    10/0
except ZeroDivisionError as e:
    print(format_tb(e.__traceback__))
    print('メッセージ：{0}'.format(e.args))

#### 4-6-2 基底クラスで例外を捕捉する
"""
ZeroDivisionErrorの基底クラス(祖先にあたる例外クラス)で待ち受ければ、
基底クラスの子孫にあたるクラスの例外が飛んできた際に捕捉できます
基底クラスで捕捉した場合も、基底クラスに型変換されることなく、
一時変数には実際の例外クラスのインスタンスが格納されます
ArithmeticErrorというZeroDivisionErrorの規定クラスで待ち受けてみる
ArithmeticErrorは通常、数学的な例外の基底クラスとして利用される
"""

try:
    10/0
except ArithmeticError as e:
    print('{0}: {1}'.format(type(e), e))

#### 4-6-3 複数の例外を捕捉する
"""
例外は、複数の種類を1箇所で捕捉できる他、複数のexcept節を用いて発生した例外に応じた処理をすることもできる
例外に対して同じ処理をする場合には、exceptに(例外クラス1, 例外クラス2)と書くことで、両方の例外を補足できる
また、except節に捕捉する例外クラスを省略すると、すべての例外を捕捉する
ただし、例外は適切な粒度で捕捉し、何が起きているのか、何が問題なのかをユーザに通知すべき
"""

#def write(file_name, dict_input):
#    f = None
#    try:
#        f = open(file_name, 'w')
#        data = dict_input['data']
#        f.write(data)
#        f.close()
#    except KeyError as e:
#        print('エラー種別： {0}'.format(type(e)))
#        print(e)
#        print('キーが見つかりません： {0}'.format(str(dict_input)))
#    except (FileNotFoundError, TypeError) as e:
#        print('エラー種別：{0}'.format(type(e)))
#        print(e)
#        print('フィアルが開けませんでした： {0}'.format(file_name))
#    except:
#        print('何らかのエラーが発生しました')

#### 4-6-4 else/finally
"""
forやwhileと同様に、tryブロックが例外を発生せずに最後まで処理が進んだ場合、
elseブロックが実行されます。tryブロックが例外を発生してもしなくても、
実行されるfinallyブロックも定義できる
"""

#def write(file_name, dict_input):
#    f = None
#    try:
#        f = open(file_name, 'w')
#        data = dict_input['data']
#        f.write(data)
#    except KeyError as e:
#        print('エラー種別： {0}'.format(type(e)))
#        print(e)
#        print('キーが見つかりません： {0}'.format(str(dict_input)))
#    except (FileNotFoundError, TypeError) as e:
#        print('エラー種別：{0}'.format(type(e)))
#        print(e)
#        print('フィアルが開けませんでした： {0}'.format(file_name))
#    else:
#        print('問題なく処理が終了しました')
#    finally:
#        if f is not None:
#            print('ファイルを閉じます')
#            f.close()

#### 4-6-5 例外を送出する
"""
例外を送出するには、raiseキーワードを使用する
"""
#raise ValueError("高岡が出したエラー")

"""
IOErrorは引数にエラー番号と、エラーメッセージを設定することになっている
AssertionErrorに関しては、特殊な記法で送出できるシンタックスassert文がある

assert 条件テスト、メッセージ

AssertionErrorは状態の確認テストに失敗し際に送出する例外です
"""
left = 3
right = 2
#assert left < right , 'left must be smaller than right'

#### 例外をチェインする
"""
例外を捕捉したexcept節で例外が発生することがある
そんな時にはもともとの例外をたどれたほうが便利です
例外発生中に例外が発生した場合、その例外オブジェクトの__context__にもともとの例外オブジェクトが格納される
"""
#try:
#    f = open(None, 'w')
#except TypeError as e:
#    try:
#        f = open('', 'r')
#    except IOError as e:
#        print('直近のエラー: {0}'.format(e))
#        print('チェインしてきたエラー: {0}'.format(e.__context__))

"""
捕捉した例外を敢えて別の例外にして送出し直したいことがあります
そんな場合には、例外送出時にもとの例外を指定して送出できます
"""
class PerfectPythonError(Exception):
    pass

try:
    try:
        f = open(None, 'w')
    except TypeError as e:
        raise PerfectPythonError('ファイルが開けませんでした') from e
except PerfectPythonError as e:
    print('もともとの例外: {0} - {1}'.format(type(e.__cause__), e.__cause__.args))

#### 4-6-6 独自の例外を定義する
"""
ビルトインの例外クラスは基本的なもののみです
実際のアプリケーションの問題を取り扱う例外クラスは別途例外クラスを定義して利用します
ここでは、BaseExceptionのサブクラスのExceptionを継承する方法の例を紹介します
"""

class TextError(Exception):
    pass

### 4-7 with
"""
withを使うとopen,closeといった処理をより簡潔にかける
"""
#with open('text.txt', 'a') as f:
#    f.write('test')

"""
コンテキストマネージャになれるクラスを定義して、
withの仕組みをみてみる
"""
class WriteFile(object):
    def __init__(self, file_name):
        print('__init__が呼ばれました')
        self.file_name = file_name
    def __enter__(self):
        print('__enter__が呼ばれました')
        self.f = open(self.file_name, 'w')
        print('ファイルを開きました')
        return self.f
    def __exit__(self, type, value, traceback):
        print('__exit__が呼ばれました')
        self.f.close()
        print('ファイルを閉じました')

"""
使うときは、withに続けてクラスを生成する
クラスの仕組みにより、__init__が自動で呼ばれ、引数のファイル名を表す文字列が渡される
withはコンテキストマネージャを得ると、コンテキストマネージャの__enter__を呼び出す
__enter__は初期化コードを既述し、必要に応じて値を返します
この返したオブジェクトをwithはasに続けた一時変数に格納します。値は複数個返せます
__enter__で問題がない場合は、withのブロックへ処理が移ります
__enter__が正常に終了した時点で、withのブロックから出る際に__exit__が呼び出されることが保証される
"""

#with WriteFile('test3.txt') as f:
#    print('withのブロックに入りました')
#    f.write('寿限無寿限無')
#    print('withのブロックから出ます')

#### 4-7-1 closeする何かを簡単に扱う
"""
ファイルのように何かをcloseして終了したいものが多くあるため、
あらかじめ、closeingというコンテキストマネージャが用意されている
"""

from contextlib import closing
with closing(open('test3.txt', 'w')) as f:
    f.write('ジュゲムジュゲム')
