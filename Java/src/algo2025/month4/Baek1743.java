package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1743 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[][] board = new int[N+1][M+1]; // 1: 있음 0: 없음 -1: 방문 완료

        int k = K;
        while (k-- > 0) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            board[r][c] = 1;
        }

        int[] di = {-1, 1, 0, 0};
        int[] dj = {0, 0, -1, 1};

        int maxSize = 0;
        for (int i=1; i<=N; i++) {
            for (int j=1; j<=M; j++) {
                if (board[i][j] != 1) continue;

                Queue<int[]> queue = new ArrayDeque<>();
                queue.offer(new int[]{i, j});
                board[i][j] = -1;
                int size = 0;

                while (!queue.isEmpty()) {
                    int[] curr = queue.poll();
                    int r = curr[0];
                    int c = curr[1];

                    size++;

                    for (int delta=0; delta<4; delta++) {
                        int nr = r + di[delta];
                        int nc = c + dj[delta];

                        if (nr < 1 || nr > N || nc < 1 || nc > M) continue;
                        if (board[nr][nc] != 1) continue;

                        board[nr][nc] = -1;
                        queue.offer(new int[]{nr, nc});
                    }
                }

                maxSize = Math.max(maxSize, size);
            }
        }

        System.out.println(maxSize);
    }
}
