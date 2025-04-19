package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek12853 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        boolean[] visited = new boolean[N + 1];
        int[] depth = new int[N + 1]; // 연산 횟수
        int[] from  = new int[N + 1]; // 경로 추적용

        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(N);
        visited[N] = true;
        from[N] = -1;

        while (!queue.isEmpty()) {
            int cur = queue.poll();

            if (cur == 1) break;

            int[] nexts = {cur - 1, cur % 2 == 0 ? cur / 2 : -1, cur % 3 == 0 ? cur / 3 : -1};

            for (int next : nexts) {
                if (next > 0 && !visited[next]) {
                    visited[next] = true;
                    queue.add(next);
                    depth[next] = depth[cur] + 1;
                    from[next] = cur;
                }
            }
        }

        System.out.println(depth[1]);

        List<Integer> path = new ArrayList<>();
        for (int cur = 1; cur != -1; cur = from[cur]) {
            path.add(cur);
        }
        Collections.reverse(path);
        StringBuilder sb = new StringBuilder();
        for (int num : path) {
            sb.append(num).append(" ");
        }
        System.out.println(sb);
    }
}
