package algo2025.month3;

import java.io.*;

public class Baek9081 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int tc = 0; tc < t; tc++) {
            sb.append(nextPermutation(br.readLine())).append("\n");
        }
        System.out.print(sb);
    }

    static String nextPermutation(String str) {
        char[] arr = str.toCharArray();

        int i = arr.length - 2;
        // 뒤에서부터 오름차순이 깨지는 지점 찾기
        while (i >= 0 && arr[i] >= arr[i+1]) {
            i--;
        }

        // 마지막 단어(순열)
        if (i < 0) return str;

        // 오름차순이 깨지는 지점이 있음
        int j = arr.length - 1;
        // arr[i]보다 큰 수 중 가장 작은 수 찾기
        while (arr[j] <= arr[i]) {
            j--;
        }

        // 스왑
        char tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;

        // i 이후를 오름차순 정렬 (reverse)
        int left = i + 1, right = arr.length - 1;
        while (left < right) {
            char tmp2 = arr[left];
            arr[left] = arr[right];
            arr[right] = tmp2;
            left++;
            right--;
        }

        return new String(arr);
    }
}
