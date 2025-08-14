package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek2979 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());

        int[] parkInfo = new int[101];
        for (int i = 0; i < 3; i++) {
            st = new StringTokenizer(br.readLine());

            int arrive = Integer.parseInt(st.nextToken());
            int left = Integer.parseInt(st.nextToken());

            for (int t = arrive; t < left; t++) {
                parkInfo[t] += 1;
            }
        }

        int cost = 0;
        for (int i = 0; i < 101; i++) {
            if (parkInfo[i] == 3) cost += C * 3;
            else if (parkInfo[i] == 2) cost += B * 2;
            else if (parkInfo[i] == 1) cost += A;
        }

        System.out.println(cost);
    }
}
