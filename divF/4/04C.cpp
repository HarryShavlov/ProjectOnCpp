Напишите функцию int func2 от одной переменной типа int, которая вызывает функцию int encode (int, int, double) от глобальных переменных N и M и константы 3.14, 
после чего возвращает произведение полученной на вход переменной и результата вычисления функции encode.
Обратите внимание, что отправляемый код должен состоять только из одной функции — функции func2.

int func2(int a)
	{
		return a *encode(N,M,3.14);
	}