package algo2025.month10;

import java.io.*;
import java.util.*;

public class Baek1952 {

    private static final int[][] delta = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    private static int counter = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        boolean[][] visited = new boolean[N][M];
        int r = 0, c = 0, dir = 0;
        visited[r][c] = true;

        for (int i = 1; i < N * M; i++) {
            int nr = r + delta[dir][0];
            int nc = c + delta[dir][1];

            if (nr < 0 || nc < 0 || nr >= N || nc >= M || visited[nr][nc]) {
                dir = (dir + 1) % 4;
                counter++;
                nr = r + delta[dir][0];
                nc = c + delta[dir][1];
            }

            visited[nr][nc] = true;
            r = nr;
            c = nc;
        }

        System.out.println(counter);
    }
}
