import java.util.*;

public class prac_java {


	public static void main(String[] args) {
//게임
		int com_num = (int)(Math.random()*100+1);
		int num;
		Scanner t = new Scanner(System.in);
		int try_num = 0;
		while(true) {
			System.out.println("숫자를 입력하세요.(1~100)");
			num = t.nextInt();
			if(num>com_num) {
				System.out.println("입력한 숫자가 정해진 숫자보다 높습니다.");
				try_num++;
			}
			else if(num<com_num) {
				System.out.println("입력한 숫자가 정해진 숫자보다 낮습니다.");
				try_num++;
			}
			else {
				System.out.println("정답입니다.");
				break;
			}
		}
		System.out.println("시도한 횟수는 "+try_num+"입니다.");
		if(try_num > 6) System.out.println("바보입니까?");
		else if(try_num <7)System.out.println("평범하네요");
		else if(try_num <4)System.out.println("운이 좋았네요");
		
		
//원주율	
//		Scanner t = new Scanner(System.in);
//		System.out.println("반복할 횟수를 입력하세요");
//		int try_num = t.nextInt();
//		double pi = 0,temp;
//		for(int i=0;i<try_num;i++) {
//			temp = 4.0/(2*i +1);
//			if(i % 2 == 1) {
//				temp = -1 *temp;
//			}
//			pi += temp;
//		}
//		System.out.println("원주율은 "+pi+"입니다.");
	}

}
