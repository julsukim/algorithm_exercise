package algo2025.month3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baek10809 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        StringBuilder sb = new StringBuilder();

//        char[] chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
//        for (int i = 0; i < chars.length; i++) {
//            sb.append(s.indexOf(chars[i])).append(" ");
//        }

        for (char c = 'a'; c <= 'z'; c++) {
            sb.append(s.indexOf(c)).append(" ");
        }

        System.out.println(sb);
    }
}
