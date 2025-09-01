package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek2460 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int maximum = 0;
        int counter = 0;
        for (int i = 0; i < 10; i++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int on = Integer.parseInt(st.nextToken());

            counter -= left;
            counter += on;

            maximum = Math.max(maximum, counter);
        }

        System.out.println(maximum);
    }
}
