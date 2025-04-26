package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek24954 {

    static int N;
    static int[] originalPrice;
    static List<List<int[]>> discounts;
    static int minCost = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());

        originalPrice = new int[N + 1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=1; i<=N; i++) {
            originalPrice[i] = Integer.parseInt(st.nextToken());
        }

        discounts = new ArrayList<>();
        for (int i=0; i<=N; i++) {
            discounts.add(new ArrayList<>());
        }
        for (int i=1; i<=N; i++) {
            int p = Integer.parseInt(br.readLine());
            for (int j=0; j<p; j++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int d = Integer.parseInt(st.nextToken());
                discounts.get(i).add(new int[]{a, d});
            }
        }

        boolean[] visited = new boolean[N + 1];
        List<Integer> path = new ArrayList<>();

        permute(0, visited, path);

        System.out.println(minCost);
    }

    static void permute(int depth, boolean[] visited, List<Integer> path) {
        if (depth == N) {
            simulate(path);
            return;
        }

        for (int i=1; i<=N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                path.add(i);
                permute(depth+1, visited, path);
                path.remove(path.size() - 1);
                visited[i] = false;
            }
        }
    }

    static void simulate(List<Integer> order) {
        int[] currentPrice = Arrays.copyOf(originalPrice, N+1);
        int totalCost = 0;

        for (int potion : order) {
            totalCost += currentPrice[potion];

            for (int[] discount : discounts.get(potion)) {
                int target = discount[0];
                int discountAmount = discount[1];
                currentPrice[target] = Math.max(1, currentPrice[target] - discountAmount);
            }
        }

        minCost = Math.min(minCost, totalCost);
    }
}
