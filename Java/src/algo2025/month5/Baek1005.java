package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek1005 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 0; tc < T; tc++) {
            st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int K = Integer.parseInt(st.nextToken());

            int[] times = new int[N+1];
            st = new StringTokenizer(br.readLine());
            for (int i = 1; i <= N; i++) {
                times[i] = Integer.parseInt(st.nextToken());
            }

            List<List<Integer>> buildOrder = new ArrayList<>();
            for (int i = 0; i <= N; i++) {
                buildOrder.add(new ArrayList<>());
            }

            int[] indegree = new int[N+1];

            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                int X = Integer.parseInt(st.nextToken());
                int Y = Integer.parseInt(st.nextToken());

                buildOrder.get(X).add(Y);
                indegree[Y]++;
            }

            int W = Integer.parseInt(br.readLine());

            Queue<Integer> queue = new ArrayDeque<>();

            for (int i = 1; i <= N; i++) {
                if (indegree[i] == 0) queue.add(i);
            }

            int[] dp = new int[N+1];
            for (int i = 1; i <= N; i++) {
                dp[i] = times[i];
            }

            while (!queue.isEmpty()) {
                int cur = queue.poll();
                if (cur == W) break;

                for (int next : buildOrder.get(cur)) {
                    dp[next] = Math.max(dp[next], dp[cur] + times[next]);
                    indegree[next]--;
                    if (indegree[next] == 0) queue.add(next);
                }
            }

            sb.append(dp[W]).append("\n");
        }

        System.out.println(sb.toString());
    }
}
