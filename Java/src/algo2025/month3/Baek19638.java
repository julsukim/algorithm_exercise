package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek19638 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());

        Queue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for (int i=0; i<n; i++) {
            pq.offer(Integer.parseInt(br.readLine()));
        }

        int count = 0;
        while (count < t) {
            int tallest = pq.poll();
            if (tallest < h) { // 이미 모두 작음
                pq.offer(tallest);
                break;
            }
            if (tallest == 1) { // 더 줄일 수 없음
                pq.offer(tallest);
                break;
            }

            pq.offer(tallest / 2); // 줄임
            count++;
        }

        if (pq.peek() < h) {
            System.out.println("YES");
            System.out.println(count);
        } else {
            System.out.println("NO");
            System.out.println(pq.peek());
        }
    }
}
