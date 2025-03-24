package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek1051 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] arr = new char[n][m];
        for (int i = 0; i < n; i++) {
            arr[i] = br.readLine().toCharArray();
        }

        int max = 1;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                // n, m 중에 최대(넘지않고)로 갈수있는 만큼만 확인
                for (int k = 1; i + k < n && j + k < m; k++) {
                    if (arr[i][j] == arr[i][j + k] &&
                            arr[i][j] == arr[i + k][j] &&
                            arr[i][j] == arr[i + k][j + k]) {
                        max = Math.max(max, k + 1);
                    }
                }
            }
        }
        System.out.println(max * max);
    }
}
