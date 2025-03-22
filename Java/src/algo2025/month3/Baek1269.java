package algo2025.month3;

import java.io.*;
import java.util.*;

public class Baek1269 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int aN = Integer.parseInt(st.nextToken());
        int bN = Integer.parseInt(st.nextToken());

        Set<Integer> aSet = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < aN; i++) {
            aSet.add(Integer.parseInt(st.nextToken()));
        }

        st = new StringTokenizer(br.readLine());
        int count = 0;
        for (int i = 0; i < bN; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (aSet.contains(num)) {
                aSet.remove(num);
            } else {
                count++;
            }
        }
        count += aSet.size();
        System.out.println(count);
    }
}
