package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek1284 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = "";
        StringBuilder sb = new StringBuilder();
        while (true) {
            input = br.readLine();
            if (input.equals("0")) break;
            int L = input.length();
            int width = 1;
            for (int i = 0; i < L; i++) {
                char c = input.charAt(i);
                if (c == '1') {
                    width += 2;
                } else if (c == '0') {
                    width += 4;
                } else {
                    width += 3;
                }
                width++;
            }
            sb.append(width).append("\n");
        }
        System.out.println(sb);
    }
}
