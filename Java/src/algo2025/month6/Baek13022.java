package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek13022 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        int i = 0;
        int len = s.length();

        while (i < len) {
            if (s.charAt(i) != 'w') {
                System.out.println(0);
                return;
            }

            int n = 0;
            while (i < len && s.charAt(i) == 'w') {
                n++;
                i++;
            }

            if (n == 0) {
                System.out.println(0);
                return;
            }

            if (!check(s, len, i, 'o', n) ||
                !check(s, len, i, 'l', n) ||
                !check(s, len, i, 'f', n)
            ) {
                System.out.println(0);
                return;
            }

            i += 3 * n;
        }

        System.out.println(1);
    }

    private static boolean check(String s, int len, int pos, char ch, int n) {
        if (pos + n > len) return false;
        for (int k = 0; k < n; k++) {
            if (s.charAt(pos + k) != ch) return false;
        }
        return true;
    }
}
