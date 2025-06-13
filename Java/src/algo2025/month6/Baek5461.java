package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek5461 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        char[][] floor = new char[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                floor[i][j] = line.charAt(j);
            }
        }

        boolean[][] visited = new boolean[N][M];
        int count = 0;
        int[][] delta = new int[][]{{0, 1}, {1, 0}};

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (visited[r][c]) continue;

                char now = floor[r][c];
                visited[r][c] = true;

                int dir;
                if (now == '-') dir = 0;
                else dir = 1;

                Queue<int[]> queue = new ArrayDeque<>();
                queue.add(new int[]{r, c});

                while (!queue.isEmpty()) {
                    int[] cur = queue.poll();

                    int nr = cur[0] + delta[dir][0];
                    int nc = cur[1] + delta[dir][1];

                    if (nr < 0 || nr >= N || nc < 0 || nc >= M) break;
                    if (floor[nr][nc] != now) break;

                    visited[nr][nc] = true;
                    queue.offer(new int[]{nr, nc});
                }

                count++;
            }
        }

        System.out.println(count);
    }
}
