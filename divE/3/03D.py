Дано натуральное число N. Рассмотрим его разбиение на натуральные слагаемые. 
Два разбиения, отличающихся только порядком слагаемых, будем считать за одно, поэтому можно считать, что слагаемые в разбиении упорядочены по невозрастанию.

def f(a, n, p):
    if n:
        for i in range(1, n+1):
            if i <= p:
                f(a + [i], n - i, i)
    else:
        print(*a, sep=' ')

n = int(input())
f([], n, n)