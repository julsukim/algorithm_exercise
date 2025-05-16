package algo2025.month5;

import java.io.*;
import java.util.*;

//public class Baek15649 {
//
//    private static StringBuilder answer;
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine());
//        int N = Integer.parseInt(st.nextToken());
//        int M = Integer.parseInt(st.nextToken());
//
//        answer = new StringBuilder();
//        solution(N, M, 0, new int[M], new HashSet<>());
//        System.out.println(answer);
//    }
//
//    private static void solution(int N, int M, int idx, int[] nums, Set<Integer> visited) {
//        if (idx == M) {
//            answer.append(
//                    Arrays.stream(nums)
//                    .mapToObj(String::valueOf)
//                    .collect(Collectors.joining(" "))
//                    ).append("\n");
//            return;
//        }
//
//        for (int i = 1; i <= N; i++) {
//            if (visited.contains(i)) continue;
//            nums[idx] = i;
//            visited.add(i);
//            solution(N, M, idx + 1, nums, visited);
//            visited.remove(i);
//        }
//    }
//}

public class Baek15649 {
    private static int N, M;
    private static int[] nums;
    private static boolean[] used;
    private static StringBuilder answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        nums = new int[M];
        used = new boolean[N + 1];

        answer = new StringBuilder();
        dfs(0);
        System.out.println(answer.toString());
    }

    private static void dfs(int depth) {
        if (depth == M) {
            for (int num : nums) {
                answer.append(num).append(" ");
            }
            answer.append("\n");
            return;
        }

        for (int i = 1; i <= N; i++) {
            if (used[i]) continue;
            nums[depth] = i;
            used[i] = true;
            dfs(depth + 1);
            used[i] = false;
        }
    }
}
