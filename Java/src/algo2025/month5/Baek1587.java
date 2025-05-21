package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek1587 {

    private static int nA, nB, M;
    private static int[][] edges;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        nA = Integer.parseInt(st.nextToken());
        nB = Integer.parseInt(st.nextToken());

        M = Integer.parseInt(br.readLine());
        edges = new int[M][2];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            edges[i][0] = Integer.parseInt(st.nextToken());
            edges[i][1] = Integer.parseInt(st.nextToken());
        }

        int result = 0;
        if (nA % 2 == 1 && nB % 2 == 1) {
            for (int i = 0; i < M; i++) {
                int a = edges[i][0];
                int b = edges[i][1];

                if (checkEdges(a, nA) && checkEdges(b, nB)) {
                    result++;
                    break;
                }
            }
        }
        result += nA/2 + nB/2;
        System.out.println(result);
    }

    private static boolean checkEdges(int v, int e) {
        if ((v - 1) % 2 == 0 && (e - v) % 2 == 0) {
            return true;
        }
        return false;
    }
}
