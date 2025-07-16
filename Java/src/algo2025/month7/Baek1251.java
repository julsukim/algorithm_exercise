package algo2025.month7;

import java.io.*;

public class Baek1251 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        int N = S.length();
        String ans = null;

        for (int i = 1; i <= N - 2; i++) {

            for (int j = i + 1; j <= N - 1; j++) {
                String a = reverse(S.substring(0, i));
                String b = reverse(S.substring(i, j));
                String c = reverse(S.substring(j, N));

                String candidate = a + b + c;
                if (ans == null || candidate.compareTo(ans) < 0) {
                    ans = candidate;
                }
            }
        }

        System.out.println(ans);
    }

    private static String reverse(String s) {
        return new StringBuilder(s).reverse().toString();
    }
}

