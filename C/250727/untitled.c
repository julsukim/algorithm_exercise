#include <stdio.h>
#include <string.h>  // strcpy 사용을 위해 필요

// 1) Person이라는 이름의 구조체 정의
typedef struct {
    char name[50];
    int  age;
} Person;

int main(void) {
    // 2) 구조체 변수 선언 및 초기화
    Person person = { "Junsu", 29 };

    // 3) & 연산자로 person 변수의 메모리 주소(address)를 얻어 포인터에 저장
    Person *pPerson = &person;
    //    └─ pPerson은 Person을 가리키는 포인터(int *p 같은 개념)

    // 4) * 연산자(dereference)로 포인터가 가리키는 실제 값을 읽기
    printf("Before: %s is %d years old\n",
           (*pPerson).name,    // (*pPerson)로 struct 전체를 역참조한 뒤 .name
           (*pPerson).age);    // (*pPerson).age

    // 5) * 연산자를 이용해 값 쓰기
    (*pPerson).age = 30;     // (*pPerson).age를 30으로 변경

    // 6) -> 연산자로 더 간결하게 “포인터→멤버” 접근
    pPerson->age = 31;       // (*pPerson).age 대신 pPerson->age
    strcpy(pPerson->name, "Kim Junsu");  // pPerson->name

    // 최종 결과 출력
    printf("After : %s is %d years old\n",
           pPerson->name,
           pPerson->age);

    return 0;  
}
