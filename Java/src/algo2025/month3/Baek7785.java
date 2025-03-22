package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek7785 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Set<String> entered = new TreeSet<>(Collections.reverseOrder());
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            String status = st.nextToken().intern();
            if (status == "enter") {
                entered.add(name);
            } else if (status == "leave") {
                entered.remove(name);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (String s : entered) {
            sb.append(s).append("\n");
        }
        System.out.println(sb);
    }
}
