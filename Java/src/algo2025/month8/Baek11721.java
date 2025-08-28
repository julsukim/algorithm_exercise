package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek11721 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        int N = word.length();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
            if (i != 0 && i % 10 == 0) {
                sb.append("\n");
            }
            sb.append(word.charAt(i));
        }

        System.out.println(sb);
    }
}
