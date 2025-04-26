package algo2025.month4;

import java.io.*;

public class Baek28702 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = new String[3];
        for (int i = 0; i < 3; i++) {
            arr[i] = br.readLine();
        }

        Integer start = null;
        for (int i = 0; i < 3; i++) {
            if (isNumber(arr[i])) {
                int num = Integer.parseInt(arr[i]);
                // 몇 번째 출력인지는 i를 이용해 보정
                start = num - i;
                break;
            }
        }

        if (start == null) {
            // 숫자가 하나도 없으면 1부터 brute-force
            start = findStartNumber(arr);
        }

        int next = start + 3;
        System.out.println(fizzBuzz(next));
    }

    static boolean isNumber(String s) {
        for (char c : s.toCharArray()) {
            if (!Character.isDigit(c)) return false;
        }
        return true;
    }

    static int findStartNumber(String[] arr) {
        for (int candidate = 1; candidate <= 10000; candidate++) {
            boolean match = true;
            for (int i = 0; i < 3; i++) {
                if (!fizzBuzz(candidate + i).equals(arr[i])) {
                    match = false;
                    break;
                }
            }
            if (match) return candidate;
        }
        return -1; // 나올 일 없음
    }

    static String fizzBuzz(int n) {
        if (n % 15 == 0) return "FizzBuzz";
        if (n % 3 == 0) return "Fizz";
        if (n % 5 == 0) return "Buzz";
        return String.valueOf(n);
    }
}
