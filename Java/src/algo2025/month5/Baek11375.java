package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek11375 {

    private static int N, M;
    private static List<Integer>[] adj;
    private static int[] match;
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        adj = new ArrayList[N+1];
        for (int i = 1; i <= N; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            for (int j = 0; j < k; j++) {
                int v = Integer.parseInt(st.nextToken());
                adj[i].add(v);
            }
        }

        match = new int[M + 1];
        int result = 0;

        for (int u = 1; u <= N; u++) {
            visited = new boolean[M + 1];
            if (dfs(u)) {
                result++;
            }
        }

        System.out.println(result);
    }

    private static boolean dfs(int u) {
        for (int v : adj[u]) {
            if (visited[v]) continue;

            visited[v] = true;

            if (match[v] == 0 || dfs(match[v])) {
                match[v] = u;
                return true;
            }
        }
        return false;
    }
}
