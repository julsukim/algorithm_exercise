package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek1652 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        boolean[][] board = new boolean[N][N];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                board[i][j] = line.charAt(j) == '.';
            }
        }
        int rCnt = 0;
        int cCnt = 0;
        for (int i = 0; i < N; i++) {
            int cnt = 0;
            for (int j = 0; j < N; j++) {
                if (board[i][j]) {
                    cnt++;
                } else {
                    if (cnt >= 2) {
                        rCnt++;
                    }
                    cnt = 0;
                }
            }
            if (cnt >= 2) {
                rCnt++;
            }
        }

        for (int j = 0; j < N; j++) {
            int cnt = 0;
            for (int i = 0; i < N; i++) {
                if (board[i][j]) {
                    cnt++;
                } else {
                    if (cnt >= 2) {
                        cCnt++;
                    }
                    cnt = 0;
                }
            }
            if (cnt >= 2) {
                cCnt++;
            }
        }

        System.out.println(rCnt + " " + cCnt);
    }
}
