package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek9093 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                String word = st.nextToken();
                int L = word.length();
                for (int i = L - 1; i >= 0; i--) {
                    sb.append(word.charAt(i));
                }
                sb.append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
