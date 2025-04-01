package algo2025.month4;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.*;
import java.util.List;
import javax.swing.Timer;

public class RouletteSwing extends JFrame {
    private final String[] menu = {
            "그냥살기", "고추바사삭", "후참후라이드",
            "고추마요", "회", "맘터"
    };

    private final Map<String, Integer> countMap = new LinkedHashMap<>();

    private JTextField inputField;
    private JButton startButton;
    private JLabel topMenuLabel;
    private JPanel centerPanel;
    private Timer timer;
    private int remainingRuns = 0;

    public RouletteSwing() {
        setTitle("룰렛 메뉴 추천기");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 450);
        setLayout(new BorderLayout());

        // 초기화
        for (String item : menu) {
            countMap.put(item, 0);
        }

        // 1위 메뉴 표시 라벨
        topMenuLabel = new JLabel("현재 1위: 없음");
        topMenuLabel.setFont(new Font("맑은 고딕", Font.BOLD, 18));
        topMenuLabel.setHorizontalAlignment(SwingConstants.CENTER);
        add(topMenuLabel, BorderLayout.NORTH);

        // 메뉴 출력 패널
        centerPanel = new JPanel();
        centerPanel.setLayout(new BoxLayout(centerPanel, BoxLayout.Y_AXIS));
        add(centerPanel, BorderLayout.CENTER);
        updateMenuDisplay(); // 초기화 시 메뉴 출력

        // 하단 입력 필드 + 버튼
        JPanel bottomPanel = new JPanel();
        inputField = new JTextField(5);
        inputField.setFont(new Font("맑은 고딕", Font.PLAIN, 16));
        inputField.setText("100");

        startButton = new JButton("자동 돌리기 ▶");
        startButton.setFont(new Font("맑은 고딕", Font.BOLD, 16));
        startButton.addActionListener(e -> startRolling());

        bottomPanel.add(new JLabel("횟수: "));
        bottomPanel.add(inputField);
        bottomPanel.add(startButton);
        add(bottomPanel, BorderLayout.SOUTH);

        setLocationRelativeTo(null);
        setVisible(true);
    }

    private void startRolling() {
        try {
            int count = Integer.parseInt(inputField.getText().trim());
            if (count <= 0) {
                JOptionPane.showMessageDialog(this, "횟수는 1 이상이어야 합니다.");
                return;
            }

            remainingRuns = count;
            startButton.setEnabled(false);
            inputField.setEnabled(false);

            Random random = new Random();

            timer = new Timer(200, new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    String selected = menu[random.nextInt(menu.length)];
                    countMap.put(selected, countMap.get(selected) + 1);

                    updateMenuDisplay(); // 정렬 & 갱신
                    updateTopMenu();     // 1위 갱신

                    remainingRuns--;
                    if (remainingRuns <= 0) {
                        timer.stop();
                        startButton.setEnabled(true);
                        inputField.setEnabled(true);
                    }
                }
            });
            timer.start();

        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this, "숫자를 입력해주세요.");
        }
    }

    // 🏆 현재 1위 메뉴 계산 및 표시
    private void updateTopMenu() {
        String topItem = null;
        int maxCount = -1;

        for (Map.Entry<String, Integer> entry : countMap.entrySet()) {
            if (entry.getValue() > maxCount) {
                topItem = entry.getKey();
                maxCount = entry.getValue();
            }
        }

        if (topItem != null) {
            topMenuLabel.setText("현재 1위: " + topItem + " (" + maxCount + "회)");
        }
    }

    // 메뉴 정렬 & 순위 출력
    private void updateMenuDisplay() {
        centerPanel.removeAll();

        List<Map.Entry<String, Integer>> sortedList = new ArrayList<>(countMap.entrySet());
        sortedList.sort((a, b) -> b.getValue() - a.getValue()); // 내림차순

        int rank = 1;
        for (Map.Entry<String, Integer> entry : sortedList) {
            String text = rank + ". " + entry.getKey() + ": " + entry.getValue();
            JLabel label = new JLabel(text);
            label.setFont(new Font("맑은 고딕", Font.PLAIN, 16));

            // 순위에 따라 스타일 다르게
            if (rank == 1) {
                label.setFont(label.getFont().deriveFont(Font.BOLD));
            } else if (rank == 2) {
                label.setFont(label.getFont().deriveFont(Font.BOLD));
            } else if (rank == 3) {
                label.setFont(label.getFont().deriveFont(Font.BOLD));
            }

            centerPanel.add(label);
            centerPanel.add(Box.createVerticalStrut(16));
            rank++;
        }

        centerPanel.revalidate();
        centerPanel.repaint();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(RouletteSwing::new);
    }
}