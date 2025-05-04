package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek2623 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        int[] indegree = new int[N+1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            if (k <= 0) continue;

            int prev = Integer.parseInt(st.nextToken());
            for (int j = 1; j < k; j++) {
                int curr = Integer.parseInt(st.nextToken());
                graph.get(prev).add(curr);
                indegree[curr]++;
                prev = curr;
            }
        }

        Queue<Integer> queue = new ArrayDeque<>();
        for (int i = 1; i <= N; i++) {
            if (indegree[i] == 0) {
                queue.offer(i);
            }
        }

        StringBuilder sb = new StringBuilder();
        int count = 0;
        while (!queue.isEmpty()) {
            int u = queue.poll();
            sb.append(u).append("\n");
            count++;

            for (int v : graph.get(u)) {
                if (--indegree[v] == 0) {
                    queue.offer(v);
                }
            }
        }

        if (count < N) {
            System.out.println(0);
        } else {
            System.out.println(sb.toString());
        }
    }
}
