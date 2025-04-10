package algo2025.month4;

import java.util.*;

public class SudokuSumConstraint {

    static class Position {
        int row, col;
        Position(int row, int col) {
            this.row = row;
            this.col = col;
        }
    }

    static class SumGroup {
        List<Position> cells;
        int targetSum;

        SumGroup(List<Position> cells, int targetSum) {
            this.cells = cells;
            this.targetSum = targetSum;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] board = new int[9][9];
        List<SumGroup> sumGroups = new ArrayList<>();

        System.out.println("sumGroup 조건을 한 줄에 입력하세요 (빈 줄 입력 시 종료):");
        while (sc.hasNextLine()) {
            String line = sc.nextLine().trim();
            if (line.isEmpty()) break;

            String[] tokens = line.split(" ");
            int len = tokens.length;

            List<Position> cells = new ArrayList<>();
            for (int i = 0; i < len - 1; i += 2) {
                int row = Integer.parseInt(tokens[i]);
                int col = Integer.parseInt(tokens[i + 1]);
                cells.add(new Position(row, col));
            }
            int targetSum = Integer.parseInt(tokens[len - 1]);
            sumGroups.add(new SumGroup(cells, targetSum));
        }

        if (solve(board, sumGroups)) {
            System.out.println("✔ 퍼즐 해결 완료:");
            printBoard(board);
        } else {
            System.out.println("❌ 해결할 수 없습니다.");
        }
    }

    static boolean solve(int[][] board, List<SumGroup> sumGroups) {
        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                if (board[row][col] == 0) {
                    for (int num = 1; num <= 9; num++) {
                        if (isValid(board, row, col, num)) {
                            board[row][col] = num;
                            if (checkAllSumGroups(board, sumGroups)) {
                                if (solve(board, sumGroups)) return true;
                            }
                            board[row][col] = 0;
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    static boolean isValid(int[][] board, int row, int col, int num) {
        for (int i = 0; i < 9; i++) {
            if (board[row][i] == num || board[i][col] == num)
                return false;
        }
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

    static boolean checkAllSumGroups(int[][] board, List<SumGroup> sumGroups) {
        for (SumGroup group : sumGroups) {
            int sum = 0;
            int filled = 0;
            for (Position p : group.cells) {
                int val = board[p.row][p.col];
                if (val == 0) continue;
                sum += val;
                filled++;
            }
            if (filled == group.cells.size()) {
                if (sum != group.targetSum) return false;
            } else if (sum >= group.targetSum) {
                return false;
            }
        }
        return true;
    }

    static void printBoard(int[][] board) {
        for (int[] row : board) {
            for (int num : row)
                System.out.print(num + " ");
            System.out.println();
        }
    }
}
