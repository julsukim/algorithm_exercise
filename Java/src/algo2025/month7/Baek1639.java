package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek1639 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int n = s.length();
        if (n < 2) {
            System.out.println(0);
            return;
        }

        int[] prefix = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            prefix[i] = prefix[i - 1] + (s.charAt(i - 1) - '0');
        }

        int maxLen = 0;
        for (int len = (n % 2 == 0 ? n : n - 1); len >= 2; len -= 2) {
            boolean found = false;
            for (int i = 0; i + len <= n; i++) {
                int mid = i + len / 2;
                int leftSum = prefix[mid] - prefix[i];
                int rightSum = prefix[i + len] - prefix[mid];
                if (leftSum == rightSum) {
                    maxLen = len;
                    found = true;
                    break;
                }
            }
            if (found) break;
        }

        System.out.println(maxLen);
    }
}