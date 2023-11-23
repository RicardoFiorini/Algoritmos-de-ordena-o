import java.util.ArrayList;
import java.util.List;

public class RadixSort {
    public static List<Integer> radixSort(List<Integer> arr) {
        int maxDigit = getMaxDigit(arr);

        for (int i = 0; i < maxDigit; i++) {
            List<List<Integer>> buckets = new ArrayList<>(10);

            // Inicializa os baldes
            for (int j = 0; j < 10; j++) {
                buckets.add(new ArrayList<>());
            }

            // Distribui os elementos nos baldes
            for (int num : arr) {
                int digit = (num / (int) Math.pow(10, i)) % 10;
                buckets.get(digit).add(num);
            }

            // Ordena cada balde e concatena
            arr.clear();
            for (List<Integer> bucket : buckets) {
                arr.addAll(bucket);
            }
        }

        return arr;
    }

    private static int getMaxDigit(List<Integer> arr) {
        int maxDigit = 0;
        for (int num : arr) {
            int digitCount = (int) Math.log10(num) + 1;
            maxDigit = Math.max(maxDigit, digitCount);
        }
        return maxDigit;
    }

    public static void main(String[] args) {
        List<Integer> arr = List.of(170, 45, 75, 90, 802, 24, 2, 66);
        List<Integer> result = radixSort(arr);
        System.out.println(result);
    }
}
