Напишите функцию my_swap, которая получает на вход адреса двух переменных типа int, меняет содержимое этих переменных местами и возвращает 0.
Отправляемый код не должен содержать ничего, кроме соответствующей функции.

int my_swap(int *a, int *b) {
    int swap = *a;
    *a = *b;
    *b = swap;
    return 0;
}
