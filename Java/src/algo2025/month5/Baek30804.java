package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek30804 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] S = new int[N];
        for (int i = 0; i < N; i++) {
            S[i] = Integer.parseInt(st.nextToken());
        }

        int[] count = new int[10];    // 과일 번호는 1~9
        int distinct = 0;             // 윈도우 내 서로 다른 과일 종류 수
        int L = 0, answer = 0;

        for (int R = 0; R < N; R++) {
            // 오른쪽 확장
            if (count[S[R]] == 0) distinct++;
            count[S[R]]++;

            // 종류가 2초과면 왼쪽에서 제거
            while (distinct > 2) {
                count[S[L]]--;
                if (count[S[L]] == 0) distinct--;
                L++;
            }

            // 최대 길이 갱신
            answer = Math.max(answer, R - L + 1);
        }

        System.out.println(answer);
    }
}

