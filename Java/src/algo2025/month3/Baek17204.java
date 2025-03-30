package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek17204 {

    static int[] graph;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        graph = new int[n];
        for (int i=0; i<n; i++) {
            graph[i] = Integer.parseInt(br.readLine());
        }
        if (graph[0] == 0) {
            System.out.println(-1);
        } else {
            int result = -1;
            for (int i=1; i<n; i++) {
                if (traversal(i, k)) {
                    result = i;
                    break;
                }
            }
            System.out.println(result);
        }
    }
    static boolean traversal(int number, int target) {
        int count = 1;
        int next = graph[0];

        while (count <= number) {
            if (count == number) {
                if (next == target) {
                    return true;
                }
                break;
            }
            next = graph[next];
            count++;
        }

        return false;
    }
}
