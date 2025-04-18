package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek2573 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Iceberg iceberg = new Iceberg();
        iceberg.initVar(br.readLine());

        for (int row=0; row<iceberg.N; row++) {
            iceberg.setFieldByRow(row, br.readLine());
        }

        System.out.println(iceberg.simulate());
    }

    private static class Iceberg {
        int N, M;
        int[][] field;
        boolean[][] visited;
        static final int[][] dir = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        enum Status {EMPTY, ONE, SEPARATED};

        public void initVar(String line) {
            StringTokenizer st = new StringTokenizer(line);
            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());
            field = new int[N][M];
            visited = new boolean[N][M];
        }

        public void setFieldByRow(int row, String line) {
            StringTokenizer st = new StringTokenizer(line);
            for (int col=0; col<M; col++) {
                field[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        public int simulate() {
            int time = 0;

            while (true) {
                Status status = getStatus();

                if (status == Status.SEPARATED) break;
                else if (status == Status.EMPTY) {
                    time = 0;
                    break;
                }
                melt();
                time++;
            }

            return time;
        }

        private void resetVisited() {
            for (int row=0; row<N; row++) {
                Arrays.fill(visited[row], false);
            }
        }

        private Status getStatus() {
            int part = 0;
            resetVisited();

            for (int r=0; r<N; r++) {
                for (int c=0; c<M; c++) {
                    if (visited[r][c] || field[r][c] == 0) continue;

                    Queue<Point> queue = new ArrayDeque<>();
                    queue.add(new Point(r, c));
                    visited[r][c] = true;
                    part++;

                    while (!queue.isEmpty()) {
                        Point now = queue.poll();

                        for (int delta=0; delta<4; delta++) {
                            int nr = now.r + dir[delta][0];
                            int nc = now.c + dir[delta][1];

                            if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                            if (visited[nr][nc] || field[nr][nc] == 0) continue;

                            visited[nr][nc] = true;
                            queue.add(new Point(nr, nc));
                        }
                    }
                }
            }

            if (part == 0) {
                return Status.EMPTY;
            } else if (part == 1) {
                return Status.ONE;
            } else {
                return Status.SEPARATED;
            }
        }

        public void melt() {
            int[][] meltCount = new int[N][M];

            for (int r=0; r<N; r++) {
                for (int c=0; c<M; c++) {
                    if (field[r][c] == 0) continue;

                    int count = 0;

                    for (int delta=0; delta<4; delta++) {
                        int nr = r + dir[delta][0];
                        int nc = c + dir[delta][1];

                        if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                        if (field[nr][nc] == 0) count++;
                    }

                    if (count > 0) {
                        meltCount[r][c] += count;
                    }
                }
            }

            for (int r=0; r<N; r++) {
                for (int c=0; c<M; c++) {
                    if (meltCount[r][c] == 0) continue;

                    field[r][c] = Math.max(0, field[r][c] - meltCount[r][c]);
                }
            }
        }
    }

    private static class Point {
        int r, c;

        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }
}
