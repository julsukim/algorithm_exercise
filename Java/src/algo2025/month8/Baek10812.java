package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek10812 {
    static final int MAX_N = 100;
    static int[] a = new int[MAX_N + 1];
    static int[] buf = new int[MAX_N + 1];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= N; i++) a[i] = i;

        for (int t = 0; t < M; t++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            rotate(i, j, k);
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            if (i > 1) sb.append(' ');
            sb.append(a[i]);
        }
        System.out.println(sb);
    }

    static void rotate(int i, int j, int k) {
        int idx = 0;

        for (int p = k; p <= j; p++) buf[++idx] = a[p];

        for (int p = i; p < k; p++) buf[++idx] = a[p];

        idx = 1;
        for (int p = i; p <= j; p++) a[p] = buf[idx++];
    }
}
