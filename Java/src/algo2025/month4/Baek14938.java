package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek14938 {

    private static final int INF = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int R = Integer.parseInt(st.nextToken());

        int[] items = new int[N+1];
        st = new StringTokenizer(br.readLine());
        for (int i=1; i<N+1; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }

        List<List<int[]>> graph = new ArrayList<>();
        for (int i=0; i<N+1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i=0; i<R; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            graph.get(start).add(new int[]{end, dist});
            graph.get(end).add(new int[]{start, dist});
        }

        int answer = 0;

        for (int s=1; s<N+1; s++) {
            int[] dist = new int[N+1];
            Arrays.fill(dist, INF);
            dist[s] = 0;

            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));
            pq.add(new int[]{s, 0});

            while (!pq.isEmpty()) {
                int[] now = pq.poll();
                int cur = now[0];
                int cost = now[1];

                if (cost > dist[cur]) continue;

                for (int[] node : graph.get(cur)) {
                    int next = node[0];
                    int newDist = dist[cur] + node[1];
                    if (newDist < dist[next]) {
                        dist[next] = newDist;
                        pq.add(new int[]{next, newDist});
                    }
                }
            }

            int sum = 0;
            for (int i=1; i<=N; i++) {
                if (dist[i] <= M) {
                    sum += items[i];
                }
            }

            answer = Math.max(answer, sum);
        }

        System.out.println(answer);
    }
}
