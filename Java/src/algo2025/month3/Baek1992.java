package algo2025.month3;

import java.io.*;

public class Baek1992 {

    static int[][] data;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        data = new int[n][n];
        for (int i=0; i<n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                data[i][j] = line.charAt(j) - '0';
            }
        }
        System.out.println(compress(0, 0, n));
    }

    static String compress(int x, int y, int size) {
        if (isSame(x, y, size)) {
            return String.valueOf(data[x][y]); // 모두 같으면 0 또는 1 반환
        }

        int newSize = size / 2;

        StringBuilder sb = new StringBuilder();
        sb.append("(");
        sb.append(compress(x, y, newSize));
        sb.append(compress(x, y + newSize, newSize));
        sb.append(compress(x + newSize, y, newSize));
        sb.append(compress(x + newSize, y + newSize, newSize));
        sb.append(")");

        return sb.toString();
    }

    static boolean isSame(int x, int y, int size) {
        int val = data[x][y];
        for (int i=x; i < x + size; i++) {
            for (int j=y; j<y+size; j++ ) {
                if (data[i][j] != val) return false;
            }
        }
        return true;
    }
}
