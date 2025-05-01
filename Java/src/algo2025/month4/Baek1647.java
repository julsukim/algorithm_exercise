package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1647 {

    static class Edge implements Comparable<Edge> {
        int from, to, weight;

        public Edge(int from, int to, int weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }

        @Override
        public int compareTo(Edge o) {
            return Integer.compare(weight, o.weight);
        }
    }

    static int[] parent;
    static int[] rank;

    static int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    static void union(int a, int b) {
        int rootA = find(a);
        int rootB = find(b);

        if (rootA == rootB) return;

        if (rank[rootA] < rank[rootB]) {
            parent[rootA] = rootB;
        } else if (rank[rootB] < rank[rootA]) {
            parent[rootB] = rootA;
        } else {
            parent[rootB] = rootA;
            rank[rootA]++;
        }
    }

    public static void main(String[] args) throws IOException {
        int N = readInt();
        int M = readInt();

        parent = new int[N + 1];
        rank = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            parent[i] = i;
            rank[i] = 0;
        }

        Edge[] edges = new Edge[M];
        for (int i = 0; i < M; i++) {
            int from = readInt();
            int to = readInt();
            int weight = readInt();
            edges[i] = new Edge(from, to, weight);
        }

        Arrays.sort(edges);

        int mstWeight = 0;
        int maximumWeight = -1;

        for (Edge edge : edges) {
            if (find(edge.from) != find(edge.to)) {
                union(edge.from, edge.to);
                mstWeight += edge.weight;
                maximumWeight = Math.max(maximumWeight, edge.weight);
            }
        }

        System.out.println(mstWeight - maximumWeight);
    }

    // 입력을 빠르게 처리하는 함수
    private static int readInt() throws IOException {
        int c, n = 0;
        while ((c = System.in.read()) > 32) { // 공백(스페이스, 개행 등)보다 큰 값만 처리
            n = (n * 10) + (c & 15);
        }
        return n;
    }
}
