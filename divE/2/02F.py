Напишите программу моделирующую работу дека, реализовав все указанные здесь методы. 
Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. 
После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

push_front - Добавить в начало дека новый элемент. Программа должна вывести ok.
push_back - Добавить в конец дека новый элемент. Программа должна вывести ok.
pop_front - Извлечь из дека первый элемент. Программа должна вывести его значение.
pop_back - Извлечь из дека последний элемент. Программа должна вывести его значение.
front - Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.
back - Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.
size - Вывести количество элементов в деке.
clear - Очистить дек (удалить из него все элементы) и вывести ok.
exit - Программа должна вывести bye и завершить работу.

Гарантируется, что количество элементов в деке в любой момент не превосходит 100. Все операции pop_front, pop_back, front, back всегда корректны.

command=['push_front','push_back', 'pop_front','pop_back', 'back', 'size', 'clear', 'exit', 'front']
a=[]
b='0'

while True:
    while b[0] not in command:
        s = input('')
        b = s.split()
    if b[0]=='push_front':
        a.insert(0,b[1])
        print('ok')
    elif b[0] == 'push_back':
        a.append(b[1])
        print('ok')
    elif b[0]=='size':
        print(len(a))
    elif b[0]=='clear':
        a.clear()
        print('ok')
    elif b[0]=='exit': print('bye'); break
    elif b[0]=='pop_back' and len(a)>0:
        print(a.pop())
    elif b[0]=='pop_front' and len(a)>0:
        print(a.pop(0))
    elif b[0]=='back' and len(a)>0:
        print(a[-1])
    elif b[0] == 'front' and len(a)>0:
        print(a[0])
    b[0]='0'