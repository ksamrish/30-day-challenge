import java.util.Scanner;
public class Smallest_of_all {

	public int smallest_in_the_array(int[] array) {
		int smallest = array[0];
		for(int i=1;i<array.length;i++) {
			if(array[i]<smallest) {
				smallest = array[i];
			}
		}
		return smallest;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] array = new int[n];
		for(int i = 0;i<n;i++) 
		{
			int value = sc.nextInt();
			array[i] = value;
		}
		Smallest_of_all obj = new Smallest_of_all();
		System.out.println(obj.smallest_in_the_array(array));
	}

}
