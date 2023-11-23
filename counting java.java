import java.util.Arrays;

public class CountingSort {
    public static int[] countingSort(int[] arr) {
        int max = Arrays.stream(arr).max().getAsInt();
        int[] count = new int[max + 1];

        // Conta as ocorrências de cada elemento
        for (int num : arr) {
            count[num]++;
        }

        // Calcula as posições corretas
        for (int i = 1; i <= max; i++) {
            count[i] += count[i - 1];
        }

        // Constrói a lista ordenada
        int[] sortedArray = new int[arr.length];
        for (int i = arr.length - 1; i >= 0; i--) {
            count[arr[i]]--;
            sortedArray[count[arr[i]]] = arr[i];
        }

        return sortedArray;
    }

    public static void main(String[] args) {
        int[] arr = {4, 2, 4, 1, 0, 2, 1};
        int[] result = countingSort(arr);
        System.out.println(Arrays.toString(result));
    }
}
