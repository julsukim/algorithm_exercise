package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek21736 {

    static int[] di = {-1, 1, 0, 0};
    static int[] dj = {0, 0, -1, 1};
    static char[][] graph;
    static int n;
    static int m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[] startPoint = new int[2];

        graph = new char[n][m];
        for (int i=0; i<n; i++) {
            String line = br.readLine();
            for (int j=0; j<m; j++) {
                char ch = line.charAt(j);
                if (ch == 'I') {
                    startPoint[0] = i;
                    startPoint[1] = j;
                }
                graph[i][j] = ch;
            }
        }

        int result = bfs(startPoint);
        System.out.println(result > 0 ? result : "TT");
    }

    static int bfs(int[] sp) {
        int count = 0;

        boolean[][] visited = new boolean[n][m];
        Queue<int[]> queue = new ArrayDeque<>();

        queue.offer(sp);
        visited[sp[0]][sp[1]] = true;

        while (!queue.isEmpty()) {
            int[] now = queue.poll();
            int i = now[0];
            int j = now[1];

            for (int delta=0; delta<4; delta++) {
                int ni = i + di[delta];
                int nj = j + dj[delta];

                if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
                if (visited[ni][nj] || graph[ni][nj] == 'X') continue;

                if (graph[ni][nj] == 'P') count++;
                visited[ni][nj] = true;
                queue.offer(new int[]{ni, nj});
            }
        }

        return count;
    }
}
