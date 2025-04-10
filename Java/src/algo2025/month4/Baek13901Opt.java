package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek13901Opt {

    private enum Direction {
        UP(-1, 0), DOWN(1, 0), LEFT(0, -1), RIGHT(0, 1);

        final int dr, dc;

        Direction(int dr, int dc) {
            this.dr = dr;
            this.dc = dc;
        }

        public static Direction fromInt(int dir) {
            switch (dir) {
                case 1: return UP;
                case 2: return DOWN;
                case 3: return LEFT;
                case 4: return RIGHT;
                default: throw new IllegalArgumentException("Invalid direction: " + dir);
            }
        }
    }

    private static class Point {
        int r, c;

        Point(int r, int c) {
            this.r = r;
            this.c = c;
        }

        Point move(Direction d) {
            return new Point(r + d.dr, c + d.dc);
        }

        boolean isInBounds(int R, int C) {
            return r >= 0 && r < R && c >= 0 && c < C;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        // 입력: 방 크기
        st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        // 입력: 장애물
        int[][] board = new int[R][C]; // 0: 빈칸, -1: 장애물
        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int brR = Integer.parseInt(st.nextToken());
            int brC = Integer.parseInt(st.nextToken());
            board[brR][brC] = -1;
        }

        // 입력: 시작 위치
        st = new StringTokenizer(br.readLine());
        int sr = Integer.parseInt(st.nextToken());
        int sc = Integer.parseInt(st.nextToken());
        Point current = new Point(sr, sc);

        // 입력: 방향 순서
        st = new StringTokenizer(br.readLine());
        Direction[] directions = new Direction[4];
        for (int i = 0; i < 4; i++) {
            directions[i] = Direction.fromInt(Integer.parseInt(st.nextToken()));
        }

        // 시뮬레이션 시작
        boolean[][] visited = new boolean[R][C];
        visited[current.r][current.c] = true;

        int dirIndex = 0;
        int failCount = 0;

        while (failCount < 4) {

            Direction dir = directions[dirIndex % 4];
            Point next = current.move(dir);

            if (!next.isInBounds(R, C) || board[next.r][next.c] == -1 || visited[next.r][next.c]) {
                dirIndex++;
                failCount++;
                continue;
            }

            // 이동 성공
            current = next;
            visited[current.r][current.c] = true;
            failCount = 0; // 초기화
        }

        System.out.println(current.r + " " + current.c);
    }
}
