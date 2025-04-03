package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1303 {

    private static final int WHITE = 0;
    private static final int BLUE = 1;
    private static final int VISITED = -1;

    private static final int[] dr = {-1, 1, 0, 0};
    private static final int[] dc = {0, 0, -1, 1};

    static int N;
    static int M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        int[][] board = new int[N][M];

        for (int i=0; i<N; i++) {
            String line = br.readLine();
            for (int j=0; j<M; j++) {
                board[i][j] = line.charAt(j) == 'W' ? WHITE : BLUE;
            }
        }

        int wPower = 0;
        int bPower = 0;

        for (int i=0; i<N; i++) {
            for (int j=0; j<M; j++) {
                if (board[i][j] == VISITED) continue;

                int color = board[i][j];
                int group = bfs(board, i, j, color);

                int power = group*group;

                if (color == WHITE) {
                    wPower += power;
                } else {
                    bPower += power;
                }
            }
        }

        System.out.println(wPower + " " + bPower);
    }

    private static int bfs(int[][] board, int startRow, int startCol, int color) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{startRow, startCol});
        board[startRow][startCol] = -1;
        int count = 0;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int r = curr[0];
            int c = curr[1];

            count++;

            for (int delta=0; delta<4; delta++) {
                int nr = r + dr[delta];
                int nc = c + dc[delta];

                if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                if (board[nr][nc] != color) continue;

                board[nr][nc] = -1;
                queue.offer(new int[]{nr, nc});
            }
        }

        return count;
    }
}
