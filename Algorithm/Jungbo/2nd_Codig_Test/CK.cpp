#include <iostream>
int total, min = 100000, max = -100000;
float avg;
int n, i, point[100000];
int main()
{
  scanf("%d", &n);

  for (i = 0; i < n; i++)
    scanf("%d", &point[i]);

  for (i = 0; i < n; i++)
    total += point[i];

  avg = (float)total / n;
  
  printf("총점: %d\n", total);
  printf("평균: %.2f\n", avg);

  for (i = 0; i < n; i++)
  {
    if (max < point[i])
      max = point[i];
    if (min > point[i])
      min = point[i];
  }

  printf("최고점: %d\n", max);
  printf("최저점: %d", min);
}
