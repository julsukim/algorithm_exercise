package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek17281 {

    private static int N;
    private static int[] order;
    private static boolean[] used;
    private static int[][] result;
    private static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        N = Integer.parseInt(br.readLine());

        result = new int[N][10];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= 9; j++) {
                result[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        order = new int[9];
        used = new boolean[10];

        order[3] = 1;
        used[1] = true;

        dfs(0);

        System.out.println(answer);
    }

    private static void dfs(int idx) {
        if (idx == 9) {
            simulate();
            return;
        }
        if (idx == 3) {
            dfs(idx + 1);
            return;
        }
        for (int p = 2; p <= 9; p++) {
            if (used[p]) continue;

            used[p] = true;
            order[idx] = p;
            dfs(idx + 1);
            used[p] = false;
        }
    }

    private static void simulate() {
        int score = 0, cur = 0;
        boolean[] bases = new boolean[3];
        for (int inning = 0; inning < N; inning++) {
            Arrays.fill(bases, false);
            int outs = 0;
            while (outs < 3) {
                int batter = order[cur];
                cur = (cur + 1) % 9;
                int h = result[inning][batter];
                if (h == 0) {
                    outs++;
                } else {
                    for (int i = 2; i >= 0; i--) {
                        if (bases[i]) {
                            int dest = i + h;
                            if (dest >= 3) score++;
                            else bases[dest] = true;
                            bases[i] = false;
                        }
                    }

                    if (h >= 4) {
                        score++;
                    } else {
                        bases[h - 1] = true;
                    }
                }
            }
        }
        answer = Math.max(answer, score);
    }
}
