package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek1629 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long c = Long.parseLong(st.nextToken());

        System.out.println(power(a, b, c));
    }

    static long power(long a, long b, long c) {
        if (b == 0) return 1; // 베이스 케이스: a^0 = 1

        long temp = power(a, b / 2, c); // 절반 지수로 줄여서 재귀 호출
        temp = (temp * temp) % c; // 절반 결과 제곱 후 모듈러 연산

        if (b % 2 == 0) return temp; // 짝수면 끝
        else return (temp * a) % c; // 홀수면 한 번 더 곱해줘야 함
    }
}
