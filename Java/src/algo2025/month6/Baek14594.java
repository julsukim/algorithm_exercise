package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek14594 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        boolean[] broken = new boolean[N+1];

        int M = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            for (int j = s; j < e; j++) {
                broken[j] = true;
            }
        }

        int count = 1;
        for (int i = 1; i < N; i++) {
            if (!broken[i]) count++;
        }

        System.out.println(count);
    }
}
