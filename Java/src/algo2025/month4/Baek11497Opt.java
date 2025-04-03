package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek11497Opt {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            int[] arr = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(arr);
            Deque<Integer> deque = new ArrayDeque<>();
            for (int i = 0; i < N; i++) {
                if (i % 2 == 0) deque.offerFirst(arr[i]);
                else deque.offerLast(arr[i]);
            }

            int maxDiff = Math.abs(deque.peekFirst() - deque.peekLast());
            int prev = deque.poll();
            while (!deque.isEmpty()) {
                int cur = deque.poll();
                int diff = Math.abs(prev - cur);
                maxDiff = Math.max(maxDiff, diff);
                prev = cur;
            }

            sb.append(maxDiff).append("\n");
        }

        System.out.print(sb);
    }
}
