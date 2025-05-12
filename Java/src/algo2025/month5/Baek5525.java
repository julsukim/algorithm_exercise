package algo2025.month5;

import java.io.*;

public class Baek5525 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine()); // PN에서 N값
        int M = Integer.parseInt(br.readLine()); // 문자열 길이
        String S = br.readLine();                // 문자열 S

        int count = 0;   // 정답
        int pattern = 0; // 현재 IOI 패턴 개수
        int i = 1;       // 중앙 문자 'O'부터 검사 시작

        while (i < M - 1) {
            // IOI 패턴 발견
            if (S.charAt(i - 1) == 'I' && S.charAt(i) == 'O' && S.charAt(i + 1) == 'I') {
                pattern++;      // 연속된 IOI 패턴 개수 증가
                i += 2;         // 다음 'O'를 기준으로 검사
                if (pattern == N) {
                    count++;    // N개의 IOI → P_N 완성
                    pattern--;  // 중첩된 PN을 위해 IOI 한 개 유지
                }
            } else {
                i++;            // 조건 안 맞으면 다음 문자로
                pattern = 0;    // 연속 패턴 리셋
            }
        }

        System.out.println(count);
    }

//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int N = Integer.parseInt(br.readLine());
//        int M = Integer.parseInt(br.readLine());
//
//        String S = br.readLine();
//
//        StringBuilder sb = new StringBuilder();
//        for (int i = 0; i < N; i++) {
//            sb.append("IO");
//        }
//        sb.append("I");
//        String P = sb.toString();
//        int pl = 2 * N;
//        int count = 0;
//        for (int i = 0; i < M - pl; i++) {
//            String sub = S.substring(i, i + pl + 1);
//            if (sub.equals(P)) count++;
//        }
//
//        System.out.println(count);
//    }
}
