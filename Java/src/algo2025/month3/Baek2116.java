package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek2116 {

    static int n;
    static int[][] dices;
    static Map<Integer, Integer> map;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        map = new HashMap<>();
        map.put(0, 5);
        map.put(1, 3);
        map.put(2, 4);
        map.put(3, 1);
        map.put(4, 2);
        map.put(5, 0);

        dices = new int[n][6];
        StringTokenizer st;
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<6; j++) {
                dices[i][j] = Integer.parseInt(st.nextToken());
            }
        }


        int result = 0;

        for (int i=1; i<7; i++) {
            result = Math.max(result, getMaxValueOf(i));
        }

        System.out.println(result);
    }

    static int getMaxValueOf(int top) {
        int sum = 0;

        for (int i = 0; i < n; i++) {
            int topIdx = -1, bottomIdx = -1;

            // 현재 주사위에서 top이 어느 인덱스인지 찾고, bottomIdx 계산
            for (int j = 0; j < 6; j++) {
                if (dices[i][j] == top) {
                    bottomIdx = j;
                    topIdx = map.get(j);
                    top = dices[i][topIdx];  // 다음 주사위에 전달할 top
                    break;
                }
            }

            // 현재 주사위에서 옆면 후보 중 가장 큰 값 선택
            int maxSide = 0;
            for (int j = 0; j < 6; j++) {
                if (j != topIdx && j != bottomIdx) {
                    maxSide = Math.max(maxSide, dices[i][j]);
                }
            }

            sum += maxSide;
        }

        return sum;
    }
}
