package algo2025.month3;

import java.util.*;

public class SetPractice {

    public static void main(String[] args) {
        Set<String> animals = new LinkedHashSet<>();

        animals.add("Cow");
        animals.add("Dog");
        animals.add("Cat");
        animals.add("Bat");

        for (String animal : animals) {
            System.out.println(animal);
        }

        System.out.println("------");

        Set<String> animals2 = new TreeSet<>(animals);

        for (String animal : animals2) {
            System.out.println(animal);
        }

        System.out.println("------");

        Iterator<String> animalsIterator = animals.iterator();
        while (animalsIterator.hasNext()) {
            System.out.println(animalsIterator.next());
        }

        System.out.println("------");

        Set<String> animals3 = new HashSet<>(animals);
        animals3.stream().filter(animal -> animal.startsWith("C")).forEach(System.out::println);
    }

}
