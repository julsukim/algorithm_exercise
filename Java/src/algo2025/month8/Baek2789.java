package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek2789 {

    private static String censoredWord = "CAMBRIDGE";

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();

        Set<Character> censor = new HashSet<>();
        for (int i = 0; i < censoredWord.length(); i++) {
            censor.add(censoredWord.charAt(i));
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (censor.contains(c)) continue;
            sb.append(c);
        }

        System.out.println(sb);
    }
}
