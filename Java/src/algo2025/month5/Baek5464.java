package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek5464 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] costs = new int[n];
        int[] cars = new int[m];

        for (int i = 0; i < n; i++) {
            costs[i] = Integer.parseInt(br.readLine());
        }

        for (int i = 0; i < m; i++) {
            cars[i] = Integer.parseInt(br.readLine());
        }

        int[] slots = new int[n];
        int sum = 0;

        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < m * 2; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num > 0) {
                boolean isParked = false;
                for (int s = 0; s < n; s++) {
                    if (slots[s] == 0) {
                        slots[s] = num;
                        isParked = true;
                        break;
                    }
                }
                if (!isParked) {
                    q.offer(num);
                }
            } else {
                num = Math.abs(num);

                for (int s = 0; s < n; s++) {
                    if (slots[s] == num) {
                        sum += costs[s] * cars[num-1];
                        slots[s] = 0;

                        if (!q.isEmpty()) {
                            slots[s] = q.poll();
                        }
                        break;
                    }
                }
            }
        }

        System.out.println(sum);
    }
}
