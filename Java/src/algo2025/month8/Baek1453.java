package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek1453 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        Set<Integer> set = new HashSet<>();

        int denied = 0;
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());

            if (num < 1 || num > 100) {
                denied++;
                continue;
            }

            if (set.contains(num)) {
                denied++;
            } else {
                set.add(num);
            }
        }

        System.out.println(denied);
    }
}
