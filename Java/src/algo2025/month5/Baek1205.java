package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek1205 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());       // 현재 랭킹에 올라있는 점수 개수
        int score = Integer.parseInt(st.nextToken());   // 태수의 새 점수
        int P = Integer.parseInt(st.nextToken());       // 랭킹에 올라갈 수 있는 최대 점수 개수

        int[] arr = new int[N];
        if (N > 0) {
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }
        }

        // 1) 리스트가 가득 찼고, 새 점수가 꼴등 이하라면 등재 불가
        if (N == P && N > 0 && score <= arr[N - 1]) {
            System.out.println(-1);
            return;
        }

        // 2) 등수 계산: 기존 점수 중 나보다 큰(score < arr[i]) 점수 개수만큼 밀린다
        int rank = 1;
        for (int i = 0; i < N; i++) {
            if (arr[i] > score) rank++;
            else break;
        }

        System.out.println(rank);
    }
}
