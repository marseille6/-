public class InsertSort {
    public int[] arr;
    public InsertSort(int[] arr) {
        this.arr = arr;
    }
    public int []main() {
        for (int j = 1; j < this.arr.length; j++) {
            int i = j - 1;
            int key = this.arr[j];
            while(i >= 0 && key < this.arr[i]) {
                this.arr[i + 1] = this.arr[i];
                i--;
            }
            this.arr[i+1] = key;
        }
        return this.arr;
    }
    public static void main(String[] args) {
        int A[] = {3,5,1,2,8,0,12,47};
        InsertSort Insert = new InsertSort(A);
        System.out.println(Arrays.toString(Insert.main()));
    }
}