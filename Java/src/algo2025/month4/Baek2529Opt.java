package algo2025.month4;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Baek2529Opt {
    static int k;
    static String[] signs;
    static boolean[] used = new boolean[10];
    static String min = null;
    static String max = null;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        k = Integer.parseInt(br.readLine());
        signs = new String[k];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            signs[i] = st.nextToken();
        }

        dfs(0, "");

        System.out.println(max);
        System.out.println(min);
    }

    static void dfs(int depth, String number) {
        if (depth == k + 1) {
            if (min == null || number.compareTo(min) < 0) {
                min = number;
            }
            if (max == null || number.compareTo(max) > 0) {
                max = number;
            }
            return;
        }

        for (int i = 0; i <= 9; i++) {
            if (!used[i]) {
                if (depth == 0 || isValid(number.charAt(depth - 1) - '0', i, signs[depth - 1])) {
                    used[i] = true;
                    dfs(depth + 1, number + i);
                    used[i] = false;
                }
            }
        }
    }

    static boolean isValid(int a, int b, String op) {
        if (op.equals("<")) return a < b;
        else return a > b;
    }
}
