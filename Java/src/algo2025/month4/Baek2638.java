package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek2638 {

    private static int N, M;
    private static int[][] field;
    private static boolean[][] visited;
    private static final int[][] dir = new int[][]{{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    private static int cheeseCount = 0;

    private static class Point {
        int r, c;

        public Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    private static void resetVisited() {
        for (boolean[] v : visited) {
            Arrays.fill(v, false);
        }
    }

    private static void setField() {
        resetVisited();
        Queue<Point> queue = new ArrayDeque<>();
        queue.add(new Point(0, 0));
        visited[0][0] = true;
        field[0][0] = -1;

        while (!queue.isEmpty()) {
            Point cur = queue.poll();

            for (int delta=0; delta<4; delta++) {
                int nr = cur.r + dir[delta][0];
                int nc = cur.c + dir[delta][1];

                if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                if (visited[nr][nc] || field[nr][nc] == 1) continue;

                field[nr][nc] = -1;
                visited[nr][nc] = true;
                queue.add(new Point(nr, nc));
            }
        }
    }

    private static void melt() {
        List<Point> meltList = new ArrayList<>();

        for (int r=1; r<N-1; r++) {
            for (int c=1; c<M-1; c++) {
                if (field[r][c] != 1) continue;

                int count = 0;

                for (int delta=0; delta<4; delta++) {
                    int nr = r + dir[delta][0];
                    int nc = c + dir[delta][1];

                    if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue;
                    if (field[nr][nc] != -1) continue;

                    count++;
                }

                if (count >= 2) {
                    meltList.add(new Point(r, c));
                }
            }
        }

        for (Point p : meltList) {
            field[p.r][p.c] = 0;
            cheeseCount--;
        }
    }

    private static boolean isMelted() {
        return cheeseCount == 0;
    }

    private static int simulation() {
        int time = 0;

        while (true) {
            if (isMelted()) break;

            setField();
            melt();
            time++;
        }

        return time;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        field = new int[N][M];
        visited = new boolean[N][M];
        for (int r=0; r<N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c=0; c<M; c++) {
                int status = Integer.parseInt(st.nextToken());
                field[r][c] = status;

                if (status == 1) cheeseCount++;
            }
        }

        System.out.println(simulation());
    }
}
