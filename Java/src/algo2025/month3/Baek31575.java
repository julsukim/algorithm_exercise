package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek31575 {

    static int[][] graph;
    static boolean[][] visited;
    static int[] di = {0, 1};
    static int[] dj = {1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        graph = new int[n][m];
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0; j<m; j++) {
                graph[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        System.out.println(bfs(n, m) ? "Yes" : "No");
    }

    static boolean bfs(int n, int m) {
        visited = new boolean[n][m];

        Queue<int[]> dq = new ArrayDeque<>();
        dq.offer(new int[]{0, 0});
        visited[0][0] = true;

        while (!dq.isEmpty()) {
            int[] cur = dq.poll();
            int i = cur[0];
            int j = cur[1];

            for (int dir=0; dir<2; dir++) {
                int ni = i + di[dir];
                int nj = j + dj[dir];

                if (ni >= 0 && ni < n && nj >= 0 && nj < m) {
                    if (!visited[ni][nj] && graph[ni][nj] == 1) {
                        visited[ni][nj] = true;
                        dq.offer(new int[]{ni, nj});
                    }
                }
            }
        }
        return visited[n-1][m-1];
    }
}
