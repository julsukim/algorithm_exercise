package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek1491 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int left = 0, right = N - 1;
        int bottom = 0, top = M - 1;
        int dir = 0; // 0=동, 1=북, 2=서, 3=남
        int x = 0, y = 0; // 마지막 방문 좌표

        while (left <= right && bottom <= top) {
            switch (dir) {
                case 0: // → 동쪽
                    x = right;
                    y = bottom;
                    bottom++;
                    break;
                case 1: // ↑ 북쪽
                    x = right;
                    y = top;
                    right--;
                    break;
                case 2: // ← 서쪽
                    x = left;
                    y = top;
                    top--;
                    break;
                default: // 3: ↓ 남쪽
                    x = left;
                    y = bottom;
                    left++;
                    break;
            }
            dir = (dir + 1) % 4;
        }

        // 최종 좌표 출력
        System.out.println(x + " " + y);
    }
}
