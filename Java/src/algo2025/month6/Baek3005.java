package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek3005 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        char[][] puzzle = new char[R][C];
        for (int r = 0; r < R; r++) {
            String line = br.readLine();
            for (int c = 0; c < C; c++) {
                puzzle[r][c] = line.charAt(c);
            }
        }

        List<String> answers = new ArrayList<>();

        StringBuilder sb = new StringBuilder();

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                char l = puzzle[r][c];

                if (l != '#') {
                    sb.append(l);
                } else {
                    if (sb.length() > 1) {
                        answers.add(sb.toString());
                    }
                    sb.setLength(0);
                }
            }

            if (sb.length() > 1) {
                answers.add(sb.toString());
            }
            sb.setLength(0);
        }

        for (int c = 0; c < C; c++) {
            for (int r = 0; r < R; r++) {
                char l = puzzle[r][c];

                if (l != '#') {
                    sb.append(l);
                } else {
                    if (sb.length() > 1) {
                        answers.add(sb.toString());
                    }
                    sb.setLength(0);
                }
            }

            if (sb.length() > 1) {
                answers.add(sb.toString());
            }
            sb.setLength(0);
        }

        System.out.println(Collections.min(answers));
    }
}
