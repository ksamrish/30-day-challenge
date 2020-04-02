import java.util.Scanner;
public class Pattern_upper_triangle {

	public void pattern(int n) {
		
		for(int i=0;i<(n/2)+1;i++) {
			for(int j=n/2;j>i;j--) {
				System.out.print(" ");
			}
			for(int j=0;j<i*2+1;j++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		Pattern_upper_triangle obj = new Pattern_upper_triangle();
		obj.pattern(n);
	}

}
