package algo2025.month3;

import java.io.*;
import java.util.*;

public class baek2775 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int tc=0; tc<t; tc++) {
            int k = Integer.parseInt(br.readLine());
            int n = Integer.parseInt(br.readLine());

            int[][] arr = new int[k+1][n+1];
            for (int i=0; i<n+1; i++) {
                arr[0][i] = i;
            }
            for (int i=1; i<k+1; i++) {
                for (int j=1; j<n+1; j++) {
                    arr[i][j] = arr[i-1][j] + arr[i][j-1];
                }
            }

            sb.append(arr[k][n]).append("\n");
        }

        System.out.println(sb);
    }

}
