package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1002 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        int tc = T;
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        while (tc-- > 0) {
            st = new StringTokenizer(br.readLine());
            int[] coords = new int[6];
            for (int i=0; i<6; i++) {
                coords[i] = Integer.parseInt(st.nextToken());
            }

            int result = 0;

            double dist = Math.sqrt(Math.pow(coords[0] - coords[3], 2) + Math.pow(coords[1] - coords[4], 2));
            double rAdd = coords[2] + coords[5];
            double rDiff = Math.abs(coords[2] - coords[5]);

            // 완전히 겹침
            if (Double.compare(dist, 0) == 0 && coords[2] == coords[5]) {
                result = -1;
            }
            // 두 점에서 만남
            else if (Double.compare(dist, rDiff) > 0 && Double.compare(dist, rAdd) < 0) {
                result = 2;
            }
            // 한 점에서 만남 (외접 또는 내접)
            else if (Double.compare(dist, rAdd) == 0 || Double.compare(dist, rDiff) == 0) {
                result = 1;
            }
            // 만나지 않음 (멀리 떨어짐 / 한 원이 안에 있음)
            else {
                result = 0;
            }
            sb.append(result).append("\n");
        }

        System.out.println(sb);
    }
}
