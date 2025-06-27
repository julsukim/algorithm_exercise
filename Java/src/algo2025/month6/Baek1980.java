package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek1980 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());

        int minCoke = t;
        int maxBug = 0;

        for (int y = 0; y * n <= t; y++) {
            int rest = t - y * n;
            int x = rest / m;
            int coke = rest - x * m;
            int bug = y + x;

            if (coke < minCoke || (coke == minCoke && bug > maxBug)) {
                minCoke = coke;
                maxBug = bug;
            }
        }

        System.out.println(maxBug + " " + minCoke);
    }
}
