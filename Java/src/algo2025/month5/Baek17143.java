package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek17143 {

    private static int R, C;
    private static int[][] board;
    private static Map<Integer, int[]> sharks;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        board = new int[R+1][C+1];

        sharks = new HashMap<>();
        for (int i = 1; i <= M; i ++) {
            st = new StringTokenizer(br.readLine());
            int[] info = new int[5];
            for (int j = 0; j < 5; j++) {
                info[j] = Integer.parseInt(st.nextToken());
            }
            board[info[0]][info[1]] = i;
            sharks.put(i, info);
        }

        int result = simulate();
        System.out.println(result);
    }

    private static int simulate() {
        int fishingCount = 0;
        for (int fisherIdx = 1; fisherIdx <= C; fisherIdx++) {
            for (int r = 1; r <= R; r++) {
                int boardInfo = board[r][fisherIdx];
                if (boardInfo != 0) {
                    fishingCount += sharks.get(boardInfo)[4];
                    board[r][fisherIdx] = 0;
                    sharks.remove(boardInfo);
                    break;
                }
            }
            move();
        }
        return fishingCount;
    }

    private static void move() {
        int[][] newBoard = new int[R+1][C+1];
        List<Integer> dieList = new ArrayList<>();

        for (Map.Entry<Integer, int[]> entry : sharks.entrySet()) {
            int num = entry.getKey();
            int[] info = entry.getValue();
            int r = info[0], c = info[1], s = info[2], d = info[3], z = info[4];

            // 1차원 반사(reflection) 계산
            if (d == 1 || d == 2) {
                int period = 2 * (R - 1);
                int raw = (r - 1) + (d == 1 ? -s : s);
                int m = raw % period;
                if (m < 0) m += period;
                boolean forward = m <= R - 1;
                int pos0 = forward ? m : period - m;
                info[0] = pos0 + 1;
                info[3] = forward ? d : (d == 1 ? 2 : 1);
            } else {
                int period = 2 * (C - 1);
                int raw = (c - 1) + (d == 3 ? s : -s);
                int m = raw % period;
                if (m < 0) m += period;
                boolean forward = m <= C - 1;
                int pos0 = forward ? m : period - m;
                info[1] = pos0 + 1;
                info[3] = forward ? d : (d == 3 ? 4 : 3);
            }

            // 같은 칸 상어 충돌 처리 (크기 비교)
            int nr = info[0], nc = info[1];
            if (newBoard[nr][nc] != 0) {
                int other = newBoard[nr][nc];
                int otherSize = sharks.get(other)[4];
                if (otherSize > z) {
                    dieList.add(num);
                    continue;
                } else {
                    dieList.add(other);
                }
            }
            newBoard[nr][nc] = num;
        }

        // 죽은 상어 제거
        for (int dead : dieList) {
            sharks.remove(dead);
        }
        // 보드 갱신
        board = newBoard;
    }
}
