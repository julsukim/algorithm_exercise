package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek16173 {

    private static final int[][] delta = new int[][]{{1, 0}, {0, 1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int N = Integer.parseInt(br.readLine());
        int[][] map = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[N][N];

        queue.offer(new int[]{0, 0});
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];

            if (r == N-1 && c == N-1) break;

            for (int[] d : delta) {
                int nr = r + (d[0] * map[r][c]);
                int nc = c + (d[1] * map[r][c]);

                if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                if (visited[nr][nc]) continue;

                visited[nr][nc] = true;
                queue.offer(new int[]{nr, nc});
            }
        }

        System.out.println(visited[N-1][N-1] ? "HaruHaru" : "Hing");
    }
}
