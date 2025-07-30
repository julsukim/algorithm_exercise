package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek2846 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int before = Integer.parseInt(st.nextToken());
        int diff = 0;
        int maximum = 0;
        for (int i = 1; i < N; i++) {
            int now = Integer.parseInt(st.nextToken());
            if (now > before) {
                diff += (now - before);
            } else {
                maximum = Math.max(maximum, diff);
                diff = 0;
            }
            before = now;
        }
        maximum = Math.max(maximum, diff);
        System.out.println(maximum);
    }
}
