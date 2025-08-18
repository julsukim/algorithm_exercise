package algo2025.month8;

import java.io.*;

public class Baek18406 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String N = br.readLine();
        int L = N.length();
        int half = L / 2;
        int lSide = 0;
        int rSide = 0;
        for (int i = 0; i < L; i++) {
            int num = Integer.parseInt(String.valueOf(N.charAt(i)));
            if (i < half) {
                lSide += num;
            } else {
                rSide += num;
            }
        }
        System.out.println(lSide == rSide ? "LUCKY" : "READY");
    }
}
