package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek2290 {

    // index: 0=a, 1=b, 2=c, 3=d, 4=e, 5=f, 6=g
    static final boolean[][] SEG = {
            {true,  true,  true,  true,  true,  true,  false}, // 0
            {false, true,  true,  false, false, false, false}, // 1
            {true,  true,  false, true,  true,  false, true }, // 2
            {true,  true,  true,  true,  false, false, true }, // 3
            {false, true,  true,  false, false, true,  true }, // 4
            {true,  false, true,  true,  false, true,  true }, // 5
            {true,  false, true,  true,  true,  true,  true }, // 6
            {true,  true,  true,  false, false, false, false}, // 7
            {true,  true,  true,  true,  true,  true,  true }, // 8
            {true,  true,  true,  true,  false, true,  true }  // 9
    };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        String num = st.nextToken();
        int rows = 2 * s + 3;

        StringBuilder sb = new StringBuilder();
        for (int r = 0; r < rows; r++) {
            for (int i = 0; i < num.length(); i++) {
                if (i > 0) sb.append(' ');
                int d = num.charAt(i) - '0';
                boolean[] on = SEG[d];
                boolean a = on[0], b = on[1], c = on[2],
                        dgt = on[3], e = on[4], f = on[5], g = on[6];

                if (r == 0) {
                    // ─ a (맨 윗가로)
                    if (a) sb.append(' ').append("-".repeat(s)).append(' ');
                    else   sb.append(" ".repeat(s+2));

                } else if (r <= s) {
                    // │ f (왼쪽 위)    │ b (오른쪽 위)
                    sb.append(f ? '|' : ' ')
                            .append(" ".repeat(s))
                            .append(b ? '|' : ' ');

                } else if (r == s + 1) {
                    // ─ g (가운데 가로)
                    if (g) sb.append(' ').append("-".repeat(s)).append(' ');
                    else   sb.append(" ".repeat(s+2));

                } else if (r <= 2*s + 1) {
                    // │ e (왼쪽 아래)  │ c (오른쪽 아래)
                    sb.append(e ? '|' : ' ')
                            .append(" ".repeat(s))
                            .append(c ? '|' : ' ');

                } else {
                    // ─ d (맨 아래 가로)
                    if (dgt) sb.append(' ').append("-".repeat(s)).append(' ');
                    else     sb.append(" ".repeat(s+2));
                }
            }
            sb.append('\n');
        }

        System.out.println(sb);
    }
}
