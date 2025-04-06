package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek15657 {

    private static StringBuilder sb = new StringBuilder();
    private static int N, M;
    private static int[] arr, result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        arr = new int[N];
        result = new int[M];
        st = new StringTokenizer(br.readLine());
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);

        dfs(0, 0);

        System.out.println(sb);
    }

    private static void dfs(int depth, int start) {
        if (depth == M) {
            for (int i=0; i<M; i++) {
                sb.append(result[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i=start; i<N; i++) {
            result[depth] = arr[i];
            dfs(depth + 1, i);
        }
    }
}
