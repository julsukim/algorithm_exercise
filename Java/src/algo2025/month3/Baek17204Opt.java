package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek17204Opt {

    static int[] graph;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        graph = new int[n];
        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            graph[i] = Integer.parseInt(br.readLine());
        }

        int result = findMinimumM(0, k);
        System.out.println(result);
    }

    static int findMinimumM(int start, int target) {
        int count = 0;
        int current = start;

        while (!visited[current]) {
            visited[current] = true;
            if (current == target) {
                return count;  // 보성이를 찾았으면 현재까지 카운트 반환
            }
            current = graph[current];
            count++;
        }

        return -1;  // 순환 발생 시 보성이 찾지 못했으면 -1
    }
}
