package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek1421 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        int[] trees = new int[N];
        int maxLen = 0;
        for (int i = 0; i < N; i++) {
            int len = Integer.parseInt(br.readLine());
            trees[i] = len;
            maxLen = Math.max(maxLen, len);
        }

        long answer = 0;
        for (int l = 1; l <= maxLen; l++) {
            long profit = 0;
            for (int len : trees) {
                int cuts = 0;

                int c = len / l;
                if (c == 0) continue;
                cuts += (len % l == 0 ? c - 1 : c);

                long p = (long) c * l * W - (long) cuts * C;
                if (p > 0) profit += p;
            }
            answer = Math.max(answer, profit);
        }

        System.out.println(answer);
    }
}
