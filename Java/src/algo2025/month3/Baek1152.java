package algo2025.month3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Baek1152 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().trim().split(" ");
        if (input.length == 1 && input[0].equals("")) {
            System.out.println(0);
        } else {
            System.out.println(input.length);
        }
    }
}
