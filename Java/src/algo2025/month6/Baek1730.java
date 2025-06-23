package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek1730 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String orders = br.readLine();

        char[][] board = new char[N][N];
        for (int i = 0; i < N; i++) {
            Arrays.fill(board[i], '.');
        }

        int[][] delta = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        Map<Character, Integer> orderMap = new HashMap<>();
        orderMap.put('U', 0);
        orderMap.put('D', 1);
        orderMap.put('L', 2);
        orderMap.put('R', 3);

        int r = 0, c = 0;
        for (int i = 0; i < orders.length(); i++) {
            char order = orders.charAt(i);

            int nr = r + delta[orderMap.get(order)][0];
            int nc = c + delta[orderMap.get(order)][1];

            if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;

            if (order == 'D' || order == 'U') {
                if (board[r][c] == '.') {
                    board[r][c] = '|';
                } else if (board[r][c] == '-') {
                    board[r][c] = '+';
                }
                if (board[nr][nc] == '.') {
                    board[nr][nc] = '|';
                } else if (board[nr][nc] == '-') {
                    board[nr][nc] = '+';
                }
            } else {
                if (board[r][c] == '.') {
                    board[r][c] = '-';
                } else if (board[r][c] == '|') {
                    board[r][c] = '+';
                }
                if (board[nr][nc] == '.') {
                    board[nr][nc] = '-';
                } else if (board[nr][nc] == '|') {
                    board[nr][nc] = '+';
                }
            }

            r = nr;
            c = nc;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(board[i][j]);
            }
            if (i < N - 1) sb.append("\n");
        }

        System.out.println(sb);
    }
}
