package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek2636 {

    static class Point {
        public int r, c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    static class Cheese {
        private int R, C;
        private int[][] board;
        private int count;
        private static final int[] dr = {-1, 1, 0, 0};
        private static final int[] dc = {0, 0, -1, 1};
        private boolean[][] visited;

        public Cheese(int r, int c) {
            this.R = r;
            this.C = c;
            board = new int[R][C];
            visited = new boolean[R][C];
        }

        public void setBoardByRow(int row, String line) {
            StringTokenizer st = new StringTokenizer(line);
            for (int col=0; col<C; col++) {
                int e = Integer.parseInt(st.nextToken());
                board[row][col] = e;
                if (e == 1) count++;
            }
        }

        public int getCount() {
            return this.count;
        }

        public int simulate() {
            int time = 0;

            while (true) {
                time++;

                int currentCount = count;

                resetVisited();

                Queue<Point> queue = new ArrayDeque<>();
                queue.offer(new Point(0, 0));
                visited[0][0] = true;

                List<Point> meltList = new ArrayList<>();

                while (!queue.isEmpty()) {
                    Point current = queue.poll();

                    if (board[current.r][current.c] == 1) continue;

                    for (int delta=0; delta<4; delta++) {
                        int nr = current.r + dr[delta];
                        int nc = current.c + dc[delta];

                        if (nr < 0 || nr >= R || nc < 0 || nc >= C) continue;
                        if (visited[nr][nc]) continue;

                        if (board[nr][nc] == 1) meltList.add(new Point(nr, nc));

                        visited[nr][nc] = true;
                        queue.offer(new Point(nr, nc));
                    }
                }

                for (Point p : meltList) {
                    currentCount--;
                    board[p.r][p.c] = 0;
                }

                if (currentCount == 0) {
                    return time;
                }

                count = currentCount;
            }
        }

        private void resetVisited() {
            for (int row=0; row<R; row++) {
                Arrays.fill(visited[row], false);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        Cheese cheese = new Cheese(r, c);
        for (int row=0; row<r; row++) {
            cheese.setBoardByRow(row, br.readLine());
        }

        int time = cheese.simulate();
        System.out.println(time);
        System.out.println(cheese.count);
    }
}
