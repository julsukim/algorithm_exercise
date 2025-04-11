package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek2072 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st;
        int turn = -1;

        Omok omok = new Omok();

        for (int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int type = (i % 2 == 0) ? 1 : 2;
            omok.put(type, r, c);
            if (turn == -1 && omok.checkStatus()) turn = i + 1;
        }

        System.out.println(turn);
    }

    private static class Omok {
        private final int size = 20;
        private int[][] board = new int[size][size];

        public void put(int type, int r, int c) {
            this.board[r][c] = type;
        }

        public boolean checkStatus() {
            int[] dr = {0, 1, 1, -1}; // → ↓ ↘ ↙
            int[] dc = {1, 0, 1, 1};

            for (int r = 1; r < size; r++) {
                for (int c = 1; c < size; c++) {
                    int type = board[r][c];
                    if (type == 0) continue;

                    for (int d = 0; d < 4; d++) {
                        int cnt = 1;

                        // 5개 확인
                        for (int k = 1; k < 5; k++) {
                            int nr = r + dr[d] * k;
                            int nc = c + dc[d] * k;

                            if (nr < 1 || nc < 1 || nr >= size || nc >= size) break;
                            if (board[nr][nc] != type) break;

                            cnt++;
                        }

                        // 정확히 5개일 때만 승리 인정
                        if (cnt == 5) {
                            int beforeR = r - dr[d];
                            int beforeC = c - dc[d];
                            int afterR = r + dr[d] * 5;
                            int afterC = c + dc[d] * 5;

                            boolean beforeValid = beforeR >= 1 && beforeC >= 1 && beforeR < size && beforeC < size;
                            boolean afterValid = afterR >= 1 && afterC >= 1 && afterR < size && afterC < size;

                            boolean beforeSame = beforeValid && board[beforeR][beforeC] == type;
                            boolean afterSame = afterValid && board[afterR][afterC] == type;

                            if (!beforeSame && !afterSame) return true;
                        }
                    }
                }
            }

            return false;
        }
    }
}
