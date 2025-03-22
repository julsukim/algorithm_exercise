package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek1620 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> nameToNum = new HashMap<>();
        String[] numToName = new String[n+1];

        for (int i = 1; i < n+1; i++) {
            String name = br.readLine();
            nameToNum.put(name, i);
            numToName[i] = name;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < m; i++) {
            String query = br.readLine();
            if (isNumber(query)) {
                int index = Integer.parseInt(query);
                sb.append(numToName[index]).append("\n");
            } else {
                sb.append(nameToNum.get(query)).append("\n");
            }
        }
        System.out.println(sb);
    }

    private static boolean isNumber(String s) {
        char c = s.charAt(0);
        return c >= '0' && c <= '9';
    }
}
