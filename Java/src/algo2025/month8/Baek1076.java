package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek1076 {

    static String[] colors = new String[]{"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        long result = 0;
        for (int i = 0; i < 3; i++) {
            String color = br.readLine();
            for (int j = 0; j < 10; j++) {
                if (i < 2 && colors[j].equals(color)) {
                    sb.append(j);
                    break;
                }
                if (i == 2 && colors[j].equals(color)) {
                    long n = Long.parseLong(String.valueOf(sb));
                    for (int k = 1; k <= j; k++) {
                        n *= 10;
                    }
                    result = n;
                }
            }
        }

        System.out.println(result);
    }
}
