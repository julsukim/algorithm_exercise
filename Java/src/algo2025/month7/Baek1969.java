package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek1969 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        String[] arr = new String[N];
        for (int i = 0; i < N; i++) {
            arr[i] = br.readLine();
        }

        StringBuilder sb = new StringBuilder();
        int mismatches = 0;

        for (int i = 0; i < M; i++) {
            int[] count = new int[4];

            for (int j = 0; j < N; j++) {
                char n = arr[j].charAt(i);

                if (n == 'A') {
                    count[0]++;
                } else if (n == 'C') {
                    count[1]++;
                } else if (n == 'G') {
                    count[2]++;
                } else {
                    count[3]++;
                }
            }

            char[] nts = {'A', 'C', 'G', 'T'};
            int maxIdx = 0;
            for (int k = 1; k < 4; k++) {
                if (count[k] > count[maxIdx]) {
                    maxIdx = k;
                }
            }

            sb.append(nts[maxIdx]);
            mismatches += (N - count[maxIdx]);
        }

        System.out.println(sb.toString());
        System.out.println(mismatches);
    }
}
