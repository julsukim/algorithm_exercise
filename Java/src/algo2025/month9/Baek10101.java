package algo2025.month9;

import java.io.*;
import java.util.*;

public class Baek10101 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());

        boolean isE = A == 60 && B == 60 && C == 60;
        boolean isI = (A + B + C) == 180 && ((A == B) || (B == C) || (A == C));
        boolean isS = (A + B + C) == 180 && ((A != B) && (B != C) && (A != C));
        boolean isEr = (A + B + C) != 180;

        if (isE) {
            System.out.println("Equilateral");
        } else if (isI) {
            System.out.println("Isosceles");
        } else if (isS) {
            System.out.println("Scalene");
        } else if (isEr) {
            System.out.println("Error");
        }
    }
}
