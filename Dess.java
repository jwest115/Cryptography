package DES;

public class Dess {

	int[] initial = {58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64,
	        56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29,
	        21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7};

	int[] binary = {
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
				roundOne[initial[i] - 1] = 1;
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
