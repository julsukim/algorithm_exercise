import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

// static 변수
//class Soojebi {
//    static int count = 0;
//}

// static 메서드
//class Soojebi {
//    static void print() {
//        System.out.println("static method");
//    }
//}

//public class Study {

    // 클래스 변수
//    int a = 5;
//    void fn() {
//        a = a + 3;
//    }
//    public static void main(String[] args) {
//        Study s = new Study();
//        s.a = s.a + 5;
//        s.fn();
//        System.out.println(s.a);
//    }

    // 지역 변수
//    public static void main(String[] args) {
//        int a = 3;
//        System.out.println(a);
//    }

    // static 변수
    // 프로그램이 종료될 때까지 소멸되지 않음
//    public static void main(String[] args) {
//        Soojebi s = new Soojebi();
//        s.count++;
//        System.out.println(s.count);
//        s.count++;
//        System.out.println(s.count);
//    }

    // 1차원 배열
    // 초깃값이 없는 경우 : 자료형 []배열명 = new 자료형[배열_요소_개수];
    //                 : 자료형 배열명[] = new 자료형[배열_요소_개수];
    // 초깃값이 있는 경우 : 자료형 []배열명 = {초깃값};
    // 초깃값을 선언하지 않는 경우 정수는 0, 실수는 0.0, 문자열은 NULL이 저장
    // length 속성을 통해서 배열의 크기를 구할 수 있다.
//    public static void main(String[] args) {
//        int []a = new int[3];
//        System.out.println(a.length);
//    }

    // 2차원 배열
    // 초깃값이 없는 경우 : 자료형 [][]배열명 = new 자료형[행의 개수][열의 개수];
    //                 : 자료형 배열명[][] = new 자료형[행의 개수][열의 개수];
    // 초깃값이 있는 경우 : 자료형 [][]배열명 = {{초깃값}, {초깃값}, ... };
//    public static void main(String[] args) {
//        int [][]a = new int[3][2];
//        System.out.println(a.length);
//        System.out.println(a[0].length);
//    }

    // 표준 입출력 함수

    // 표준 출력 함수
    // System.out.print(); 개행을 하지 않는 출력함수
    // System.out.println(); 개행을 하는 출력함수
    // System.out.printf(); C언어 처럼 변수를 출력할 수 있는 출력 함수
//    public static void main(String[] args) {
//        int a = 100;
//        System.out.print("Hello");
//        System.out.println("Hello");
//        System.out.printf("%d", a);
//    }

    // 표준 입력 함수
    // System.in.readline() 입력장치(키보드)로부터 라인 전체를 읽는 표준 입력 함수
//    public static void main(String[] args) throws IOException {
//        String a = null;
//        BufferedReader r =
//                new BufferedReader(new InputStreamReader(System.in));
//        a = r.readLine();
//
//        System.out.println(a);
//    }

    // 문자열

    // 문자열 생성
    // 1. 리터럴을 이용
    // String 변수명 = "문자열";
    // 리터럴 문자열은 문자열 풀에 저장, 같은 리터럴을 사용하는 변수는 같은 문자열 풀을 가리킴
    // 2. new를 이용
    // String 변수명 = new String("문자열");
    // 문자열 인스턴스를 생성하여 String 변수에 주소값을 대입
    // String 인스턴스는 힙에 저장되고, 변수는 힙에 저장된 인스턴스의 주소를 대입
//    public static void main(String[] args) {
//        String a = "abc";
//        String b = "abc";
//        String c = new String("abc");
//        String d = new String("abc");
//
//        System.out.println(a);
//        System.out.println(b);
//        System.out.println(c);
//        System.out.println(d);
//    }

    // 문자열 연결
    // 문자열과 문자열, 문자열과 정수, 문자열과 실수를 더하게 되면 문자열이 된다.

    // 문자열 비교
    // 1. == 연산자
    // 문자열의 주소값을 비교
    // 2. equals 메서드
    // 문자열 자체를 비교
//    public static void main(String[] args) {
//        String a = "abc";
//        String b = "abc";
//        String c = new String("abc");
//        String d = new String("abc");
//        String e = a;
//
//        System.out.println(a == b); // true
//        System.out.println(a == c); // false
//        System.out.println(b == e); // true
//        System.out.println(c == d); // false
//        System.out.println(d == e); // false
//
//        System.out.println(a.equals(b)); // true
//        System.out.println(a.equals(c)); // true
//        System.out.println(b.equals(e)); // true
//        System.out.println(c.equals(d)); // true
//        System.out.println(d.equals(e)); // true
//    }


    // 반복문
    // for each
    // for( 제어변수: 배열 ) { 문장; }
//    public static void main(String[] args) {
//        String[] name = {"Soo", "Je", "Bi"};
//        for( String nm : name ) {
//            System.out.println(nm);
//        }
//    }

    // 메서드
    // 사용자 정의 함수 (메서드)
    // 사용자가 직접 새로운 함수를 정의하여 사용
    // 사용자 정의 함수에서 매개변수나 생성된 변수는 사용자 정의 함수가 종료되면 없어진다
    // 자료형 함수명(자료형 변수명, ...){ 명령어; return 반환값; }
//    static char fn(int num) {
//        if(num % 2 == 0) return 'Y';
//        else return 'N';
//    }
//    public static void main(String[] args) {
//        char a = fn(5);
//        System.out.print(a);
//    }

    // static 메서드
    // 클래스가 메모리에 올라갈 때 자동적으로 생성되는 메서드
    // 인스턴스를 생성하지 않아도 호출이 가능하게 된다.
//    public static void main(String[] args) {
//        Soojebi.print();
//    }


    // 클래스
    // 클래스는 객체 지향 프로그래밍 (OOP)에서 특정 객체를 생성하기 위해 변수와 메서드를 정의하는 틀이다.

    // 클래스 접근 제어자
    // 지정된 클래스, 변수, 메서드를 외부(같은 혹은 다른 패키지)에서 접근할 수 있도록 권한을 설정하는 기능
    // public : 외부의 모든 클래스에서 접근이 가능한 접근 제어자
    // protected : 같은 패키지 내부에 있는 클래스, 하위 크래스(상속받은 경우)에서 접근이 가능한 접근 제어자
    //           : 자기 자신과 상속받은 하위 클래스 둘 다 접근이 가능한 접근 제어자
    // default : 접근 제어자를 명시하지 않은 경우로 같은 패키지 내부에 있는 클래스에서 접근이 가능
    // private : 같은 클래스 내에서만 접근이 가능한 접근 제어자

    // 클래스 정의
    // 클래스에서 변수는 변수 선언과 동일, 메서드는 사용자 정의 함수와 문법이 동일.
    // 일반적으로 변수는 private 접근 제어자를 사용하여 외부에서 접근하지 못하게 함
    // 메서드는 외부에 공개할 것만 public 접근 제어자를,
    // 그렇지 않으면 protected나 private 접근 제어자를 사용하여 정보은닉을 한다.

    // 클래스 변수 생성
    // 클래스는 객체를 생성하기 위해 변수와 메서드를 정의하는 틀이므로,
    // 실제 변수에 들어갈 인스턴스를 new 키워드로 생성해주어야한다.
    // 변수를 이용해 클래스의 메서드에 접근한다.

    // 클래스 this
    // this는 현재 객체를 가리키는 키워드.
    // 클래스 내부의 변수와 메서드를 가리킬 수 있다.
    // 클래스 내부 변수 접근 : this.변수;
    // 클래스 내부 메서드 접근 : this.메서드(매개변수);
    // 클래스 내부 생성자 호출 : this(매개변수);

//    private int a;
//    public void setA(int a) {
//        this.a = a;
//    }
//    public int getA() {
//        return a;
//    }
//    public static void main(String[] args) {
//        Study std = new Study();
//        std.setA(5);
//        System.out.print(std.getA());
//    }

    // 생성자
    // 생성자는 해당 클래스의 객체가 생성될 때 자동으로 호출되는 특수한 종류의 메서드
    // 일반적으로 클래스 멤버 변수를 초기화하거나 클래스를 사용하는 데 필요한 설정이 필요한 경우 사용
    // 생성자는 클래스 명과 동일한 메서드명을 가지고, 반환 값이 없다.
    // 생성자가 없을 경우 public 클래스명(){}이라는 아무 일도 하지 않는 생성자가 있는 것처럼 동작
//    public Study(){
//        System.out.println("A");
//    }
//    public Study(int a) {
//        System.out.println("B: " + a);
//    }
//    public void fn() {
//        System.out.println("C");
//    }
//    public static void main(String[] args) {
//        Study s1 = new Study();
//        Study s2 = new Study(5);
//        s1.fn();
//    }
//}

// 클래스 상속
// 어떤 객체가 있을 때 그 객체의 변수와 메서드를 다른 객체가 물려받는 기능
// 자식 클래스를 생성하면 무조건 부모 클래스의 생성자를 실행한 후에 자식 클래스의 생성자를 실행한다.
// class 부모 {} class 자식 extends 부모 {}

//class A {
//    public void fnA() {
//        System.out.println("A");
//    }
//}
//class B extends A {
//    public void fnB() {
//        System.out.println("B");
//    }
//}
//public class Study {
//    public static void main(String[] args) {
//        B b = new B();
//        b.fnA();
//        b.fnB();
//    }
//}

// 오버로딩
// 오버로딩은 동일 이름의 메서드를 매개변수만 다르게 하여 여러 개 정의할 수 있는 기능
// - 메서드 이름이 같아야 한다
// - 매개변수 개수가 달라야 한다
// - 매개 변수가 개수가 같을 경우 데이터 타입이 달라야 한다.
// - 반환형은 같거나 달라도 된다
//class A {
//    public void fn() {
//        System.out.println("A");
//    }
//    public void fn(int i) {
//        System.out.println(i);
//    }
//    public void fn(double d) {
//        System.out.println(d);
//    }
//    public int fn(int a, int b) {
//        return a+b;
//    }
//}
//public class Study {
//    public static void main(String[] args) {
//        A a = new A();
//        a.fn();
//        a.fn(7);
//        a.fn(10.0);
//        System.out.println(a.fn(2, 4));
//    }
//}

// 오버라이딩
// 오버라이딩은 하위 클래스에서 상위 클래스 메서드를 재정의할 수 있는 기능
// - 오버라이드하고자 하는 메서드가 상위 클래스에 존재하여야 한다.
// - 메서드 이름은 같아야 한다.
// - 메서드 매개변수 개수, 데이터 타입이 같아야 한다.
// - 메서드 반환형이 같아야 한다.
//class A {
//    public void fn() {
//        System.out.println("A");
//    }
//}
//class B extends A {
//    public void fn() {
//        System.out.println("B");
//    }
//}
//public class Study {
//    public static void main(String[] args) {
//        A a = new A();
//        B b = new B();
//        a.fn();
//        b.fn();
//    }
//}

//class Parent {
//    public Parent() {
//        System.out.println("A");
//    }
//    public Parent(int a) {
//        System.out.println("B");
//    }
//    public void fn() {
//        System.out.println("C");
//    }
//}
//class Child extends Parent {
//    public Child() {
//        System.out.println("D");
//    }
//    public Child(int a) {
//        super(a);
//        // 부모 클래스의 특정 생성자 Parent(int a)를 호출하기 위함.
//        // 없으면 매개변수가 없는 생성자 Parent()가 호출됨
//        System.out.println("E");
//    }
//    public void fn() {
//        System.out.println("F");
//    }
//}
//public class Study {
//    public static void main(String[] args) {
//        Parent a = new Parent(); // A
//        Parent b = new Parent(1); // B
//        Parent c = new Child(); // A D
//        Parent d = new Child(1); // B E
//        Child e = new Child(); // A D
//        Child f = new Child(2); // B E
//        a.fn(); // C
//        e.fn(); // F
//    }
//}

// 부모 클래스 접근
// 자바는 super 키워드를 이용하여 상위 클래스의 변수나 메서드에 접근할 수 있다.
// 부모 클래스 내부 변수 접근 : super.변수;
// 부모 클래스 내부 메서드 접근 : super.메서드(매개변수);
// 부모 클래스 내부 생성자 호출 : super(매개변수);
//class A {
//    public void fn() {
//        System.out.println("A");
//    }
//}
//class B extends A {
//    public void fn() {
//        super.fn();
//        System.out.println("B");
//    }
//}
//public class Study {
//    public static void main(String[] args) {
//        A a = new B();
//        a.fn();
//    }
//}


// 추상 클래스

// 추상 클래스는 미구현 추상 메서드를 한 개 이상 가지며,
// 자식 클래스에서 해당 추상 메서드를 반드시 구현하도록 강제하는 기능
//abstract class A {
//    abstract void fn();
//}
//class B extends A {
//    void fn() {
//        System.out.println("B");
//    }
//}
//class C extends A {
//    void fn() {
//        System.out.println("C");
//    }
//}
//public class Study {
//    public static void main(String[] args) {
//        A b = new B();
//        A c = new C();
//        b.fn();
//        c.fn();
//    }
//}


// 인터페이스
// 인터페이스는 자바의 다형성을 극대화하여 개발코드 수정을 줄이고 프로그램 유지보수성을 높이기 위한 문법
// (인터페이스는 일종의 추상 클래스)
// 오직 추상 메서드와 상수만을 멤버로 가질 수 있으며, 그 외의 다른 어떠한 요소도 허용되지 않는다.
// 인터페이스는 구현된 것은 아무것도 없고 밑그림만 그려져 있는 '기본 설계도'라고 할 수 있다.
//interface A{
//    void fn();
//}
//class B implements A {
//    public void fn() {
//        System.out.println("B");
//    }
//}
//class C implements A {
//    public void fn() {
//        System.out.println("C");
//    }
//}
//class Study {
//    public static void main(String[] args) {
//        A b = new B();
//        A c = new C();
//        b.fn();
//        c.fn();
//    }
//}