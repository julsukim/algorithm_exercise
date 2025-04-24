package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1987 {

    private static int R, C, answer = 0;
    private static char[][] board;
    private static final int[][] d = {{-1,0},{1,0},{0,-1},{0,1}};

    private static void dfs(int r, int c, int mask, int depth) {
        answer = Math.max(answer, depth);

        for (int[] dir : d) {
            int nr = r + dir[0];
            int nc = c + dir[1];
            if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;

            int ch = board[nr][nc] - 'A';
            if ((mask & (1 << ch)) == 0) {
                dfs(nr, nc, mask | (1 << ch), depth + 1);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        board = new char[R][C];
        for (int i = 0; i < R; i++) board[i] = br.readLine().toCharArray();

        int startMask = 1 << (board[0][0] - 'A');
        dfs(0, 0, startMask, 1);
        System.out.println(answer);
    }
}
