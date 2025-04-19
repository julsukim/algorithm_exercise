package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek17140 {
    static int[][] arr = new int[101][101];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        for (int i = 1; i <= 3; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= 3; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int rowSize = 3, colSize = 3;
        int time = 0;

        while (time <= 100) {
            if (r <= rowSize && c <= colSize && arr[r][c] == k) {
                System.out.println(time);
                return;
            }

            if (rowSize >= colSize) {
                colSize = doR(rowSize, colSize);
            } else {
                rowSize = doC(rowSize, colSize);
            }

            time++;
        }

        System.out.println(-1);
    }

    static int doR(int rowSize, int colSize) {
        int newColSize = 0;

        for (int i = 1; i <= rowSize; i++) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int j = 1; j <= colSize; j++) {
                if (arr[i][j] == 0) continue;
                map.put(arr[i][j], map.getOrDefault(arr[i][j], 0) + 1);
            }

            List<int[]> list = new ArrayList<>();
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                list.add(new int[]{entry.getKey(), entry.getValue()});
            }

            list.sort((a, b) -> {
                if (a[1] != b[1]) return a[1] - b[1];
                return a[0] - b[0];
            });

            int idx = 1;
            for (int[] pair : list) {
                if (idx > 100) break;
                arr[i][idx++] = pair[0];
                if (idx > 100) break;
                arr[i][idx++] = pair[1];
            }

            for (int j = idx; j <= 100; j++) {
                arr[i][j] = 0;
            }

            newColSize = Math.max(newColSize, idx - 1);
        }

        return newColSize;
    }

    static int doC(int rowSize, int colSize) {
        int newRowSize = 0;

        for (int j = 1; j <= colSize; j++) {
            Map<Integer, Integer> map = new HashMap<>();
            for (int i = 1; i <= rowSize; i++) {
                if (arr[i][j] == 0) continue;
                map.put(arr[i][j], map.getOrDefault(arr[i][j], 0) + 1);
            }

            List<int[]> list = new ArrayList<>();
            for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
                list.add(new int[]{entry.getKey(), entry.getValue()});
            }

            list.sort((a, b) -> {
                if (a[1] != b[1]) return a[1] - b[1];
                return a[0] - b[0];
            });

            int idx = 1;
            for (int[] pair : list) {
                if (idx > 100) break;
                arr[idx++][j] = pair[0];
                if (idx > 100) break;
                arr[idx++][j] = pair[1];
            }

            for (int i = idx; i <= 100; i++) {
                arr[i][j] = 0;
            }

            newRowSize = Math.max(newRowSize, idx - 1);
        }

        return newRowSize;
    }
}
