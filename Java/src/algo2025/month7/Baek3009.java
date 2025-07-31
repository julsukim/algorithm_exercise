package algo2025.month7;

import java.io.*;
import java.util.*;

public class Baek3009 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] xs = new int[3];
        int[] ys = new int[3];
        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            xs[i] = x;
            ys[i] = y;
        }

        System.out.println(findUnique(xs) + " " + findUnique(ys));
    }

    public static int findUnique(int[] x) {
        if (x[0] == x[1]) return x[2];
        else if (x[0] == x[2]) return x[1];
        else return x[0];
    }
}
