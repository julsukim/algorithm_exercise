package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek11557 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        while (T-- > 0) {
            int N = Integer.parseInt(br.readLine());

            int maximum = 0;
            String max = "";

            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                String name = st.nextToken();
                int count = Integer.parseInt(st.nextToken());
                if (count >= maximum) {
                    maximum = count;
                    max = name;
                }
            }

            sb.append(max).append("\n");
        }
        System.out.println(sb);
    }
}
