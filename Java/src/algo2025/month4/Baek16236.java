package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek16236 {
    static int N;
    static int[][] field;
    static int[] cur;
    static int sharkSize = 2;
    static int eatCount = 0;
    static final int[][] delta = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        field = new int[N][N];
        cur = new int[2];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int val = Integer.parseInt(st.nextToken());
                if (val == 9) {
                    cur[0] = i;
                    cur[1] = j;
                    field[i][j] = 0;
                    continue;
                }
                field[i][j] = val;
            }
        }

        System.out.println(simulate());
    }

    static int simulate() {
        int time = 0;

        while (true) {
            int passedTime = seek();
            if (passedTime == 0) {
                break;
            }
            time += passedTime;
        }

        return time;
    }

    static int seek() {
        int[][] visited = new int[N][N];
        visited[cur[0]][cur[1]] = 1;

        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{cur[0], cur[1]});

        List<int[]> candidates = new ArrayList<>();
        int minDepth = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();

            for (int[] d : delta) {
                int nr = now[0] + d[0];
                int nc = now[1] + d[1];

                if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                if (visited[nr][nc] != 0 || field[nr][nc] > sharkSize) continue;

                int depth = visited[now[0]][now[1]] + 1;
                if (depth > minDepth) continue;

                if (field[nr][nc] != 0 && field[nr][nc] < sharkSize) {
                    minDepth = depth;
                    candidates.add(new int[]{nr, nc});
                }

                visited[nr][nc] = depth;
                queue.add(new int[]{nr, nc});
            }
        }

        if (candidates.isEmpty()) return 0;

        if (candidates.size() > 1) {
            candidates.sort((a, b) -> {
                if (a[0] == b[0]) {
                    return Integer.compare(a[1], b[1]);
                }
                return Integer.compare(a[0], b[0]);
            });
        }

        cur[0] = candidates.get(0)[0];
        cur[1] = candidates.get(0)[1];

        field[cur[0]][cur[1]] = 0;
        eat();
        return visited[cur[0]][cur[1]] - 1;
    }

    static void eat() {
        eatCount++;
        if (eatCount >= sharkSize) {
            eatCount = 0;
            sharkSize++;
        }
    }
}
