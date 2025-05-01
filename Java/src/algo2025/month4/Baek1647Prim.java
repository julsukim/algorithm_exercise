package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1647Prim {
    static class Edge implements Comparable<Edge> {
        int to, weight;

        public Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge other) {
            return this.weight - other.weight;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        List<Edge>[] graph = new ArrayList[N+1];
        for (int i = 0; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            graph[from].add(new Edge(to, weight));
            graph[to].add(new Edge(from, weight));
        }

        boolean[] visited = new boolean[N+1];
        PriorityQueue<Edge> pq = new PriorityQueue<>();

        int start = 1;
        visited[start] = true;
        pq.addAll(graph[start]);

        int mstWeight = 0;
        int edgesUsed = 0;
        int maxEdgeWeight = -1;

        while (!pq.isEmpty() && edgesUsed < N - 1) {
            Edge edge = pq.poll();

            if (visited[edge.to]) continue;

            visited[edge.to] = true;
            mstWeight += edge.weight;
            edgesUsed++;
            maxEdgeWeight = Math.max(maxEdgeWeight, edge.weight);

            pq.addAll(graph[edge.to]);
        }

        System.out.println(mstWeight - maxEdgeWeight);
    }
}
