public class DES {
    public static void main(String[] args) {

        // placeholder -1 so index starts at 1
        int[] initial = {-1, 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64,
                56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29,
                21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7};

        // placeholder -1 so index starts at 1
        int[] binary = {-1,
                1, 0, 1, 0,
                1, 1, 0, 1,
                0, 1, 0, 1,
                0, 1, 1, 0,
                1, 1, 0, 0,
                1, 0, 0, 1,
                1, 1, 0, 1,
                1, 0, 1, 0,
                1, 0, 0, 1,
                0, 0, 0, 1,
                1, 0, 1, 1,
                1, 0, 1, 1,
                0, 0, 0, 1,
                1, 0, 0, 1,
                1, 0, 1, 1,
                1, 0, 1, 0};

        // size 65 because of placeholder 1
        int[] newBinary = new int[64 + 1];


        // start at 1 to skip over placeholder
        for (int i = 1; i < binary.length; i++) {
            if(binary[i] == 1) {
                int index = find(initial, i);
                System.out.println("looking for " + i + " ---> " + i + " has been found at " + index);
                newBinary[index] = 1;
            }

        }

        // start at 1 to skip over placeholder
        for(int i = 1; i < newBinary.length; i++) {
            System.out.print(newBinary[i] + " ");
            if(i % 4 == 0) {
                System.out.print("    ");
            }
        }
    }

    // start at 1 to skip over placeholder
    public static int find(int[] array, int n) {
        for(int i = 1; i < array.length; i++) {
            if(array[i] == n) {
                return i;
            }
        }
        return -1;
    }
}

