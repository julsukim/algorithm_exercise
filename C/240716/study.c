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
// int main() {
//   int a = 10;
//   int b = 15;
//   int c = a++ + --b; // 10 + 14
//   int d = ++a + b--; // 12 + 14

//   printf("%d\n", a); // 12
//   printf("%d\n", b); // 13
//   printf("%d\n", c); // 24
//   printf("%d", d); // 26
//   return 0;
// }

// 비트연산자
// 2진수
// & 둘다 1일 때만 1 반환
// ^ 1개는 1, 1개는 0일 때만 1 반환
// | 둘 중 하나만 1일 때도 1 반환
// >> 비트 이동 : 8>>2 라면, 8에서 2의 제곱만큼 나눠준다
// << 8<<2 라면, 8에서 2의 제곱만큼 곱해준다

// static 변수
// - 블록 내외부 상관없이 선언
// - 프로그램이 시작되면 변수 생성, 종료 시 변수 소멸
// - (지역 변수는 블록이 닫히면 소멸)
// void fn() {
//   static int a = 3;
//   int b = 3;
//   a++;
//   b++;
//   printf("%d %d\n", a, b);
// }
// int main() {
//   fn();
//   fn();
//   return 0;
// }

// 포맷 스트링
// int main() {
//     int a=4, c=5;
//     char b = 'A';
//     printf("a는 %d, b는 %c입니다.", a, b);
//     printf("%d", a+c);
//     return 0;
// }

// 변수 상세 출력
// %[-][0][전체자리수].[소수점자리수]스트링
// - : 붙이면 왼쪽 정렬 (- 붙이지 않고, 전체자릿수가 정해져있다면 오른쪽 정렬)
// 0 : 붙이면 전체 자릿수에서 앞에 빈공간 만큼 0을 채움 (뒤는 붙이지 않음)
// 전체자리수 만큼 공간 확보 (소수점 . 도 한자릿수로 포함)
// 소수점자리수 만큼 소수점이 출력 (실수형일 때만 적용)
// int main() {
//     float a = 1.234;
//     int b = 10;
//     printf("%.2f\n", a); // 1.23
//     printf("%5.1f\n", a); //   1.2
//     printf("%05.1f\n", a); // 001.2
//     printf("%-05.1f\n", a); // 1.2
//     printf("%5d\n", b); //    10
//     printf("%05d\n", b); // 00010
//     printf("%-5d\n", b); // 10
//     printf("%-05d\n", b); // 10
//     return 0;
// }

// scanf(포맷_스트링이_포함된_문자열, 변수의_주솟값, ...);
// int main() {
//     int a;
//     char b;
//     scanf("%d %c", &a, &b);
//     printf("a는 %d, b는 %c 입니다.", a, b);
//     return 0;
// }

// gets(문자열_배열_함수)
// 키보드로 입력받은 문자열을 문자형 배열에 저장
// int main() {
//     char a[10];
//     gets(a);
//     printf("%s", a);
//     return 0;
// }

// 연산자
// 우선순위
// 같은지 다른지보다 대소비교가 우선순위가 더 높다.

// 증감 연산자
// x++ : 변수의 값을 사용한 후에 1 증가
// ++x : 변수를 1 증가시킨 후에 사용

// 산술 연산자
// int main() {
//     int x = 3, y = 2;
//     float z = 2.0;
//     printf("%d %d\n", x%y, y%x); // 1 2
//     printf("%d %.2f", x/y, x/z); // 1 1.50
//     return 0;
// }

// 포인터
// 포인터는 변수의 주솟값을 저장하는 공간
// 자료형* 포인터_변수명 = &변수명;
// 자료형 (char, int, float) 뒤에 *를 붙이면 주소를 저장하는 포인터 변수를 의미
// 변수명 뒤에 &를 붙이면 해당 변수명의 주솟값이다.
// 주소에 해당하는 값을 가리킬때는 *를 사용한다.
// int main() {
//     int a = 10;
//     int* b = &a;
//     printf("%d %d %d", a, *b, *(&a)); // 10 10 10
//     return 0;
// }

// 배열과 포인터
// 배열의 i번지 주소 : 배열+i == &배열[i];
// 배열의 i번지 값 : *(배열+i) == 배열[i];

// 1차원 배열과 1차원 포인터
// 1차원 배열에서 배열명만 단독으로 사용할 경우 1차원 포인터와 동일
// 1차원 배열일 때는 배열명[요소] 형태, *(배열명+요소)일 경우 값을 가리키고,
// 1차원 포인터일 때는 포인터[요소] 형태, *(포인터+요소)일 경우 값을 가리킨다
// int main() {
//     int a[3] = {1, 2};
//     int *p = a;
//     printf("%d %d %d\n", a[0], a[1], a[2]); // 1 2 0
//     printf("%d %d %d\n", *a, *(a+1), *(a+2)); // 1 2 0
//     printf("%d %d %d\n", p[0], p[1], p[2]); // 1 2 0
//     printf("%d %d %d\n", *p, *(p+1), *(p+2)); // 1 2 0
//     return 0;
// }

// 2차원 배열과 1차원 포인터
// 2차원 배열에서 배열명만 단독으로 사용할 경우 2차원 포인터와 동일하다
// 2차원 배열일 때는 배열명[요소] 형태, *(배열명+요소)는 1차원 포인터와 동일하고,
// 1차원 포인터에 대해 *과 []을 이용해야 값을 가리킬 수 있다.
// int main() {
//     int a[3][2] = {{1, 2}, {3, 4}, {5, 6}};
//     int *p = a[1];
//     printf("%d %d %d\n", *a[0], *a[1], *a[2]);
//     printf("%d %d %d\n", **a, **(a+1), **(a+2)); // **a는 a[0][0]을 의미
//     printf("%d %d\n", *p, *(p+1));
//     printf("%d %d\n", p[0], p[1]);
//     return 0;
// }

// int main() {
//     int a[3][2] = {{1, 2}, {3, 4}, {5, 6}};
//     int *p[3] = {a[2], a[0], a[1]};
//     printf("%d\n", **a);
//     printf("%d %d %d\n", a[0], a[1], a[2]);
//     printf("%d %d %d\n", a[0][0], a[1][0], a[2][0]); // 1 3 5
//     printf("%d %d %d\n", *a[0], *a[1], *a[2]); // 1 3 5
//     printf("%d %d %d\n", p[1][0], p[2][0], p[0][0]); // 1 3 5
//     printf("%d %d %d\n", *p[1], *p[2], *p[0]); // 1 3 5
//     return 0;
// }

// 2차원 배열과 2차원 포인터
// 2차원 배열에서 배열명만 단독으로 사용할 경우 2차원 포인터와 동일
// 2차원 배열에서 배열명[요소][요소], *배열명[요소], **(배열명+요소)일 경우 값을 가리킨다.

// int main() {
//     int a[3][2] = {{1, 2}, {3, 4}, {5, 6}};
//     int (*p)[2] = a;
//     int (*q)[2] = a+1;
//     printf("%d %d %d\n", a[0][0], a[0][1], a[1][0]); // 1 2 3
//     printf("%d %d %d\n", p[0][0], p[0][1], p[1][0]); // 1 2 3
//     printf("%d %d %d\n", q[0][0], q[0][1], q[1][0]); // 3 4 5
//     return 0;
// }

// 구조체와 포인터
// 구조체는 일반 구조체 변수로 접근할때는 . 으로 접근하고,
// 구조체 포인터로 접근할 때는 -> 로 접근한다.

// struct Student{
//     char gender;
//     int age;
// };
//
// int main() {
//     struct Student s = {'F', 21};
//     struct Student *p = &s;
//     printf("%c %d\n", s.gender, s.age);
//     printf("%c %d\n", (&s)->gender, (&s)->age);
//     printf("%c %d\n", p->gender, p->age);
//     printf("%c %d\n", (*p).gender, (*p).age);
//     printf("%c %d\n", p[0].gender, p[0].age);
//     return 0;
// }

// 1차원 구조체 배열과 1차원 구조체 포인터
// 1차원 구조체 배열에서 배열명만 단독으로 사용할 경우 1차원 구조체 포인터와 동일
// 1차원 구조체 배열일 때 배열명[요소].변수명 형태, (*(배열명+요소)).변수명,
//     배열명->변수명 형태, (배열명+요소)->변수명 형태로 값을 가리킨다.
// 1차원 포인터일 때 포인터[요소].변수명, (*(포인터+요소)).변수명,
//     포인터->변수명, (포인터+요소)->변수명 형태로 값을 가리킨다.

// 함수 포인터
// 함수 포인터는 함수의 주소를 저장하고, 해당 주소의 함수를 호출하는데 사용하는 포인터
// 리턴타입 (*함수_포인터)(함수_파라미터);

// void fn1() {
//     printf("fn1 함수\n");
// }
// int fn2(int a) {
//     printf("fn2 함수: %d\n", a);
//     return 0;
// }
// int main() {
//     void (*pf1)();
//     int (*pf2)(int);
//     fn1();
//     fn2(5);
//     pf1 = fn1;
//     pf2 = fn2;
//     pf1();
//     pf2(2);
//     return 0;
// }

// 사용자 정의 함수 포인터 반환
// 사용자 정의 함수의 반환 값으로 포인터를 전달 받을 수 있다.
// #include<string.h>

// char n[6];
// char *soojebi() {
//     strcpy(n, "Hello");
//     return n;
// }
// int main() {
//     char *p = soojebi();
//     printf("%s\n", p);
//     return 0;
// }

// 표준 함수
#include<string.h>

// strcat 문자열끼리 연결하는 함수
// strcat(dest, src); src의 문자열을 dest뒤에 붙임
// strncat(dest, src, maxlen); src의 문자열에서 maxlen의 개수만큼 dest뒤에 붙임
// int main() {
//     char a[20] = "Hello";
//     char b[10] = "Soojebi";
//     strcat(a, b);
//     printf("%s\n", a);
//     strncat(a, b, 3);
//     printf("%s\n", a);
//     return 0;
// }

// strcpy 문자열을 복사하는 함수
// strcpy(dest, src); src의 문자열을 dest 문자열에 복사
// strncpy(dest, src, maxlen); src의 문자열을 maxlen의 개수만큼 dest 문자열에 복사
// int main() {
//     char a[20] = "Hello";
//     char b[10] = "Soojebi";
//     strncpy(a, b, 3);
//     printf("%s\n", a); // Soolo
//     return 0;
// }

// strcmp 문자열의 ASCII 코드를 비교
// strcmp(s1, s2);
// strncmp(s1, s2, maxlen); maxlen 길이 만큼만 s1과 s2를 비교
// s1이 s2보다 크면 1을, s1과 s2가 같으면 0, s1이 s2보다 작으면 -1을 반환

// strlen 문자열의 길이를 알려준다.

// strrev 문자열을 거꾸로 뒤집는 함수

// strchr 문자열 내에 일치하는 문자가 있는지 검사하는 함수
// strchr(str, cl); str 내에 c가 존재하는지 알려줌 (위치를 반환, 없으면 NULL)

// int main() {
//     char a[20] = "Hello";
//     char* p = strchr(a, 'k'); // 첫번째 l이 나온 위치를 반환하여 포인터 변수에 저장
//     printf("%s", p); // llo
//     return 0;
// }


// 수학 함수

// sqrt 는 양의 제곱근을 계산하는 함수

// ceil은 소수점 올림 함수

// floor은 소수점 내림 함수

// 유틸리티 함수

// rand() 임의의 정수값 1개를 생성

// srand(seed); seed값에 따라 난수발생기를 초기화한다.

// time(NULL); time 함수는 1970 1월 1일 이후로 몇 초가 경과했는지 나타낸다.
// 파라미터를 NULL로 하면 현재 시간을 리턴

// atoi(str); 문자열을 정수형으로 변환

// atof(str); 문자열을 실수형으로 변환

// itoa(value, str, radix); value를 변환하여 str에 radix 진수로 저장