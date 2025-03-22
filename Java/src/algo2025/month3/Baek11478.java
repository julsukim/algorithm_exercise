package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek11478 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        int length = input.length();
        Set<String> subStrings = new HashSet<>();
        for (int i = 1; i <= length; i++) {
            int start = 0;
            while (start+i <= length) {
                subStrings.add(input.substring(start, start + i));
                start++;
            }
        }
        System.out.println(subStrings.size());
    }
}
