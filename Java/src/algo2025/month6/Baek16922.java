package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek16922 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        Set<Integer> sums = new HashSet<>();

        for (int c1 = 0; c1 <= N; c1++) {
            for (int c2 = 0; c2 <= N - c1; c2++) {
                for (int c3 = 0; c3 <= N - c1 - c2; c3++) {
                    int c4 = N - c1 - c2 - c3;
                    int sum = c1 * 1 + c2 * 5 + c3 * 10 + c4 * 50;
                    sums.add(sum);
                }
            }
        }

        System.out.println(sums.size());
    }
}
