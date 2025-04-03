package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1058Opt {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        boolean[][] isFriend = new boolean[N][N];
        for (int i=0; i<N; i++) {
            String line = br.readLine();
            for (int j=0; j<N; j++) {
                char c = line.charAt(j);
                if (c == 'Y') {
                    isFriend[i][j] = true;
                }
            }
        }

        int max = 0;
        for (int i = 0; i < N; i++) {
            int count = 0;
            for (int j = 0; j < N; j++) {
                if (i == j) continue;
                if (isFriend[i][j]) count++;
                else {
                    for (int k = 0; k < N; k++) {
                        if (isFriend[i][k] && isFriend[k][j]) {
                            count++;
                            break;
                        }
                    }
                }
            }
            max = Math.max(max, count);
        }

        System.out.println(max);

//        int maximum = 0;
//
//        for (int i=0; i<N; i++) {
//
//            boolean[] visited = new boolean[N];
//
//            Queue<int[]> queue = new ArrayDeque<>();
//            queue.offer(new int[]{i, 0});
//            visited[i] = true;
//
//            int count = 0;
//
//            while (!queue.isEmpty()) {
//                int[] cur = queue.poll();
//                int now = cur[0];
//                int depth = cur[1];
//
//                if (depth == 2) break;
//
//                for (int next=0; next<N; next++) {
//                    if (!isFriend[now][next]) continue;
//                    if (visited[next]) continue;
//
//                    visited[next] = true;
//                    count++;
//                    queue.offer(new int[]{next, depth+1});
//                }
//            }
//            maximum = Math.max(maximum, count);
//        }
//
//        System.out.println(maximum);
    }
}
