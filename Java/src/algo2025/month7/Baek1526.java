package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek1526 {
    static int N;
    static int max = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        dfs("");
        System.out.println(max);
    }

    static void dfs(String current) {
        if (!current.isEmpty()) {
            int num = Integer.parseInt(current);
            if (num <= N) {
                max = Math.max(max, num);
            } else {
                return;
            }
        }

        if (current.length() > 10) return;

        dfs(current + "4");
        dfs(current + "7");
    }
}
