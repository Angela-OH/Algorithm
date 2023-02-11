package test;
import java.util.Arrays;

public class question3 {
	public static int make_num(int digit) {
		int num = 0;
		for (int i = 0; i < digit; i++) {
			num += Math.pow(10, i);
		}
		return num;
	}
    public static int sum_digit(int num) {
        int sum = 0;
        String s = Integer.toString(num);
        for (int i = 0; i < s.length(); i++){
            sum += (int)(s.charAt(i) - '0');
        }
        return sum;
    }
	public static void main(String[] args) {
		 int n = 10, answer = 0;
		 String s = Integer.toString(n);
		 int sum = 0;
		 for (int i = 0; i<s.length(); i++) {
			 sum += (int)(s.charAt(i)-'0');
		 }
		 sum *= 2;
		 int digit_num = (int)((sum-1)/9) + 1;
		 System.out.println(digit_num);
		 int min_num = (int)Math.pow(10, digit_num - 1);
		 if (min_num < n)
			 min_num = n;
		 int max_num = (int)Math.pow(10, digit_num);
		 System.out.println(min_num);
		 System.out.println(max_num);
        for (int i = min_num; i <= max_num; i++){
            if (sum_digit(i) == sum) {
                answer = i;
                break;
            }
        }
        System.out.println(answer);
	 }
}
