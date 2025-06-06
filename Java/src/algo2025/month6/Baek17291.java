package algo2025.month6;

import java.io.*;
import java.util.*;

public class Baek17291 {

    private static List<Bug> bugs;
    private static Queue<Bug> birthBugs;
    private static int aliveBugsCount;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        bugs = new ArrayList<>();
        bugs.add(new Bug(1));
        birthBugs = new ArrayDeque<>();
        aliveBugsCount = 1;

        for (int i = 2; i <= N; i++) {
            for (Bug b : bugs) {
                b.act(i);
            }
            while (!birthBugs.isEmpty()) bugs.add(birthBugs.poll());
        }

        System.out.println(aliveBugsCount);
    }

    private static class Bug {
        boolean isOdd;
        boolean isDead;
        int splitCount;

        public Bug(int year) {
            if (year % 2 == 1) {
                isOdd = true;
            } else {
                isOdd = false;
            }
            isDead = false;
            splitCount = 0;
        }

        public void act(int year) {
            if (isDead) return;

            split(year);

            if (isOdd) {
                if (splitCount == 3) die();

            } else {
                if (splitCount == 4) die();
            }
        }

        private void split(int year) {
            splitCount++;
            birthBugs.add(new Bug(year));
            aliveBugsCount++;
        }

        private void die() {
            aliveBugsCount--;
            isDead = true;
        }
    }
}
