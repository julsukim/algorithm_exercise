package algo2025.month5;

import java.io.*;
import java.util.*;

public class Baek12933 {

    private static final String quack = "quack";
    private static final Set<Character> soundSet = new HashSet<>(Arrays.asList('q', 'u', 'a', 'c', 'k'));

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String sound = br.readLine();
        int length = sound.length();

        List<Duck> ducks = new ArrayList<>();

        boolean isCorrectSound = true;
        for (int i = 0; i < length; i++) {
            char s = sound.charAt(i);

            if (!soundSet.contains(s)) {
                isCorrectSound = false;
                break;
            }

            boolean isFindMatchDuck = false;
            for (int d = 0; d < ducks.size(); d++) {
                if (ducks.get(d).checkAndAddSound(i, s)) {
                    isFindMatchDuck = true;
                    break;
                }
            }

            if (isFindMatchDuck) continue;

            if (s == 'q') {
                Duck duck = new Duck(length);
                duck.checkAndAddSound(i, s);
                ducks.add(duck);
            } else {
                isCorrectSound = false;
                break;
            }
        }

        for (Duck duck : ducks) {
            if (!duck.isCompleted) {
                isCorrectSound = false;
                break;
            }
        }

        if (!isCorrectSound) {
            System.out.println(-1);
        } else {
            System.out.println(ducks.size());
        }
    }

    private static class Duck {
        char[] sound;
        int idx;
        boolean isCompleted;

        public Duck(int length) {
            sound = new char[length];
            idx = 0;
            isCompleted = false;
        }

        public boolean checkAndAddSound(int i, char s) {
            if (quack.charAt(idx % 5) != s) {
                return false;
            }
            sound[i] = s;
            idx++;

            if (s == 'k') {
                isCompleted = true;
            } else {
                isCompleted = false;
            }
            return true;
        }
    }
}
