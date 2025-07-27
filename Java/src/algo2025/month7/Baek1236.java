package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek1236 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        boolean[][] castle = new boolean[N][M];
        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < M; j++) {
                char c = line.charAt(j);
                if (c == '.') {
                    castle[i][j] = false;
                } else {
                    castle[i][j] = true;
                }
            }
        }

        int emptyRow = 0;
        for (int i = 0; i < N; i++) {
            boolean isEmpty = true;
            for (int j = 0; j < M; j++) {
                if (castle[i][j]) isEmpty = false;
            }
            if (isEmpty) emptyRow++;
        }

        int emptyCol = 0;
        for (int i = 0; i < M; i++) {
            boolean isEmpty = true;
            for (int j = 0; j < N; j++) {
                if (castle[j][i]) isEmpty = false;
            }
            if (isEmpty) emptyCol++;
        }

//        System.out.println(emptyRow + " : " + emptyCol);
        System.out.println(Math.max(emptyCol, emptyRow));
    }
}
