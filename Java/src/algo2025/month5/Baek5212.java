package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek5212 {

    private static final int[][] delta = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        char[][] map = new char[R][C];
        for (int i = 0; i < R; i++) {
            String line = br.readLine();
            for (int j = 0; j < C; j++) {
                map[i][j] = line.charAt(j);
            }
        }

        List<int[]> sink = new ArrayList<>();
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (map[r][c] == '.') continue;

                int count = 0;
                for (int d = 0; d < 4; d++) {
                    int nr = r + delta[d][0];
                    int nc = c + delta[d][1];

                    if (nr < 0 || nr >= R || nc < 0 || nc >= C) {
                        count++;
                        continue;
                    }
                    if (map[nr][nc] == '.') {
                        count++;
                    }
                }

                if (count >= 3) {
                    sink.add(new int[]{r, c});
                }
            }
        }

        for (int[] s : sink) {
            map[s[0]][s[1]] = '.';
        }

        int minR = R -1, maxR = 0, minC = C - 1, maxC = 0;
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (map[r][c] == '.') continue;

                minR = Math.min(minR, r);
                maxR = Math.max(maxR, r);
                minC = Math.min(minC, c);
                maxC = Math.max(maxC, c);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int r = minR; r <= maxR; r++) {
            for (int c = minC; c <= maxC; c++) {
                sb.append(map[r][c]);
            }
            sb.append("\n");
        }

        System.out.print(sb.toString());
    }
}
