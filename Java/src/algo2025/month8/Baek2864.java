package algo2025.month8;

import java.io.*;
import java.util.*;

public class Baek2864 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String A = st.nextToken();
        String B = st.nextToken();

        int minA = Integer.parseInt(A.replace('6', '5'));
        int minB = Integer.parseInt(B.replace('6', '5'));
        int minSum = minA + minB;

        int maxA = Integer.parseInt(A.replace('5', '6'));
        int maxB = Integer.parseInt(B.replace('5', '6'));
        int maxSum = maxA + maxB;

        System.out.println(minSum + " " + maxSum);
    }
}
