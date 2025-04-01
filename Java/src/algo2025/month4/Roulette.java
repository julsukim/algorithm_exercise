package algo2025.month4;

import java.util.*;

public class Roulette {
    public static void main(String[] args) throws InterruptedException {
        String[] arr = {
                "그냥살기", "고추바사삭", "후참후라이드",
                "고추마요", "회", "맘터", "스모크"
        };

        Map<String, Integer> map = new HashMap<>();
        for (String str: arr) {
            map.put(str, 0);
        }

        Random random = new Random();

        for (int i = 0; i < 100; i++) { // 100번 반복 (필요하면 늘려도 됨)
            String selected = arr[random.nextInt(arr.length)];
            map.put(selected, map.get(selected) + 1);

            // 화면 지우는 효과 (콘솔마다 다를 수 있음)
            System.out.print("\033[H\033[2J"); // ANSI escape code
            System.out.flush();

            for (Map.Entry<String, Integer> entry : map.entrySet()) {
                System.out.println(entry.getKey() + ": " + entry.getValue());
            }

            Thread.sleep(10); // 100ms 대기 (0.1초)
        }

        System.out.println("\n🎉 가장 많이 나온 메뉴는?");
        map.entrySet().stream()
                .max(Map.Entry.comparingByValue())
                .ifPresent(e -> System.out.println(e.getKey() + " (" + e.getValue() + "회)"));
    }
}
