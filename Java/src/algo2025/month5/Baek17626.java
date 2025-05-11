package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek17626 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int[] dp = new int[N+1];
        final int INF = N+1;

        dp[0] = 0;
        for (int i = 1; i <= N; i++) {
            dp[i] = INF;
        }

        for (int i = 1; i <= N; i++) {
            for (int k = 1; k*k <= i; k++) {
                dp[i] = Math.min(dp[i], dp[i - k*k] + 1);
            }
        }

        System.out.println(dp[N]);
    }

    /*
      BFS
     */
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int N = Integer.parseInt(br.readLine());
//
//        boolean[] visited = new boolean[N+1];
//        Queue<int[]> queue = new ArrayDeque<>();
//        queue.offer(new int[]{N, 0});
//        visited[N] = true;
//
//        while (!queue.isEmpty()) {
//            int[] cur = queue.poll();
//            int value = cur[0];
//            int depth = cur[1];
//
//            if (value == 0) {
//                System.out.println(depth);
//                break;
//            }
//
//            for (int k = 1; k*k <= value; k++) {
//                int next = value - k*k;
//                if (!visited[next]) {
//                    visited[next] = true;
//                    queue.offer(new int[]{next, depth + 1});
//                }
//            }
//        }
//    }
}
