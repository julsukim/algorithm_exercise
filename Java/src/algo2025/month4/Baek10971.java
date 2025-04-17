package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek10971 {

    private static int N;
    private static int[][] cities;
    private static boolean[] visited;
    private static int minimum = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        cities = new int[N][N];
        visited = new boolean[N];

        StringTokenizer st;
        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<N; j++) {
                cities[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i=0; i<N; i++) {
            visited[i] = true;
            backtrack(i, i, 0, 0);
            visited[i] = false;
        }

        System.out.println(minimum);
    }

    private static void backtrack(int start, int now, int depth, int acc) {
        if (acc > minimum) return;

        if (depth == N - 1) {
            if (cities[now][start] > 0) {
                minimum = Math.min(minimum, acc + cities[now][start]);
            }
            return;
        }

        for (int i=0; i<N; i++) {
            if (!visited[i] && cities[now][i] > 0) {
                visited[i] = true;
                backtrack(start, i, depth + 1, acc + cities[now][i]);
                visited[i] = false;
            }
        }
    }
}
