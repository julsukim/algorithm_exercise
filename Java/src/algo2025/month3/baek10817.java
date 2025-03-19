package algo2025.month3;

import java.io.*;
import java.util.*;

public class baek10817 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
//        int a = Integer.parseInt(input[0]);
//        int b = Integer.parseInt(input[1]);
//        int c = Integer.parseInt(input[2]);
//
//        List<Integer> list = new ArrayList<>();
//        list.add(a);
//        list.add(b);
//        list.add(c);
//        Collections.sort(list);

        int[] nums = new int[3];
        for (int i=0; i<3; i++) {
            nums[i] = Integer.parseInt(input[i]);
        }

        Arrays.sort(nums);
        System.out.println(nums[1]);
    }

}
