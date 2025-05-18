package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek1913 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int target = Integer.parseInt(br.readLine());
        int[][] map = new int[N][N];
        // 시작 위치: 중앙 (0-indexed)
        int r = N / 2, c = N / 2;
        map[r][c] = 1;
        // 찾을 위치 초기화
        int tr = r, tc = c;
        if (target == 1) {
            tr = r;
            tc = c;
        }
        int num = 1;

        // 상, 우, 하, 좌 방향 벡터
        int[] dr = { -1, 0, 1,  0 };
        int[] dc = {  0, 1, 0, -1 };
        int dir = 0;     // 현재 방향 인덱스
        int step = 1;    // 한 방향으로 이동할 칸 수

        // 바깥으로 나선 형태 채우기
        outer:
        while (num < N * N) {
            for (int rep = 0; rep < 2; rep++) {
                for (int i = 0; i < step; i++) {
                    r += dr[dir];
                    c += dc[dir];
                    num++;
                    map[r][c] = num;
                    if (num == target) {
                        tr = r;
                        tc = c;
                    }
                    // 최댓값(N*N) 채운 뒤 더 이상 이동하지 않도록 종료
                    if (num == N * N) {
                        break outer;
                    }
                }
                dir = (dir + 1) % 4;
            }
            step++;
        }

        // 결과 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                sb.append(map[i][j]).append(' ');
            }
            sb.append('\n');
        }
        sb.append(tr + 1).append(' ').append(tc + 1);
        System.out.print(sb);
    }
}