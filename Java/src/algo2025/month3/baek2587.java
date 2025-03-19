package algo2025.month3;

import java.io.*;
import java.util.*;

public class baek2587 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] nums = new int[5];
        for (int i=0; i<5; i++) {
            nums[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(nums);

//        int sum = 0;
//        for (int num : nums) {
//            sum += num;
//        }

        int sum = Arrays.stream(nums).sum();

        System.out.println(sum / 5);
        System.out.println(nums[2]);
    }

}
