package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1085 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] borders = new int[4];
        for (int i=0; i<4; i++) {
            borders[i] = Integer.parseInt(st.nextToken());
        }

        int[] dist = new int[]{
                borders[0],
                borders[1],
                borders[2] - borders[0],
                borders[3] - borders[1]
        };

        Arrays.sort(dist);
        System.out.println(dist[0]);
    }
}
