package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek2239 {
    static final int N = 9;
    static int[][] board = new int[N][N];
    static List<int[]> blanks = new ArrayList<>();
    static boolean solved = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for (int r = 0; r < N; r++) {
            String line = br.readLine();
            for (int c = 0; c < N; c++) {
                board[r][c] = line.charAt(c) - '0';
                if (board[r][c] == 0) {
                    blanks.add(new int[]{r, c});
                }
            }
        }

        dfs(0);
    }

    static void dfs(int idx) {
        if (idx == blanks.size()) {
            printBoard();
            solved = true;
            return;
        }

        int[] pos = blanks.get(idx);
        int r = pos[0], c = pos[1];

        for (int num = 1; num <= 9; num++) {
            if (isValid(r, c, num)) {
                board[r][c] = num;
                dfs(idx + 1);
                if (solved) return;
                board[r][c] = 0;
            }
        }
    }

    static boolean isValid(int row, int col, int num) {
        for (int i = 0; i < N; i++) {
            if (board[row][i] == num || board[i][col] == num) return false;
        }

        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[startRow + i][startCol + j] == num) {
                    return false;
                }
            }
        }

        return true;
    }

    static void printBoard() {
        StringBuilder sb = new StringBuilder();
        for (int[] row : board) {
            for (int num : row) {
                sb.append(num);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
