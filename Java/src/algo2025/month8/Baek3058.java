package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek3058 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        StringTokenizer st;
        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            int min = 101;
            int sum = 0;
            for (int i = 0; i < 7; i++) {
                int num = Integer.parseInt(st.nextToken());
                if (num % 2 == 0) {
                    min = Math.min(min, num);
                    sum += num;
                }
            }
            sb.append(sum).append(" ").append(min).append("\n");
        }
        System.out.println(sb);
    }
}
