package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek5567 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i=0; i<N+1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i=0; i<M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        int start = 1;
        int[] visited = new int[N+1];
        Queue<Integer> queue = new ArrayDeque<>();
        queue.add(start);
        visited[1] = 1;

        while (!queue.isEmpty()) {
            int cur = queue.poll();

            for (int next : graph.get(cur)) {
                if (visited[next] != 0) continue;

                int dist = visited[cur] + 1;
                if (dist > 3) continue;

                visited[next] = dist;
                queue.add(next);
            }
        }

        int count = 0;
        for (int cnt : visited) {
            if (cnt > 0) count++;
        }

        System.out.println(count - 1);
    }
}
