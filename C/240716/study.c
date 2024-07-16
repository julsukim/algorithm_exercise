#include<stdio.h> // 선행처리기

// int main() {
//   printf("안녕");
//   printf("안녕\n");
//   printf("안녕하세요");
//   return 0;
// }

// 자료형
// 1. 정수형
// char 1바이트
// short 2바이트
// int 4바이트
// long 4바이트
// long long 8바이트
// 2. 실수형
// float 4바이트
// double 8바이트
// long double 8바이트 이상
// int main() {
//   int a = 3;
//   printf("%d", a);
//   return 0;
// }

// %d : 10진 정수형 출력
// %f : 실수형 출력
// %c : 문자 출력
// %s : 문자열 출력
// %o : 8진 정수형 출력
// %x : 16진 정수형 출력
// %e : 지수형 출력
// %u : 부호 없는 10진 정수형 출력
// %g : e와 f 중에서 출력할 자리를 덜 차지하는 형태로 자동 출력
// %p : 포인터의 주소 값 출력
// int main() {
//   char a = 'A';
//   printf("%d\n", a); // 정수형으로 출력 => 아스키코드 값이 출력
//   printf("%c\n", a); // 문자형으로 출력
//   printf("%d\n", a+1);
//   printf("%c\n", a+1);
//   return 0;
// }

// &은 앰퍼샌드(ampersand), 주소연산자
// &a는 변수 a의 주소
// scanf에서 a가 아니라 &a라고 작성하는 이유
// - 임시공간(레지스터)에 저장된 값을 변수의 주소에 저장하고 임시공간을 삭제하기 때문
// int main() {
//   int a;
//   scanf("%d", &a);
//   printf("%d", a);
//   return 0;
// }

// 증감연산자 (증감연산자는 사칙연산보다 먼저 연산)
// ++a 전치연산 => 바로 계산
// a++ 후치연산 => 그 다음 라인부터 계산
int main() {
  int a = 10;
  int b = 15;
  int c = a++ + --b; // 10 + 14
  int d = ++a + b--; // 12 + 14

  printf("%d\n", a); // 12
  printf("%d\n", b); // 13
  printf("%d\n", c); // 24
  printf("%d", d); // 26
  return 0;
}