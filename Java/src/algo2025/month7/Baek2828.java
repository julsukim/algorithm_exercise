package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek2828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int left = 0;
        int right = M - 1;

        int cnt = 0;
        int J = Integer.parseInt(br.readLine());
        for (int i = 0; i < J; i++) {
            int loc = Integer.parseInt(br.readLine()) - 1;

            int diff = 0;
            if (loc < left) {
                diff = loc - left;
            } else if (loc > right) {
                diff = loc - right;
            }

            left += diff;
            right += diff;
            cnt += Math.abs(diff);
        }

        System.out.println(cnt);
    }
}
