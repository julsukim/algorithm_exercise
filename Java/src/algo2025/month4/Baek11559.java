package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek11559 {

    private static class Point {
        int r, c;

        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }
    }

    private static class PuyoPuyo {
        private int row = 12;
        private int col = 6;
        private char[][] field = new char[row][col];
        private boolean[][] visited = new boolean[row][col];
        private static final int[] dr = {-1, 1, 0, 0};
        private static final int[] dc = {0, 0, -1, 1};

        public void initFieldByRow(int row, String line) {
            for (int c=0; c<col; c++) {
                field[row][c] = line.charAt(c);
            }
        }

        public int simulate() {
            int chain = 0;

            while (true) {
                boolean popped = canPop();

                if (!popped) break;

                chain++;
                fall();
            }

            return chain;
        }

        private void resetVisited() {
            for (int r=0; r<row; r++) {
                Arrays.fill(visited[r], false);
            }
        }

        private boolean canPop() {
            boolean popped = false;
            resetVisited();

            for (int r=0; r<row; r++) {
                for (int c=0; c<col; c++) {
                    if (field[r][c] == '.' || visited[r][c]) continue;

                    Queue<Point> queue = new ArrayDeque<>();
                    List<Point> selectedList = new ArrayList<>();

                    Point curr = new Point(r, c);
                    queue.add(curr);
                    selectedList.add(curr);
                    visited[r][c] = true;

                    while (!queue.isEmpty()) {
                        Point now = queue.poll();

                        for (int delta=0; delta<4; delta++) {
                            int nr = now.r + dr[delta];
                            int nc = now.c + dc[delta];

                            if (nr < 0 || nr >= row || nc < 0 || nc >= col) continue;
                            if (visited[nr][nc] || field[nr][nc] != field[r][c]) continue;

                            visited[nr][nc] = true;
                            Point next = new Point(nr, nc);
                            selectedList.add(next);
                            queue.add(next);
                        }
                    }

                    if (selectedList.size() >= 4) {
                        for (Point p : selectedList) {
                            field[p.r][p.c] = '.';
                        }
                        popped = true;
                    }
                }
            }

            return popped;
        }

        private void fall() {
            for (int c=0; c<col; c++) {
                List<Character> column = new ArrayList<>();
                for (int r = row - 1; r>=0; r--) {
                    if (field[r][c] == '.') continue;
                    column.add(field[r][c]);
                }
                for (int r = row - 1, i = 0; r >= 0; r--, i++) {
                    if (i < column.size()) {
                        field[r][c] = column.get(i);
                    } else {
                        field[r][c] = '.';
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PuyoPuyo puyo = new PuyoPuyo();

        for (int i=0; i<12; i++) {
            puyo.initFieldByRow(i, br.readLine());
        }

        System.out.println(puyo.simulate());
    }
}
