package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek2346 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        Deque<int[]> deque = new ArrayDeque<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            deque.offer(new int[]{i, Integer.parseInt(st.nextToken())});
        }
        while (!deque.isEmpty()) {
            int[] now = deque.pollFirst();
            sb.append(now[0]).append(" ");

            if (deque.isEmpty()) break;

            if (now[1] > 0) {
                for (int i=0; i<now[1]-1; i++) {
                    int[] next = deque.pollFirst();
                    deque.offerLast(next);
//                    if (next != null) {
//                        deque.offerLast(next);
//                    }
                }
            } else if (now[1] < 0) {
                for (int i=0; i>now[1]; i--) {
                    int[] next = deque.pollLast();
                    deque.offerFirst(next);
//                    if (next != null) {
//                        deque.offerFirst(next);
//                    }
                }
            }
        }
        System.out.println(sb);
    }
}
