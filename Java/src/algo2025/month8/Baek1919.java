//package algo2025.month8;
//
//import java.io.*;
//import java.util.*;
//
//public class Baek1919 {
//    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        String a = br.readLine();
//        String b = br.readLine();
//        int aL = a.length();
//        int bL = b.length();
//
//        Map<Character, Integer> aMap = new HashMap<>();
//        Map<Character, Integer> bMap = new HashMap<>();
//        Set<Character> aSet = new HashSet<>();
//        for (int i = 0; i < aL; i++) {
//            aSet.add(a.charAt(i));
//            aMap.put(a.charAt(i), aMap.getOrDefault(a.charAt(i), 0) + 1);
//        }
//
//        for (int i = 0; i < bL; i++) {
//            bMap.put(b.charAt(i), bMap.getOrDefault(b.charAt(i), 0) + 1);
//        }
//
//        int sameCount = 0;
//        for (char c : aSet) {
//            if (bMap.containsKey(c)) {
//                sameCount += Math.min(aMap.get(c), bMap.get(c));
//            }
//        }
//
//        System.out.println(aL + bL - 2 * sameCount);
//    }
//}

package algo2025.month8;

import java.io.*;

public class Baek1919 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine();
        String b = br.readLine();

        int[] diff = new int[26]; // a에서 +1, b에서 -1
        for (int i = 0; i < a.length(); i++) diff[a.charAt(i) - 'a']++;
        for (int i = 0; i < b.length(); i++) diff[b.charAt(i) - 'a']--;

        int ans = 0;
        for (int d : diff) ans += Math.abs(d);
        System.out.println(ans);
    }
}

