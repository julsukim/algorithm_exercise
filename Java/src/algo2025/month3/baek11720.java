package algo2025.month3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baek11720 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int sum = 0;
        char[] c = br.readLine().toCharArray();
        for (int i = 0; i < n; i++) {
            sum += c[i] - '0';
        }
        System.out.println(sum);
    }
}
