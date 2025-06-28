package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek1972 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        while (true) {
            String word = br.readLine();

            if (word.equals("*")) break;

            boolean isSurprising = true;

            int l = word.length();
            for (int d = 1; d < l; d++) {

                Set<String> wordSet = new HashSet<>();
                int cnt = 0;
                StringBuilder wm = new StringBuilder();

                for (int i = 0; i < l - d; i++) {
                    wm.append(word.charAt(i)).append(word.charAt(i + d));
                    wordSet.add(wm.toString());
                    wm.setLength(0);
                    cnt++;
                }

                if (wordSet.size() != cnt) {
                    isSurprising = false;
                    break;
                }
            }

            sb.append(word);
            if (isSurprising) sb.append(" is surprising.");
            else sb.append(" is NOT surprising.");
            sb.append("\n");
        }

        System.out.println(sb);
    }
}
