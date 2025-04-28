package algo2025.month4;

import java.util.*;

public class SortTest {
    public static void main(String[] args) {
        List<int[]> list = new ArrayList<>();
        list.add(new int[]{0, 1});
        list.add(new int[]{0, 2});
        list.add(new int[]{1, 0});
        list.add(new int[]{2, 0});
        list.add(new int[]{2, 1});
        list.add(new int[]{0, 0});
        list.add(new int[]{2, 2});
        list.add(new int[]{1, 2});

        list.sort((a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(a[1], b[1]);
            }
            return Integer.compare(a[0], b[0]);
        });

        System.out.println(Arrays.toString(list.get(0)));
    }
}
