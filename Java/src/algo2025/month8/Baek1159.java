package algo2025.month8;

import java.io.*;

public class Baek1159 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        int[] players = new int[26];

        for (int i = 0; i < N; i++) {
            char f = br.readLine().charAt(0);
            players[f - 'a']++;
        }

        boolean flag = false;
        for (int i = 0; i < 26; i++) {
            if (players[i] >= 5) {
                flag = true;
                char c = (char) (i + 'a');
                sb.append(c);
            }
        }

        System.out.println(flag ? sb : "PREDAJA");
    }
}
