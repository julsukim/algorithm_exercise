package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek13901 {

    private static final int[] dr = {-1, 1, 0, 0};
    private static final int[] dc = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int[][] board = new int[R][C];
        int K = Integer.parseInt(br.readLine());
        for (int i=0; i<K; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            board[r][c] = -1;
        }

        st = new StringTokenizer(br.readLine());
        int sr = Integer.parseInt(st.nextToken());
        int sc = Integer.parseInt(st.nextToken());

        int[] order = new int[4];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<4; i++) {
            order[i] = Integer.parseInt(st.nextToken());
        }

        boolean[][] visited = new boolean[R][C];
        visited[sr][sc] = true;
        int t = 0;
        int[] now = {sr, sc};
        int dirCount = 0;

        while (true) {
            if (dirCount >= 4) break;

            int nr = now[0] + dr[order[t%4] - 1];
            int nc = now[1] + dc[order[t%4] - 1];

            if (nr < 0 || nr >= R || nc < 0 || nc >= C) {
                dirCount++;
                t++;
                continue;
            }

            if (board[nr][nc] == -1 || visited[nr][nc]) {
                dirCount++;
                t++;
                continue;
            }

            dirCount = 0;
            visited[nr][nc] = true;

            now[0] = nr;
            now[1] = nc;
        }

        System.out.println(now[0] + " " + now[1]);
    }
}
