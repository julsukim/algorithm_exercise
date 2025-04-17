package algo2025.month4;

import java.util.Arrays;

public class CopyBenchmark {
    public static void main(String[] args) {
        int[] original = new int[10_000_000];
        for (int i = 0; i < original.length; i++) {
            original[i] = i;
        }

        int from = 100_000;
        int to = 8_000_000;
        int newLength = to - from;

        long start, end;

        // 1. System.arraycopy
        start = System.nanoTime();
        int[] sysCopy = new int[newLength];
        System.arraycopy(original, from, sysCopy, 0, newLength);
        end = System.nanoTime();
        System.out.println("System.arraycopy: " + (end - start) / 1_000_000.0 + " ms");

        // 2. Arrays.copyOfRange
        start = System.nanoTime();
        int[] rangeCopy = Arrays.copyOfRange(original, from, to);
        end = System.nanoTime();
        System.out.println("Arrays.copyOfRange: " + (end - start) / 1_000_000.0 + " ms");

        // 3. 수동 for 루프
        start = System.nanoTime();
        int[] manualCopy = new int[newLength];
        for (int i = 0; i < newLength; i++) {
            manualCopy[i] = original[from + i];
        }
        end = System.nanoTime();
        System.out.println("Manual for loop: " + (end - start) / 1_000_000.0 + " ms");
    }
}

