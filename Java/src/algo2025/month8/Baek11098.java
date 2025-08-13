package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek11098 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        while (n-- > 0) {
            int p = Integer.parseInt(br.readLine());
            int maxCost = Integer.MIN_VALUE;
            String targetName = "";
            for (int i = 0; i < p; i++) {
                st = new StringTokenizer(br.readLine());
                int cost = Integer.parseInt(st.nextToken());
                String name = st.nextToken();
                if (cost > maxCost) {
                    targetName = name;
                    maxCost = cost;
                }
            }
            sb.append(targetName);
            if (n >= 1) sb.append("\n");
        }
        System.out.println(sb);
    }
}
