package algo2025.month4;

import java.io.IOException;

import java.io.IOException;

public class Sudoku {
    public static void main(String[] args) throws IOException {
        int[][] board = {
                {0, 9, 6, 4, 0, 2, 0, 0, 7},
                {1, 0, 0, 0, 0, 0, 0, 9, 0},
                {3, 0, 0, 0, 6, 0, 0, 0, 0},
                {0, 0, 0, 8, 0, 0, 0, 0, 3},
                {0, 2, 9, 0, 4, 0, 0, 8, 0},
                {0, 1, 0, 0, 0, 0, 0, 0, 0},
                {6, 0, 0, 0, 0, 0, 0, 0, 0},
                {0, 0, 0, 0, 0, 7, 5, 0, 0},
                {0, 8, 4, 0, 2, 0, 0, 3, 0}
        };

        if (solveSudoku(board)) {
            System.out.println("✔ 스도쿠 퍼즐 해결 완료:");
            printBoard(board);
        } else {
            System.out.println("❌ 해결할 수 없는 스도쿠입니다.");
        }
    }

    public static boolean solveSudoku(int[][] board) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == 0) {
                    for (int num = 1; num <= 9; num++) {
                        if (isValid(board, row, col, num)) {
                            board[row][col] = num;
                            if (solveSudoku(board)) return true;
                            board[row][col] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    public static boolean isValid(int[][] board, int row, int col, int num) {
        // 행, 열 확인
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == num || board[i][col] == num)
                return false;
        }

        // 3x3 박스 확인
        int startRow = (row / 3) * 3;
        int startCol = (col / 3) * 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[startRow + i][startCol + j] == num)
                    return false;
            }
        }

        return true;
    }

    public static void printBoard(int[][] board) {
        for (int[] row : board) {
            for (int num : row) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}
