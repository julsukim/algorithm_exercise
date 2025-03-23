package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek10773 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        Deque<Integer> stack = new ArrayDeque<>();
        for (int i = 0; i < k; i++) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) {
                stack.poll();
                continue;
            }
            stack.push(n);
        }
        int sum = stack.stream().reduce(0, Integer::sum);
        System.out.println(sum);
    }
}
