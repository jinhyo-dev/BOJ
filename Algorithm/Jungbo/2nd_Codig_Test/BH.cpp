#include <iostream>
using namespace std;
int a, b;

int main()
{
  char s;
  cin >> a >> b >> s;
  switch (s)
  {
    case '+':
      printf("%d", a+b);
      break;
    case '-':
      printf("%d", a-b);
      break;
    case '*':
      printf("%d", a*b);
      break;
    case '/':
      printf("%.2f", (float)a/b);
      break;
    case '%':
      printf("%d", a%b);
      break;
    case 'a':
      printf("%d", a&b);
      break;
    case 'o':
      printf("%d", a|b);
      break;
    case 'x':
      printf("%d", a^b);
      break;
  }
}