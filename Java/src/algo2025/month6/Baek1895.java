package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek1895 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        short R = Short.parseShort(st.nextToken());
        short C = Short.parseShort(st.nextToken());

        short[][] image = new short[R][C];
        for (short r = 0; r < R; r++) {
            st = new StringTokenizer(br.readLine());
            for (short c = 0; c < C; c++) {
                image[r][c] = Short.parseShort(st.nextToken());
            }
        }
        short T = Short.parseShort(br.readLine());

        short count = 0;

        short[] filter = new short[9];
        for (short r = 0; r < R-2; r++) {
            for (short c = 0; c < C-2; c++) {
                short idx = 0;
                for (short nr = r; nr <= r + 2; nr++) {
                    for (short nc = c; nc <= c + 2; nc++) {
                        filter[idx++] = image[nr][nc];
                    }
                }
                Arrays.sort(filter);
                if(filter[4] >= T) count++;
            }
        }

        System.out.println(count);
    }
}
