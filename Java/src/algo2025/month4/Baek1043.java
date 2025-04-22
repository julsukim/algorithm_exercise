package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1043 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int T = Integer.parseInt(st.nextToken());
        List<Integer> truth = new ArrayList<>();
        for (int i=0; i<T; i++) {
            truth.add(Integer.parseInt(st.nextToken()));
        }

        List<List<Integer>> graph = new ArrayList<>();
        for (int i=0; i<=N; i++) {
            graph.add(new ArrayList<>());
        }

        List<int[]> parties = new ArrayList<>();
        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int P = Integer.parseInt(st.nextToken());
            int[] partyInfo = new int[P];
            for (int j=0; j<P; j++) {
                partyInfo[j] = Integer.parseInt(st.nextToken());
            }
            parties.add(partyInfo);

            for (int a=0; a<P-1; a++) {
                for (int b=a+1; b<P; b++) {
                    graph.get(partyInfo[a]).add(partyInfo[b]);
                    graph.get(partyInfo[b]).add(partyInfo[a]);
                }
            }
        }

        Set<Integer> knowTruth = new HashSet<>();
        boolean[] visited = new boolean[N+1];
        for (int t : truth) {
            if (visited[t]) continue;
            visited[t] = true;
            Queue<Integer> queue = new ArrayDeque<>();
            queue.add(t);

            while (!queue.isEmpty()) {
                int cur = queue.poll();
                knowTruth.add(cur);

                for (int next : graph.get(cur)) {
                    if (visited[next]) continue;

                    visited[next] = true;
                    queue.add(next);
                }
            }
        }

        int count = 0;
        for (int[] party : parties) {
            boolean isPossible = true;
            for (int p : party) {
                if (knowTruth.contains(p)) {
                    isPossible = false;
                    break;
                }
            }
            if (isPossible) count++;
        }

        System.out.println(count);
    }
}
