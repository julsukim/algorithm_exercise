package algo2025.month4;

import java.io.*;
import java.util.*;

class Point {
    int r, c;
    Point(int r, int c) {
        this.r = r;
        this.c = c;
    }
}

class Nations {
    private int N, L, R;
    private int[][] map;
    private static final int[] dr = {-1, 1, 0, 0};
    private static final int[] dc = {0, 0, -1, 1};
    private final boolean[][] visited = new boolean[50][50];

    public void initialize(String line) {
        StringTokenizer st = new StringTokenizer(line);
        this.N = Integer.parseInt(st.nextToken());
        this.L = Integer.parseInt(st.nextToken());
        this.R = Integer.parseInt(st.nextToken());

        this.map = new int[N][N];
    }

    public void setMapRow(int row, String line) {
        StringTokenizer st = new StringTokenizer(line);
        for (int col=0; col<N; col++) {
            this.map[row][col] = Integer.parseInt(st.nextToken());
        }
    }

    public int getN() {
        return N;
    }

    public int movePopulation() {
        int days = 0;

        while (true) {

            resetVisited();
            boolean isMoved = false;

            for (int r=0; r<N; r++) {
                for (int c=0; c<N; c++) {
                    if (visited[r][c]) continue;

                    if (processUnion(r, c, visited)) {
                        isMoved = true;
                    }
                }
            }

            if (!isMoved) break;
            days++;
        }

        return days;
    }

    private void resetVisited() {
        for (int i = 0; i < N; i++) {
            Arrays.fill(visited[i], false);
        }
    }

    private boolean processUnion(int r, int c, boolean[][] visited) {
        Queue<Point> queue = new ArrayDeque<>();
        List<Point> union = new ArrayList<>();

        queue.offer(new Point(r, c));
        union.add(new Point(r, c));
        visited[r][c] = true;

        int populationSum = map[r][c];

        while (!queue.isEmpty()) {
            Point current = queue.poll();

            for (int d = 0; d < 4; d++) {
                int nr = current.r + dr[d];
                int nc = current.c + dc[d];

                if (nr < 0 || nr >= N || nc < 0 || nc >= N) continue;
                if (visited[nr][nc]) continue;

                int diff = Math.abs(map[current.r][current.c] - map[nr][nc]);
                if (diff < L || diff > R) continue;

                queue.offer(new Point(nr, nc));
                union.add(new Point(nr, nc));
                visited[nr][nc] = true;
                populationSum += map[nr][nc];
            }
        }

        if (union.size() > 1) {
            int average = populationSum / union.size();
            for (Point p : union) {
                map[p.r][p.c] = average;
            }
            return true;
        }

        return false;
    }
}

public class Baek16234 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Nations nations = new Nations();
        nations.initialize(br.readLine());

        for (int r=0; r<nations.getN(); r++) {
            nations.setMapRow(r, br.readLine());
        }

        System.out.println(nations.movePopulation());
    }
}
