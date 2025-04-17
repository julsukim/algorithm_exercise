package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek10971Dp {

    static int N;
    static int[][] W;
    static int[][] dp;
    static final int INF = 1_000_000_000;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        W = new int[N][N];
        dp = new int[1 << N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                W[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int[] row : dp) {
            Arrays.fill(row, -1);
        }

        System.out.println(tsp(1, 0));  // 시작: 도시 0만 방문, 현재 위치 0
    }

    static int tsp(int visited, int current) {
        if (visited == (1 << N) - 1) {
            // 모든 도시 방문 완료 → 출발점(0)으로 돌아감
            if (W[current][0] == 0) return INF;
            return W[current][0];
        }

        if (dp[visited][current] != -1) {
            return dp[visited][current];
        }

        int minCost = INF;

        for (int next = 0; next < N; next++) {
            // 이미 방문했거나, 길이 없으면 스킵
            if ((visited & (1 << next)) != 0 || W[current][next] == 0) continue;

            int cost = W[current][next] + tsp(visited | (1 << next), next);
            minCost = Math.min(minCost, cost);
        }

        dp[visited][current] = minCost;
        return minCost;
    }
}
