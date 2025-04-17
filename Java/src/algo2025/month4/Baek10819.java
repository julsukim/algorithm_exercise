package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek10819 {

    private static int N;
    private static int[] arr;
    private static boolean[] visited;
    private static int[] selected;
    private static int maximum = Integer.MIN_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        arr = new int[N];
        selected = new int[N];
        visited = new boolean[N];

        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        backtrack(0);
        System.out.println(maximum);
    }

    private static void backtrack(int depth) {
        if (depth == N) {
            int sum = 0;
            for (int i=0; i < N - 1; i++) {
                sum += Math.abs(selected[i] - selected[i + 1]);
            }
            maximum = Math.max(maximum, sum);
            return;
        }

        for (int i=0; i<N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                selected[depth] = arr[i];
                backtrack(depth + 1);
                visited[i] = false;
            }
        }
    }
}
