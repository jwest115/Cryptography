import java.util.ArrayList;

public class MultiplicativeInverse {
    public static void main(String[] args) {
//        findMultiplicativeInverses(6);
        extendedEuclidean(7, 6);
    }

    public static void extendedEuclidean(int n, int b) {
        int r1 = n;
        int r2 = b;
        int t1 = 0;
        int t2 = 1;

        while(r2 > 0) {
            int q = r1 / r2;
            System.out.println("q = " + q);
            int r = r1 - (q * r2);

            System.out.println("r = " + r);
            r1 = r2;
            r2 = r;

            System.out.println("r1 " + r1);
            System.out.println("r2 " + r2);
            int t = t1 - (q * t2);
            System.out.println(t1 + " - " + q + " * " + t2 + " = " + t);


            System.out.println("t " + t);
            t1 = t2;
            t2 = t;

            System.out.println("t1 = " + t1);
            System.out.println("t2 = " + t2);
        }
        if(r1 == 1) {
            System.out.print("inverse is " + t1);
        }
        else {
            System.out.print("there is no inverse");
        }
    }


    public static void findMultiplicativeInverses(int n) {
        int[][] array = new int[n][n];
        ArrayList<String> answer = new ArrayList<String>();
        for(int i = 0; i < n; i++) {
            array[i][1] = i;
            System.out.print(array[i][1]);
        }
        for(int i = 0; i < n; i++) {
            array[1][i] = i;
            System.out.println(array[1][i]);
        }

        for(int i = 2; i < n; i++) {
            int temp = i;
            for(int j = 2; j < n; j++) {
                array[i][j] = (temp += i) % n;
            }
        }

        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                System.out.print(array[i][j] + " ");
                if(array[i][j] == 1){
                    answer.add("Multiplication inverse pair (" + i + ", " + j + ")");
                }
            }
            System.out.println();
        }

        System.out.println();

        for(int i = 0; i < answer.size(); i++) {
            System.out.println(answer.get(i));
        }
    }
}
