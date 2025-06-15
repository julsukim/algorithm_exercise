package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek20125 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int hr = 0;
        int hc = 0;
        boolean findHeart = false;

        char[][] board = new char[N][N];
        for (int r = 0; r < N; r++) {
            String line = br.readLine();
            for (int c = 0; c < N; c++) {
                char ch = line.charAt(c);
                board[r][c] = ch;

                if (!findHeart && ch == '*') {
                    hr = r + 1;
                    hc = c;
                    findHeart = true;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(hr + 1).append(" ").append(hc + 1).append("\n");

        int la = -1;
        int ra = -1;
        for (int c = 0; c < N; c++) {
            if (la == -1 && board[hr][c] == '*') la = c;
            else if (board[hr][c] == '*') ra = c;
        }
        sb.append(hc - la).append(" ").append(ra - hc).append(" ");

        int mid = N-1;
        for (int r = hr; r < N; r++) {
            if (board[r][hc] != '*') break;
            mid = r;
        }
        sb.append(mid - hr).append(" ");

        int ll = N - 1;
        int rl = N - 1;
        for (int r = mid+1; r < N; r++) {
            if (board[r][hc-1] == '*') ll = r;
            if (board[r][hc+1] == '*') rl = r;
        }
        sb.append(ll - mid).append(" ").append(rl - mid);

        System.out.println(sb.toString());
    }
}
