package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek14654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int N = Integer.parseInt(br.readLine());

        int[] aTeam = new int[N];
        int[] bTeam = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            aTeam[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            bTeam[i] = Integer.parseInt(st.nextToken());
        }

        int aW = 0;
        int bW = 0;
        int mW = 0;

        for (int i = 0; i < N; i++) {
            if (fight(aTeam[i], bTeam[i]) > 0) {
                aW++;
                bW = 0;
            } else if (fight(aTeam[i], bTeam[i]) < 0) {
                bW++;
                aW = 0;
            } else {
                if (aW == 0) {
                    aW++;
                    bW = 0;
                } else {
                    bW++;
                    aW = 0;
                }
            }
            mW = Math.max(mW, Math.max(aW, bW));
        }

        System.out.println(mW);
    }

    // 1: a 0: tie -1: b
    private static int fight(int a, int b) {
        if (a == b) return 0;
        // (가위→보), (바위→가위), (보→바위)
        if ((a == 1 && b == 3) ||
            (a == 2 && b == 1) ||
            (a == 3 && b == 2)) {
            return 1;
        }
        return -1;
    }
}
