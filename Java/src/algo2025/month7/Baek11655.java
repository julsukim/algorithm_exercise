package algo2025.month7;

import java.io.*;

public class Baek11655 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();
        int N = line.length();

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < N; i++) {
            char c = line.charAt(i);
            if (c >= 'a' && c <= 'z') {
                sb.append((char) ('a' + (c - 'a' + 13) % 26));
            } else if (c >= 'A' && c <= 'Z') {
                sb.append((char) ('A' + (c - 'A' + 13) % 26));
            } else {
                sb.append(c);
            }
        }

        System.out.println(sb);
    }
}
