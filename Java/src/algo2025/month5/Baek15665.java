package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek15665 {

    private static int N, M, L;
    private static int[] nums;
    private static int[] numArr;
    private static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        nums = new int[N];
        numArr = new int[M];
        sb = new StringBuilder();

        Set<Integer> numSet = new HashSet<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(st.nextToken());
            numSet.add(num);
        }

        L = numSet.size();
        nums = new int[L];
        int idx = 0;
        for (int num : numSet) {
            nums[idx] = num;
            idx++;
        }
        Arrays.sort(nums);
        dfs(0);

        System.out.println(sb.toString());
    }

    private static void dfs(int depth) {
        if (depth == M) {
            for (int i = 0; i < M; i++) {
                sb.append(numArr[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = 0; i < L; i++) {
            numArr[depth] = nums[i];
            dfs(depth + 1);
        }
    }
}
