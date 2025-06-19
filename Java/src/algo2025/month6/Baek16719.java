package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek16719 {

    private static String str;
    private static boolean[] visited;
    private static int N;
    private static StringBuilder result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = br.readLine();
        N = str.length();
        visited = new boolean[N];
        result = new StringBuilder();
        backtrack(0, N);

        System.out.println(result);
    }

    private static void backtrack(int start, int end) {
        if (start >= end) return;

        char best = '~';
        int idx = -1;
        for (int i = start; i < end; i++) {
            if (str.charAt(i) < best) {
                best = str.charAt(i);
                idx = i;
            }
        }

        visited[idx] = true;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            if (visited[i]) sb.append(str.charAt(i));
        }
        result.append(sb.toString()).append("\n");

        backtrack(idx + 1, end);
        backtrack(start, idx);
    }
}
