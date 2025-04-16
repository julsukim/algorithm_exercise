package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1008 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        double A = Double.parseDouble(st.nextToken());
        double B = Double.parseDouble(st.nextToken());
        double div = A / B;
        System.out.printf("%.9f", div);
    }
}
