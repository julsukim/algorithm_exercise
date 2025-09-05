package algo2025.month8;

import java.io.*;
import java.util.*;

public class baek10797 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int count = 0;
        for (int i = 0; i < 5; i++) {
            String num = st.nextToken();
            if (num.charAt(num.length() - 1) == (char) ('0' + N)) {
                count++;
            }
        }
        System.out.println(count);
    }
}
