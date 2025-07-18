package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek11576 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        int decimalValue = 0;
        for (int i = 0; i < m; i++) {
            int digit = Integer.parseInt(st.nextToken());
            decimalValue = decimalValue * A + digit;
        }

        if (decimalValue == 0) {
            System.out.println(0);
        } else {
            List<Integer> converted = new ArrayList<>();
            while (decimalValue > 0) {
                converted.add(decimalValue % B);
                decimalValue /= B;
            }
            Collections.reverse(converted);

            StringBuilder sb = new StringBuilder();
            for (int d : converted) {
                sb.append(d).append(' ');
            }
            sb.setLength(sb.length() - 1);
            System.out.println(sb);
        }
    }
}
