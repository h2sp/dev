# -*- coding: utf-8 -*--

a,b = 0,1
while b < 10:
    print (b)
    a,b = b, a+b

x = int(input("整数を入れてください: "))

if x < 0:
    x = 0
    print('負数は0とする')
elif x == 0:
    print('ゼロ')
elif x == 1 :
    print('ひとつ')
else:
    print('もっと')


a = ['cat', 'window', 'defenestrate']

for x in a:
    print(x, len(x))

