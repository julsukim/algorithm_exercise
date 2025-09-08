package algo2025.month9;

import java.io.*;
import java.util.*;

public class Baek2506 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int streak = 0;
        int score = 0;
        for (int i = 0; i < N; i++) {
            int res = Integer.parseInt(st.nextToken());
            if (res == 1) {
                score += res;
                score += streak;
                streak++;
            } else {
                streak = 0;
            }
        }
        System.out.println(score);
    }
}
