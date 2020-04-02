import java.util.Scanner;
public class Compare_triplets {

	public int[] comparetriplets(int[] array1,int[] array2,int[] array3) {
		int a=0,b=0;
		for(int i=0;i<array1.length;i++) {
			if(array1[i]>array2[i]) {
				a++;
			}
			else if(array1[i]<array2[i]) {
				b++;
			}
		}
		array3[0] = a;
		array3[1] = b;
		return array3;
	}

	public static void main(String[] args) {
		int[] array1 = new int[3];
		int[] array2 = new int[3];
		int[] array3 = new int[2]; 
		Scanner sc = new Scanner(System.in);
		for(int i=0;i<array1.length;i++) {
			int value = sc.nextInt();
			array1[i] = value;
		}
		for(int i=0;i<array2.length;i++) {
			int value = sc.nextInt();
			array2[i] = value;
		}
		Compare_triplets obj = new Compare_triplets();
		obj.comparetriplets(array1, array2,array3);
		for(int i=0;i<array3.length;i++) {
			System.out.print(array3[i]+" ");
		}
	}

}
