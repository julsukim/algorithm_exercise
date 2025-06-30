package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek17829 {

    private static int N;
    private static int[][] matrix;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        matrix = new int[N][N];

        StringTokenizer st;
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                matrix[r][c] = Integer.parseInt(st.nextToken());
            }
        }

        backtrack(N, matrix);
    }

    private static void backtrack(int n, int[][] board) {
        if (n == 2) {
            int[] arr = new int[4];
            int idx = 0;
            arr[idx++] = board[0][0];
            arr[idx++] = board[0][1];
            arr[idx++] = board[1][0];
            arr[idx] = board[1][1];
            Arrays.sort(arr);
            System.out.println(arr[2]);
            return;
        }

        int ri = 0;
        int ci = 0;
        int[][] newBoard = new int[n/2][n/2];

        for (int r = 0; r < n; r += 2) {
            for (int c = 0; c < n; c += 2) {
                int[] arr = new int[4];
                int idx = 0;
                arr[idx++] = board[r][c];
                arr[idx++] = board[r][c+1];
                arr[idx++] = board[r+1][c];
                arr[idx] = board[r+1][c+1];
                Arrays.sort(arr);
                newBoard[ri][ci] = arr[2];
                ci++;
            }
            ri++;
            ci = 0;
        }

        backtrack(n/2, newBoard);
    }
}
