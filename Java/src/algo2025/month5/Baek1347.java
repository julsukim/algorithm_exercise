package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek1347 {

    private static final int[][] delta = new int[][]{{1, 0}, {0, -1}, {-1, 0}, {0, 1}}; // + pos - neg

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Set<int[]> logs = new HashSet<>();
        logs.add(new int[]{0, 0});
        int dir = 0;
        int r = 0;
        int c = 0;

        int minCol = 0, minRow = 0, maxCol = 0, maxRow = 0;

        String moves = br.readLine();
        for (int i = 0; i < N; i++) {
            char move = moves.charAt(i);
            if (move == 'L') {
                dir = (dir - 1 + 4) % 4;
            } else if (move == 'R') {
                dir = (dir + 1 + 4) % 4;
            } else {
                r += delta[dir][0];
                c += delta[dir][1];

                minRow = Math.min(minRow, r);
                maxRow = Math.max(maxRow, r);
                minCol = Math.min(minCol, c);
                maxCol = Math.max(maxCol, c);

                logs.add(new int[]{r, c});
            }
        }

        int rDiff = minRow < 0 ? -minRow : 0;
        int cDiff = minCol < 0 ? -minCol : 0;

        minRow += rDiff;
        maxRow += rDiff;
        minCol += cDiff;
        maxCol += cDiff;

        boolean[][] map = new boolean[maxRow + 1][maxCol + 1];

        for (int[] m : logs) {
            map[m[0] + rDiff][m[1] + cDiff] = true;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i <= maxRow; i++) {
            for (int j = 0; j <= maxCol; j++) {
                sb.append(map[i][j] ? '.' : '#');
            }
            sb.append("\n");
        }

        System.out.println(sb.toString());
    }
}
