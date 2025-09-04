package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek2914 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken());
        int I = Integer.parseInt(st.nextToken());
        int x = A * (I - 1) + 1;
        System.out.println(x);
    }
}
