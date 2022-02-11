 #include<stdio.h>

   
 int main()
 {
 	int n,old,man,teen,kid,a;
 	n = 0;
 	old = 0;
 	man = 0;
 	teen = 0;
 	kid = 0;
 	a = 0;
	scanf("%d", &n);

	while(1)
	{
		if (n<=7)
		{
			kid++;
		}
		else if (n>=8&&19>=n)
		{
			teen++;
		}
		else if (n>=20&&64>=n)
		{
			man++;
		}
		else if (n>=65)
		{
			old++;
		}
		scanf("%d", &n);
		if (n == 0){
			a = a + 1;			break;
		}
		a++;

	} 
	
	printf("..조사 종료..\n<귀 댁의 가족 구성>\n총 %d명 : 노인 %d명, 성인 %d명, 청소년 %d명, 아동 %d명", a,old,man,teen,kid);
	
 }