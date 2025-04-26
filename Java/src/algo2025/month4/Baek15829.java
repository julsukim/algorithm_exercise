package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek15829 {

    static final long M = 1_234_567_891L;
    static final long r = 31L;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int L = Integer.parseInt(br.readLine());
        char[] charArr = br.readLine().toCharArray();

        long answer = 0L;
        long pow = 1L;

        for (int i=0; i<L; i++) {
            int value = charArr[i] - 'a' + 1;
            answer = (answer + (value * pow) % M) % M;
            pow = (pow * r) % M;
        }

        System.out.println(answer);
    }
}
