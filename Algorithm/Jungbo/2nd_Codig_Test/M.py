n = int(input())

def round(n):
  n = (2 * 3.14 * n)
  return n

def area(n):
  n = (3.14 * n * n)
  return n

print('반지름 :', n)
print('둘레 :', round(n))
print('넓이:', area(n))

# include <stdio.h>
# int main(){
# 	int a;
# 	scanf("%d", &a);
# 	float b,c;
# 	b = 2 * 3.14 * a;
# 	c = 3.14 * a * a;
# 	printf("반지름 : %d\n둘레 : %f\n넓이 : %f", a,b,c);
# 	return 0;
# }