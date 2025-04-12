package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek2615 {

    private static class Omok {

        private static final int size = 19;
        private int[][] board = new int[size][size];
        private StringTokenizer input;
        private int winner = 0;
        private int wr;
        private int wc;


        public void put(int row, String line) {
            input = new StringTokenizer(line);
            for (int c=0; c<size; c++) {
                board[row][c] = Integer.parseInt(input.nextToken());
            }
        }

        public void setWinner(int winner, int r, int c) {
            this.winner = winner;
            this.wr = r + 1;
            this.wc = c + 1;
        }

        public void printWinner() {
            System.out.println(winner);
            if (winner != 0) {
                System.out.println(wr + " " + wc);
            }
        }

        public void checkBoard() {
            int[] dr = {1, 0, 1, -1};
            int[] dc = {0, 1, 1, 1};

            for (int r = 0; r < size; r++) {
                for (int c = 0; c < size; c++) {
                    int type = board[r][c];
                    if (type == 0) continue;

                    for (int d = 0; d < 4; d++) {
                        int cnt = 1;

                        // 5개 확인
                        for (int k = 1; k < 5; k++) {
                            int nr = r + dr[d] * k;
                            int nc = c + dc[d] * k;

                            if (nr < 0 || nc < 0 || nr >= size || nc >= size) break;
                            if (board[nr][nc] != type) break;

                            cnt++;
                        }

                        // 정확히 5개일 때만 승리 인정
                        if (cnt == 5) {
                            int beforeR = r - dr[d];
                            int beforeC = c - dc[d];
                            int afterR = r + dr[d] * 5;
                            int afterC = c + dc[d] * 5;

                            boolean beforeValid = beforeR >= 0 && beforeC >= 0 && beforeR < size && beforeC < size;
                            boolean afterValid = afterR >= 0 && afterC >= 0 && afterR < size && afterC < size;

                            boolean beforeSame = beforeValid && board[beforeR][beforeC] == type;
                            boolean afterSame = afterValid && board[afterR][afterC] == type;

                            if (!beforeSame && !afterSame) {
                                setWinner(type, r, c);
                                return;
                            }
                        }
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Omok omok = new Omok();
        for (int r=0; r<19; r++) {
            omok.put(r, br.readLine());
        }

        omok.checkBoard();
        omok.printWinner();
    }
}
