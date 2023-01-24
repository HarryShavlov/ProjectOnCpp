Комната характеризуется тремя целыми числами: длиной, шириной и высотой, заданными в миллиметрах. 
Комната считается хорошей, если выполнены следующие условия: 
отношение меньшей из длины и ширины к высоте хотя бы 2, а также отношение большей из длины и ширины к меньшей не превосходит 2.
По заданным размерам комнаты определите, является ли она хорошей.
  
  
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;


int main()
{
    int w, l, h;
    cin >> w >> l >> h;
    if (min(w, l) / h >= 2 and max(w, l) / min(w, l) <= 2)
    {
        cout << "good";
    }
    else
    {
        cout << "bad";
    }
}