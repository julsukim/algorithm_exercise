package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek2711 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            String b = st.nextToken();
            for (int j = 0; j < b.length(); j++) {
                if (j != a - 1) sb.append(b.charAt(j));
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
