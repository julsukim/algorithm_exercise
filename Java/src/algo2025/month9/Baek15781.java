package algo2025.month9;

import java.io.*;
import java.util.*;

public class Baek15781 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int vast = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            vast = Math.max(vast, Integer.parseInt(st.nextToken()));
        }

        int head = 0;
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            head = Math.max(head, Integer.parseInt(st.nextToken()));
        }

        System.out.println(vast + head);
    }
}
