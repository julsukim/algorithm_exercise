package algo2025.month4;

import java.io.*;

public class Baek1676 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int count = 0;

        for (int i = 5; i <= N; i *= 5) {
            count += N / i;
        }

        System.out.println(count);
    }
}

