package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek27172 {
    static final int MAX = 1_000_001;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] cards = new int[N];
        int[] count = new int[MAX]; // 숫자 출현 여부 체크

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
            count[cards[i]] = 1;
        }

        int[] result = new int[MAX]; // 점수 저장

        for (int i = 1; i < MAX; i++) {
            if (count[i] == 1) {
                // i의 배수를 찾아서 i가 나눌 수 있는 수를 찾음
                for (int j = i * 2; j < MAX; j += i) {
                    if (count[j] == 1) {
                        result[i]++;
                        result[j]--;
                    }
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int x : cards) {
            sb.append(result[x]).append(' ');
        }
        System.out.println(sb);
    }
}
