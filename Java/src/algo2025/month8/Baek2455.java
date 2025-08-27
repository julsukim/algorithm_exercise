package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek2455 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int maxSum = 0;
        int sum = 0;
        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            int minus = Integer.parseInt(st.nextToken());
            int plus = Integer.parseInt(st.nextToken());

            sum += (plus - minus);
            maxSum = Math.max(maxSum, sum);
        }

        System.out.println(maxSum);
    }
}
