package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek23037 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String number = br.readLine();
        int result = 0;
        for (int i = 0; i < 5; i++) {
            int num = Integer.parseInt(String.valueOf(number.charAt(i)));
            int five = num;
            for (int j = 0; j < 4; j++) {
                five *= num;
            }
            result += five;
        }
        System.out.println(result);
    }
}
