import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class BucketSort {
    public static List<Double> bucketSort(List<Double> arr) {
        int bucketSize = 5;
        List<List<Double>> buckets = new ArrayList<>(bucketSize);

        // Inicializa os baldes
        for (int i = 0; i < bucketSize; i++) {
            buckets.add(new ArrayList<>());
        }

        // Distribui os elementos nos baldes
        for (double element : arr) {
            int index = (int) (element * bucketSize);
            buckets.get(index).add(element);
        }

        // Ordena cada balde e concatena
        List<Double> sortedArray = new ArrayList<>();
        for (List<Double> bucket : buckets) {
            Collections.sort(bucket);
            sortedArray.addAll(bucket);
        }

        return sortedArray;
    }

    public static void main(String[] args) {
        List<Double> arr = List.of(0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51);
        List<Double> result = bucketSort(arr);
        System.out.println(result);
    }
}
