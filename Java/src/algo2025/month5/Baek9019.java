package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek9019 {

    private static final char[] queries = new char[]{'D', 'S', 'L', 'R'};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            Queue<Integer> queue = new ArrayDeque<>();
            queue.offer(a);

            String[] commands = new String[10000];
            boolean[] visited = new boolean[10000];
            commands[a] = "";
            visited[a] = true;

            while (!queue.isEmpty()) {
                int cur = queue.poll();
                if (cur == b) break;

                for (char q : queries) {
                    int next = calculate(cur, q);

                    if (!visited[next]) {
                        visited[next] = true;
                        String query = commands[cur] + q;
                        commands[next] = query;
                        queue.offer(next);
                    }
                }
            }

            sb.append(commands[b]).append("\n");
        }

        System.out.println(sb.toString());
    }

    private static int calculate(int num, char cmd) {
        switch (cmd) {
            case 'D':
                return (num * 2) % 10000;
            case 'S':
                return (num == 0) ? 9999 : num - 1;
            case 'L':
                return (num % 1000) * 10 + (num / 1000);
            case 'R':
                return (num % 10) * 1000 + (num / 10);
        }
        return -1;
    }
}
