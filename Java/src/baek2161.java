import java.io.*;
import java.util.*;

public class baek2161 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());

        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            queue.offer(i);
        }

        StringBuilder sb = new StringBuilder();
        while (queue.size() > 1) {
            sb.append(queue.poll()).append(" ");
            queue.offer(queue.poll());
        }

        sb.append(queue.poll());
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }

}
