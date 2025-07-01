package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek24523 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] ans = new int[N];
        Arrays.fill(ans, -1);

        for (int i = N - 2; i >= 0; i--) {
            if (arr[i] != arr[i + 1]) {
                ans[i] = i + 2;
            } else {
                ans[i] = ans[i + 1];
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int e : ans) {
            sb.append(e).append(" ");
        }

        System.out.println(sb);
    }
}
