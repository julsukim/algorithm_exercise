package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1417 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int my = Integer.parseInt(br.readLine());

        int count = 0;

        if (N > 1) {
            Queue<Integer> arr = new PriorityQueue<>(Comparator.reverseOrder());
            for (int i=0; i<N-1; i++) {
                arr.offer(Integer.parseInt(br.readLine()));
            }

            while (my <= arr.peek()) {
                int max = arr.poll();
                my++;
                max--;
                count++;
                arr.offer(max);
            }

        }

        System.out.println(count);
    }
}
