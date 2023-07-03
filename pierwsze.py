print('Hello world')
# 1
a = 2
b = 5
c = 5.0
d = 4.2
print(a, b, c, d)
print(a + b, a + c, a + d)
print(a * b, a * c, a * d)
print(a / b, a / c, a / d)
# 2
s = 'kot'
t = 'pies'
print(s, t)
print(s + t, t + s + t, 2 * s)
# 3
i = input('Podaj i: ')
j = input('Podaj j: ')
print(i, j, i + j)
# 4
i = int(input('Podaj i: '))
j = int(input('Podaj j: '))
print(i, j, i + j)
# 5
x = int(input('Podaj x: '))
y = int(input('Podaj y: '))
print(x % y)
print(x // y)
# 6
x = int(input('Podaj x: '))
y = int(input('Podaj y: '))
z = int(input('Podaj z: '))
if x > 10:
    print(x)
if y > 10:
    print(y)
if z > 10:
    print(z)
# 7
x = int(input('Podaj x: '))
if x % 2 == 0:
    print('Liczba jest parzysta')
else:
    print('Liczba jest nieparzyta')
# 8
R = int(input('Podaj rok: '))
if R % 4 == 0:
    if R % 100 == 0:
        if R% 400 == 0:
            print('Rok', R, 'jest przestępny.')
        else:
            print('Rok', R, 'nie jest przestępny.')
    else:
        print('Rok', R, 'jest przestępny.')
else:
    print('Rok', R, 'nie jest przestępny.')

# 9
f = float(input('Podaj liczbę zmiennoprzecinkowa: '))
length = len(str(f)) - len(str(int(f)))+1
print(int(f % (f+1)))
print(str((f % 1))[2:length])

# 10
f = float(input('Podaj liczbę f: '))
fcal = str(int(f))
g = float(input('Podaj liczbę g: '))
gcal = str(int(g))
g = str(g)[len(gcal):]
f = str(f)[len(fcal):]
g = fcal + g
f = gcal + f
print(f)
print(g)

# 11
i = int(input('Podaj i: '))
j = int(input('Podaj j: '))
if i ** j > j ** i:
    print(i, 'do', j, 'równe', i ** j, 'jest większe od', j, 'do', i, 'równe', j ** i, end='.\n')
else:
    print(j, 'do', i, 'równe', j ** i, 'jest większe od', i, 'do', j, 'równe', i ** j, end='.')

#12
x = 2
n = 2
n2res = result = x ** (1 / n)
print(result)
x = 3
n = 3
n3res = result = x ** (1 / n)
print(result)
x = 5
n = 5
result = x ** (1 / n)
print(result)
if n2res > n3res:
    if n2res > result:
        print('pierwiastek stopnia 2 z 2 równy', n2res, 'jest największy')
    else:
        print('pierwiastek stopnia 5 z 5 równy', result, 'jest największy')
elif n3res > result:
    print('pierwiastek stopnia 3 z 3 równy', n3res, 'jest największy')
else:
    print('pierwiastek stopnia 5 z 5 równy', result, 'jest największy')
