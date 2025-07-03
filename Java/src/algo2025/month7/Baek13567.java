package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek13567 {

    private static final int[][] delta = new int[][]{{0, 1}, {-1, 0}, {0, -1}, {1, 0}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int cx = 0;
        int cy = 0;
        int dir = 0;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String q = st.nextToken();
            int num = Integer.parseInt(st.nextToken());

            if (q.equals("MOVE")) {
                cx = cx + delta[dir][1] * num;
                cy = cy + delta[dir][0] * num;

                if (cx < 0 || cx > M || cy < 0 || cy > M) {
                    System.out.println(-1);
                    return;
                }
            } else if (q.equals("TURN")) {
                if (num == 0) dir = (dir + 3) % 4;
                else dir = (dir + 1) % 4;
            }
        }

        System.out.println(cx + " " + cy);
    }
}
