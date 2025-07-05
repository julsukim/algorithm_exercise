package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek1324 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int N = s.length();
        StringBuilder ans = new StringBuilder();
        int suf = 0;
        for (int i = 0; i < N; i++) {
            if (s.charAt(i) == '.') {
                if (suf > 0) {
                    if (suf % 2 == 1) {
                        System.out.println(-1);
                        return;
                    }
                    int b4 = suf / 4;
                    int b2 = (suf % 4) > 0 ? 1 : 0;
                    while (b4-- > 0) {
                        ans.append("AAAA");
                    }
                    while (b2-- > 0) {
                        ans.append("BB");
                    }
                }
                ans.append('.');
                suf = 0;
            } else {
                suf++;
            }
        }
        if (suf > 0) {
            if (suf % 2 == 1) {
                System.out.println(-1);
                return;
            }
            int b4 = suf / 4;
            int b2 = (suf % 4) > 0 ? 1 : 0;
            while (b4-- > 0) {
                ans.append("AAAA");
            }
            while (b2-- > 0) {
                ans.append("BB");
            }
        }
        System.out.println(ans);
    }
}
