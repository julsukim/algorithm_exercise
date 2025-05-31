package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek16931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] grid = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                grid[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.out.println(getSurfaceArea(grid, N, M));
    }

    private static int getSurfaceArea(int[][] grid, int N, int M) {
        int area = 0;

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] > 0) {
                    area += 2;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int h = grid[i][j];

                if (i == 0) area += h;
                else area += Math.max(h - grid[i - 1][j], 0);

                if (i == N - 1) area += h;
                else area += Math.max(h - grid[i + 1][j], 0);

                if (j == 0) area += h;
                else area += Math.max(h - grid[i][j - 1], 0);

                if (j == M - 1) area += h;
                else area += Math.max(h - grid[i][j + 1], 0);
            }
        }

        return area;
    }
}
