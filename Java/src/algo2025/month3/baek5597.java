package algo2025.month3;

import java.io.*;
import java.util.*;

public class baek5597 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        boolean[] checklist = new boolean[30];

        for (int i=0; i<28; i++) {
            int num = Integer.parseInt(br.readLine());
            checklist[num-1] = true;
        }

        for (int i=0; i<30; i++) {
            if (!checklist[i]) {
                System.out.println(i+1);
            }
        }
    }
}
