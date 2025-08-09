package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek3985 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int L = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());

        int expected = 0, eCount = 0, result = 0, rCount = 0;

        boolean[] occupied = new boolean[L];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());

            int p = Integer.parseInt(st.nextToken()) - 1;
            int k = Integer.parseInt(st.nextToken()) - 1;

            int e = k - p + 1;
            if (e > eCount) {
                expected = i + 1;
                eCount = e;
            }

            int tmpCount = 0;
            for (int j = p; j <= k; j++) {
                if (!occupied[j]) {
                    tmpCount++;
                    occupied[j] = true;
                }
            }

            if (tmpCount > rCount) {
                result = i + 1;
                rCount = tmpCount;
            }
        }

        System.out.println(expected + "\n" + result);
    }
}
