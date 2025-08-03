package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek11170 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        while (T-- > 0) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
//            int counter = 0;
//
//            for (int i = n; i <= m; i++) {
//                String num = String.valueOf(i);
//                for (int c = 0; c < num.length(); c++) {
//                    if (num.charAt(c) == '0') counter++;
//                }
//            }

            sb.append(countZeros(n, m)).append("\n");
        }
        System.out.println(sb);
    }

    public static int countZeros(int A, int B) {
        int result = 0;

        for (int i = A; i <= B; i++) {
            int num = i;
            if (num == 0) {
                result++;
                continue;
            }
            while (num != 0) {
                int rest = num % 10;
                if (rest == 0) result++;
                num /= 10;
            }
        }

        return result;
    }
}
