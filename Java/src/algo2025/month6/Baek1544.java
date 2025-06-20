package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek1544 {

//    private static String canonical(String s) {
//        String min = s;
//        for (int i = 1; i < s.length(); i++) {
//            String rot = s.substring(i) + s.substring(0, i);
//            if (rot.compareTo(min) < 0) min = rot;
//        }
//        return min;
//    }
//
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int N = Integer.parseInt(br.readLine());
//
//        Set<String> wordSet = new HashSet<>();
//        for (int i = 0; i < N; i++) {
//            String word = br.readLine();
//            wordSet.add(canonical(word));
//        }
//
//        System.out.println(wordSet.size());
//    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        Set<String> wordSet = new HashSet<>();
        for (int i = 0; i < N; i++) {
            String word = br.readLine();

            if (wordSet.isEmpty()) {
                wordSet.add(word);
                continue;
            }

            boolean findCycle = false;
            for (String st : wordSet) {
                if (isCycle(st, word)) {
                    findCycle = true;
                    break;
                }
            }

            if (!findCycle) wordSet.add(word);
        }

        System.out.println(wordSet.size());
    }

    private static boolean isCycle(String a, String b) {
        return a.length() == b.length() && (a + a).contains(b);
    }

//    private static boolean isCycle(String a, String b) {
//        int al = a.length();
//        int bl = b.length();
//
//        if (al != bl) return false;
//
//        char fc = a.charAt(0);
//        List<Integer> startList = new ArrayList<>();
//
//        for (int i = 0; i < bl; i++) {
//            if (fc == b.charAt(i)) startList.add(i);
//        }
//        if (startList.isEmpty()) return false;
//
//        for (int i = 0; i < startList.size(); i++) {
//            boolean isCycle = true;
//            for (int j = 0; j < al; j++) {
//                if (a.charAt(j) != b.charAt((startList.get(i) + j) % bl)) isCycle = false;
//            }
//            if (isCycle) return true;
//        }
//
//        return false;
//    }
}
