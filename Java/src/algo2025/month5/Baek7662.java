package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek7662 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        while (T-- > 0) {
            int K = Integer.parseInt(br.readLine());

            TreeMap<Integer, Integer> map = new TreeMap<>();
            for (int i = 0; i < K; i++) {
                st = new StringTokenizer(br.readLine());
                char query = st.nextToken().charAt(0);
                int number = Integer.parseInt(st.nextToken());

                if (query == 'I') {
                    map.put(number, map.getOrDefault(number, 0) + 1);
                } else if (query == 'D') {
                    if (map.isEmpty()) continue;

                    int key = (number == 1) ? map.lastKey() : map.firstKey();
                    if (map.get(key) == 1) {
                        map.remove(key);
                    } else {
                        map.put(key, map.get(key) - 1);
                    }
                }
            }

            if (map.isEmpty()) {
                sb.append("EMPTY").append("\n");
            } else {
                sb.append(map.lastKey() + " " + map.firstKey()).append("\n");
            }
        }

        System.out.println(sb.toString());
    }
}
