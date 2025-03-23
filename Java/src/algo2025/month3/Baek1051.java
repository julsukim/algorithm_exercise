package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek1051 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String[][] arr = new String[n][m];
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split("");
            arr[i] = s;
        }

        int max = 1;
        int min = Math.min(n, m);
        for (int i = 0; i < n - max; i++) {
            for (int j = 0; j < m - max; j++) {
                // n, m 중에 최대(넘지않고)로 갈수있는 만큼만 확인
                for (int k = 1; k < min; k++) {

                }
            }
        }
    }
}
