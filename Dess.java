package DES;

public class Dess {

	int[] initial = { 58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64,
	        56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29,
	        21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7};
	int[] finalPermutation = {40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45,
            13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41,
            9, 49, 17, 57, 25};
	// HOMEWORK PROBLEM
//	int[] binary = {
//	        1, 0, 1, 0,
//	        1, 1, 0, 1,
//	        0, 1, 0, 1,
//	        0, 1, 1, 0,
//	        1, 1, 0, 0,
//	        1, 0, 0, 1,
//	        1, 1, 0, 1,
//	        1, 0, 1, 0,
//	        1, 0, 0, 1,
//	        0, 0, 0, 1,
//	        1, 0, 1, 1,
//	        1, 0, 1, 1,
//	        0, 0, 0, 1,
//	        1, 0, 0, 1,
//	        1, 0, 1, 1,
//	        1, 0, 1, 0};
	
	// this is the example of  0000 0080 0000 0002
	 int[] binary = {
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             1, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 0, 0,
             0, 0, 1, 0};
	
	// this is example 0002 0000 0000 0001
//	 int[] binary = {
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 1, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 0,
//             0, 0, 0, 1};
	
	int[] roundOne = new int[64];
	
	public Dess() {
		newBinary();
		printBinary(roundOne);
	}
	
	public static void main(String[] args) {
		Dess des = new Dess();
	}
	
	private void newBinary() {
		for(int i = 0; i < binary.length; i++) {
			if(binary[i] == 1) {
				int index = 
						/*
						 * Use the initial Permutation
						 * to find the output of the 
						 * final Permutation
						 */
						initial[i] - 1;
						
						/*
						 * Use the Final Permutation
						 * to find the output of the
						 * initial Permeation
						 */
						//finalPermutation[i] - 1;
						
				System.out.println("INDEX: " + index);
				roundOne[index] = 1;
			}
		}
	}
	
	private void printBinary(int[] binary) {
		
		for(int i = 0; i < binary.length; i++) {
			if(i % 4 == 0) {
				System.out.print(" ");
			}
			System.out.print(binary[i]);
		}
	}
}
