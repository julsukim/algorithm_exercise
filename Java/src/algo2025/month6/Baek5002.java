package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek5002 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());
        String line = br.readLine();

        LinkedList<Character> queue = new LinkedList<>();
        for (char c : line.toCharArray()) {
            queue.add(c);
        }

        int m = 0, w = 0, cnt = 0;
        while (!queue.isEmpty()) {
            if (canAdmit(queue.getFirst(), m, w, X)) {
                char c = queue.removeFirst();
                if (c == 'M') m++;
                else w++;
            } else if (queue.size() >= 2 && canAdmit(queue.get(1), m, w, X)) {
                char c = queue.remove(1);
                if (c == 'M') m++;
                else w++;
            } else {
                break;
            }
            cnt++;
        }

        System.out.println(cnt);
    }

    private static boolean canAdmit(char c, int m, int w, int X) {
        if (c == 'M') {
            return Math.abs((m + 1) - w) <= X;
        } else {
            return Math.abs(m - (w + 1)) <= X;
        }
    }
}
