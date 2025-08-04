package algo2025.month8;

import java.io.*;

public class Baek7567 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String bowl = br.readLine();
        int N = bowl.length();

        int height = 10;
        char before = bowl.charAt(0);

        for (int i = 1; i < N; i++) {
            char cur = bowl.charAt(i);

            if (cur == before) {
                height += 5;
            } else {
                height += 10;
            }
            before = cur;
        }

        System.out.println(height);
    }
}
