package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek9375 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            Map<String, Integer> map = new HashMap<>();
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                String name = st.nextToken();
                String category = st.nextToken();
                map.put(category, map.getOrDefault(category, 0) + 1);
            }

            int result = 1;
            for (Integer v : map.values()) {
                result *= (v + 1);
            }

            sb.append(result - 1).append("\n");
        }

        System.out.println(sb.toString());
    }
}
