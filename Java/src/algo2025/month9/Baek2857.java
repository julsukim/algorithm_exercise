package algo2025.month9;

import java.io.*;

public class Baek2857 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        boolean isFind = false;
        for (int i = 1; i <= 5; i++) {
            String name = br.readLine();
            int l = name.length();
            for (int c = 0; c < l - 2; c++) {
                if (name.charAt(c) == 'F' && name.charAt(c + 1) == 'B' && name.charAt(c + 2) == 'I') {
                    sb.append(i).append(' ');
                    isFind = true;
                    break;
                }
            }
        }

        System.out.println(isFind ? sb : "HE GOT AWAY!");
    }
}
