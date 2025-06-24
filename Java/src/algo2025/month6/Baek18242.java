package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek18242 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        boolean[][] board = new boolean[N][M];
        for (int r = 0; r < N; r++) {
            String line = br.readLine();
            for (int c = 0; c < M; c++) {
                if (line.charAt(c) == '#') board[r][c] = true;
            }
        }

        int minR = -1, minC = -1, maxR = -1, maxC = -1;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < M; c++) {
                if (board[r][c]) {
                    if (minR == -1) minR = r;
                    else maxR = r;

                    if (minC == -1) minC = c;
                    else maxC = c;
                }
            }
        }

//        for (int c = minC; c <= maxC; c++) {
//            if (!board[minR][c]) {
//                System.out.println("UP");
//                return;
//            }
//            if (!board[maxR][c]) {
//                System.out.println("DOWN");
//                return;
//            }
//        }
//        for (int r = minR; r <= maxR; r++) {
//            if (!board[r][minC]) {
//                System.out.println("LEFT");
//                return;
//            }
//            if (!board[r][maxC]) {
//                System.out.println("RIGHT");
//                return;
//            }
//        }

        int midR = (minR + maxR) / 2;
        int midC = (minC + maxC) / 2;

        if (!board[minR][midC])      System.out.println("UP");
        else if (!board[maxR][midC]) System.out.println("DOWN");
        else if (!board[midR][minC]) System.out.println("LEFT");
        else if (!board[midR][maxC]) System.out.println("RIGHT");
    }
}
