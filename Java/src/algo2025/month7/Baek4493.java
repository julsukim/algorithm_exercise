package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek4493 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        while (T-- > 0) {
            int score1 = 0;
            int score2 = 0;

            int N = Integer.parseInt(br.readLine());
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                String p1 = st.nextToken();
                String p2 = st.nextToken();

                int r = play(p1, p2);
                if (r == 1) {
                    score2++;
                } else if (r == -1) {
                    score1++;
                }
            }

            if (score1 > score2) {
                sb.append("Player 1\n");
            } else if (score1 < score2) {
                sb.append("Player 2\n");
            } else {
                sb.append("TIE\n");
            }
        }

        System.out.println(sb);
    }

    static int play(String p1, String p2) {
        if (p1.equals("R")) {
            if (p2.equals("P")) {
                return 1;
            } else if (p2.equals("S")) {
                return -1;
            } else {
                return 0;
            }
        } else if (p1.equals("P")) {
            if (p2.equals("R")) {
                return -1;
            } else if (p2.equals("S")) {
                return 1;
            } else {
                return 0;
            }
        } else {
            if (p2.equals("R")) {
                return 1;
            } else if (p2.equals("P")) {
                return -1;
            } else {
                return 0;
            }
        }
    }
}
