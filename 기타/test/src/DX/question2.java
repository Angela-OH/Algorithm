package DX;

import java.util.Scanner;

public class question2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T, x, y, tmp, intN, compare, idx, cnt;
		String n;
		boolean isSpace, checked;
		T = sc.nextInt();
		StringBuilder answer = new StringBuilder();
		
		for(int test_case = 1; test_case <= T; test_case++)
		{
			n = sc.next();
			x = sc.nextInt();
			y = sc.nextInt();
			isSpace = false;
			checked = false;
			idx = 0;
			answer.setLength(0);
			
			if (x > y) { // x <= y 순으로 정렬되도록
				tmp = x;
				x = y;
				y = tmp;
			}
			
			if (x == 0 && y == 0) {
				answer.append("-1");
			}
			else if (n.length() == 1) {
				intN = Integer.parseInt(n);
				if (x == 0 && intN < y)
					answer.append("-1");
				else if (intN < x)
					answer.append("-1");       
				else if (intN >= y)
					answer.append(y);
				else
					answer.append(x);
			}
			else {
				if (((n.charAt(0) - '0') < x) || (x == 0 && (n.charAt(0) - '0') < y)) {
					answer.append(y);
					isSpace = true;
					idx = 2;
				}
				for (int i = idx; i < n.length(); i++) {
					compare = n.charAt(i) - '0';
					if (compare > y) {
						answer.append(y);
						isSpace = true;
					}
					else if (isSpace || compare == y) {
						answer.append(y);
					}
					else if (compare > x) {
						answer.append(x);
						isSpace = true;
					}
					else if (compare == x) {
						answer.append(x);
					}
					else {
						cnt = 1;
						while (true) {
							if ((answer.charAt(answer.length() - cnt) - '0') == y)
								break;
							if (answer.length() == cnt) {
								answer.setLength(0);
								for (int j = 1; j < n.length(); j++)
									answer.append(y);
								checked = true;
								break;
							}
							else
								cnt += 1;
						}
						if (!checked) {
							answer.replace(answer.length() - cnt, answer.length() - cnt + 1, Integer.toString(x));
							answer.setLength(answer.length() - cnt + 1);
							for (int j = answer.length(); j < n.length(); j++)
								answer.append(y);
						}
						break;
					}
				}
			}
			System.out.printf("#%d %s\n", test_case, answer);
		}
	}
}
