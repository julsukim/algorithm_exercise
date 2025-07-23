package algo2025.month7;

import java.io.*;

public class Baek1032 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] names = new String[N];
        for (int i = 0; i < N; i++) {
            names[i] = br.readLine();
        }
        int L = names[0].length();
        StringBuilder sb = new StringBuilder();
        boolean isSame = true;
        for (int i = 0; i < L; i++) {
            isSame = true;
            char now = names[0].charAt(i);
            for (int j = 1; j < N; j++) {
                if (now != names[j].charAt(i)) {
                    isSame = false;
                    break;
                }
            }
            sb.append(isSame ? now : '?');
        }
        System.out.println(sb.toString());
    }
}
