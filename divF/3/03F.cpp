В связи с визитом Императора Палпатина было решено обновить состав дроидов в ангаре 32. 
Из-за кризиса было решено новых дроидов не закупать, но выкинуть пару старых. 
Как известно, Палпатин не переносит дроидов с маленькими серийными номерами, так что все, что требуется - найти среди них двух, у которых серийные номера наименьшие.

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, t, k = 0, idx = 0;
    cin >> n;
    vector<int> a(n);
    for(int i = 0; i < n; ++i){
        cin >> a[i];
    }
    sort(a.begin(), a.end());
    cout << a[0] << " " << a[1];
    return 0;
}