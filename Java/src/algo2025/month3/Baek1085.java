package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek1085 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        int min = 0;
        min = Math.min(Math.abs(x - w), Math.abs(x));
        min = Math.min(min, Math.min(Math.abs(y - h), Math.abs(y)));
        System.out.println(min);
    }
}
