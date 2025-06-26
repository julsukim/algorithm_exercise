package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek25943 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int left = Integer.parseInt(st.nextToken());
        int right = Integer.parseInt(st.nextToken());
        for (int i = 0; i < N - 2; i++) {
            int s = Integer.parseInt(st.nextToken());
            if (left == right) {
                left += s;
            } else {
                if (left > right) right += s;
                else left += s;
            }
        }

        int diff = Math.abs(left - right);
        int count = 0;
        int[] weights = new int[]{100, 50, 20, 10, 5, 2, 1};
        for (int i = 0; i < 7; i++) {
            if (diff == 0) break;
            count += diff / weights[i];
            diff %= weights[i];
        }
        System.out.println(count);
    }
}
