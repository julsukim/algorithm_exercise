package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek10709 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int H = Integer.parseInt(st.nextToken());
        int W = Integer.parseInt(st.nextToken());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < H; i++) {
            sb.setLength(0);
            String line = br.readLine();
            int lastCloud = -1;

            for (int j = 0; j < W; j++) {
                if (line.charAt(j) == 'c') {
                    lastCloud = j;
                    sb.append('0');
                } else {
                    sb.append(lastCloud < 0 ? "-1" : Integer.toString(j - lastCloud));
                }

                if (j < W - 1) sb.append(' ');
            }

            pw.println(sb);
        }

        pw.flush();

//        char[][] cloud = new char[H][W];
//        for (int i = 0; i < H; i++) {
//            String line = br.readLine();
//            for (int j = 0; j < W; j++) {
//                cloud[i][j] = line.charAt(j);
//            }
//        }
//
//        int[][] board = new int[H][W];
//        for (int i = 0; i < H; i++) {
//            boolean isCloudy = false;
//            int counter = 0;
//            for (int j = 0; j < W; j++) {
//                if (cloud[i][j] == 'c') {
//                    isCloudy = true;
//                    counter = 0;
//                    board[i][j] = 0;
//                } else if (cloud[i][j] == '.') {
//                    if (isCloudy) {
//                        board[i][j] = counter;
//                    } else {
//                        board[i][j] = -1;
//                    }
//                }
//                if (isCloudy) counter++;
//            }
//        }
//
//        StringBuilder sb = new StringBuilder();
//        for (int[] r : board) {
//            for (int e : r) {
//                sb.append(e).append(" ");
//            }
//            sb.append("\n");
//        }
//
//        System.out.println(sb.toString());
    }
}
