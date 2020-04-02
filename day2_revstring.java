import java.util.Scanner;
public class Reverse_string {

	public void revstring(String str) {
		StringBuilder strrev = new StringBuilder();
		char temp;
		for(int i=str.length()-1;i>=0;i--) {
			temp = str.charAt(i);
			strrev.append(temp);
		}
		System.out.println(strrev);
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		Reverse_string obj = new Reverse_string();
		obj.revstring(str);
	}

}
