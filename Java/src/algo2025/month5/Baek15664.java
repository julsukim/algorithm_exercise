package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek15664 {

    private static int N, M;
    private static int[] candidates, nums;
    private static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        candidates = new int[N];
        nums = new int[M];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            candidates[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(candidates);

        sb = new StringBuilder();
        dfs(0, 0);

        System.out.println(sb.toString());
    }

    private static void dfs(int depth, int start) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(nums[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        int prev = -1;
        for (int i = start; i < N; i++) {
            if (candidates[i] == prev) continue;
            prev = candidates[i];
            nums[depth] = candidates[i];
            dfs(depth + 1, i + 1);
        }
    }
}
