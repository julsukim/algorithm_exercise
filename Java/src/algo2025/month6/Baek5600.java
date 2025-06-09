package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek5600 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int M = a + b + c;

        int N = Integer.parseInt(br.readLine());
        int[] p = new int[N], q = new int[N], r = new int[N], res = new int[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            p[i] = Integer.parseInt(st.nextToken());
            q[i] = Integer.parseInt(st.nextToken());
            r[i] = Integer.parseInt(st.nextToken());
            res[i] = Integer.parseInt(st.nextToken());
        }

        int[] state = new int[M + 1];
        Arrays.fill(state, 2);

        for (int i = 0; i < N; i++) {
            if (res[i] == 1) {
                state[p[i]] = 1;
                state[q[i]] = 1;
                state[r[i]] = 1;
            }
        }

        boolean changed;
        do {
            changed = false;
            for (int i = 0; i < N; i++) {
                if (res[i] == 0) {
                    int cntGood = 0, cntUnknown = 0, unkIdx = -1;
                    int[] parts = {p[i], q[i], r[i]};
                    for (int part : parts) {
                        if (state[part] == 1) cntGood++;
                        else if (state[part] == 2) {
                            cntUnknown++;
                            unkIdx = part;
                        }
                    }
                    if (cntGood == 2 && cntUnknown == 1) {
                        state[unkIdx] = 0;
                        changed = true;
                    }
                }
            }
        } while (changed);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= M; i++) {
            sb.append(state[i] + "\n");
        }
        System.out.println(sb);
    }
}
