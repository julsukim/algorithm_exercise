package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek1434 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[] caps = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            caps[i] = Integer.parseInt(st.nextToken());
        }

        int answer = 0;
        int idx = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int book = Integer.parseInt(st.nextToken());
            for (int j = idx; j < N; j++) {
                if (caps[j] >= book) {
                    caps[j] -= book;
                    break;
                } else {
                    idx++;
                }
            }
        }
        for (int i = 0; i < N; i++) {
            answer += caps[i];
        }

        System.out.println(answer);
    }
}
