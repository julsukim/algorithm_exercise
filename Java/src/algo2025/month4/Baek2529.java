package algo2025.month4;

import java.util.*;

public class Baek2529 {
    static int k;
    static String[] signs;
    static boolean[] used = new boolean[10];
    static List<String> results = new ArrayList<>();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        k = sc.nextInt();
        signs = new String[k];
        for (int i = 0; i < k; i++) {
            signs[i] = sc.next();
        }

        backtrack(0, "");

        // 정렬해서 최댓값, 최솟값 출력
        Collections.sort(results);
        System.out.println(results.get(results.size() - 1)); // 최대값
        System.out.println(results.get(0)); // 최소값
    }

    static void backtrack(int depth, String number) {
        if (depth == k + 1) {
            results.add(number);
            return;
        }

        for (int i = 0; i <= 9; i++) {
            if (!used[i]) {
                if (depth == 0 || isValid(number.charAt(depth - 1) - '0', i, signs[depth - 1])) {
                    used[i] = true;
                    backtrack(depth + 1, number + i);
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

