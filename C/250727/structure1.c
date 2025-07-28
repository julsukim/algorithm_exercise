#include <stdio.h>
#include <string.h>

// 1) 구조체 정의: 사람(Person)의 이름, 나이, 키 정보를 담는다.
typedef struct {
    char name[50];
    int  age;
    float height;   // 단위: cm
} Person;

// 2) 구조체를 출력하는 함수: 포인터로 받아서 -> 연산자 사용
void printPerson(const Person *p) {
    // p->name, p->age, p->height 로 각 멤버에 접근
    printf("이름: %s\n", p->name);
    printf("나이: %d세\n", p->age);
    printf("키: %.1fcm\n", p->height);
}

int main(void) {
    // 3) 스택에 구조체 인스턴스 생성 및 초기화
    Person p1;                   // 메모리 할당 (쓰레기 값)
    strcpy(p1.name, "Kim Junsu"); // name 필드 초기화
    p1.age    = 29;              // age 필드 초기화
    p1.height = 175.5f;          // height 필드 초기화

    // 4) . 연산자로 직접 접근
    printf("== 직접 접근 ==\n");
    printf("%s, %d세, %.1fcm\n\n", p1.name, p1.age, p1.height);

    // 5) 포인터로 구조체를 가리키기
    Person *ptr = &p1;   // &p1: p1의 주소를 ptr에 저장

    // 6) -> 연산자로 멤버 접근
    ptr->age += 1;       // 나이를 1살 증가시킨다
    strcpy(ptr->name, "Kim J."); // 이름 변경

    printf("== 포인터 -> 연산자 ==\n");
    printf("%s, %d세, %.1fcm\n\n", ptr->name, ptr->age, ptr->height);

    // 7) 함수에 포인터 전달
    printf("== printPerson 함수 호출 ==\n");
    printPerson(ptr);

    return 0;
}
