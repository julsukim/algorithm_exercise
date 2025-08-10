package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek2851 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int diff = 100;
        int score = 0;
        int result = 0;

        for (int i = 0; i < 10; i++) {
            int item = Integer.parseInt(br.readLine());

            score += item;
            int tmp = Math.abs(100 - score);
            if (tmp <= diff) {
                result = score;
                diff = tmp;
            }
        }

        System.out.println(result);
    }
}
