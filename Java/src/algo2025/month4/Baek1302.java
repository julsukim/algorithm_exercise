package algo2025.month4;

import java.io.*;
import java.util.*;

public class Baek1302 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Map<String, Integer> books = new HashMap<>();
        for (int i=0; i<N; i++) {
            String name = br.readLine();
            books.put(name, books.getOrDefault(name, 0) + 1);
        }

        int maxCount = 0;
        String maxName = "";

        for (Map.Entry<String, Integer> entry : books.entrySet()) {
            String name = entry.getKey();
            Integer count = entry.getValue();

            if (count > maxCount || (count == maxCount && name.compareTo(maxName) < 0)) {
                maxName = name;
                maxCount = count;
            }
        }

        System.out.println(maxName);
    }
}
