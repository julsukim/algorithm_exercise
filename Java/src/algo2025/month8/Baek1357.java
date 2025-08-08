package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek1357 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int X = Integer.parseInt(st.nextToken());
        int Y = Integer.parseInt(st.nextToken());

        System.out.println(rev(rev(X) + rev(Y)));
    }

    static int rev(int n) {
        String num = String.valueOf(n);
        StringBuilder sb = new StringBuilder();
        for (int i = num.length() - 1; i >= 0; i--) {
            sb.append(num.charAt(i));
        }
        return Integer.parseInt(String.valueOf(sb));
    }
}
