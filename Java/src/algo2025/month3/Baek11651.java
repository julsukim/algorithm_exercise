package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek11651 {

    static class Coord implements Comparable<Coord> {
        int x, y;

        public Coord(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public int compareTo(Coord other) {
            int result = Integer.compare(y, other.y);
            if (result == 0) {
                result = Integer.compare(x, other.x);
            }
            return result;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Coord[] coords = new Coord[n];
        StringTokenizer st;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            coords[i] = new Coord(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(coords);
        StringBuilder sb = new StringBuilder();
        for (Coord c : coords) {
            sb.append(c.x).append(" ").append(c.y).append("\n");
        }
        System.out.println(sb.toString());
    }
}
