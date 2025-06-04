package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek1411 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        String[] words = new String[N];
        for (int i = 0; i < N; i++) {
            words[i] = br.readLine();
        }

        int counter = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (isSimilar(words[i], words[j])) counter++;
            }
        }

        System.out.println(counter);
    }

    private static boolean isSimilar(String a, String b) {
        Map<Character, Character> charMap = new HashMap<>();
        Set<Character> used = new HashSet<>();
        for (int i = 0; i < a.length(); i++) {
            if (charMap.containsKey(a.charAt(i))) {
                if (charMap.get(a.charAt(i)) != b.charAt(i)) return false;
            } else {
                if (used.contains(b.charAt(i))) return false;

                charMap.put(a.charAt(i), b.charAt(i));
                used.add(b.charAt(i));
            }
        }
        return true;
    }
}
