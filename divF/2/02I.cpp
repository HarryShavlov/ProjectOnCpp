В параде принимают участие M военных. 
Командование парада решило, что наиболее эффектное построение военных – в форме квадрата, то есть число участников построения должно быть точным квадратом. 
Но поскольку число M может не быть точным квадратом, разрешается разбить военных на несколько полков, каждый из которых строится в форме квадрата. 
Для красоты все полки должны быть одинакового размера, также командование парада хочет, чтобы размер каждого полка был как можно больше. 
Определите максимально возможный размер полка.

#include <iostream>
using namespace std; 
 
int main()
{
    int M, sz = 0;
    cin >> M;
    for( int i = 1; i * i <= M; i++ )
        if( M % (i * i) == 0 )
            sz = i * i;
    cout << sz << endl;                    
    return 0;
}
