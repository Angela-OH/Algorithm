package DX;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class question1 {
	
	static int t, r, c;
	static int answer = 0;
	static int[] dx = {0, 0, 1, -1}, dy = {1, -1, 0, 0};
	
	public static void dfs(List<String> array, boolean[][] visited, boolean[] alpha, int x, int y, int cnt) {
		
		if (cnt > answer)
			answer = cnt;

		int new_x, new_y;
		for (int i = 0; i < 4; i++) {
			new_x = x + dx[i];
			new_y = y + dy[i];
			if (0 <= new_x && new_x < r && 0 <= new_y && new_y < c) {
				if (!visited[new_x][new_y] && !alpha[array.get(new_x).charAt(new_y) - 'A']) {
					visited[new_x][new_y] = true;
					alpha[array.get(new_x).charAt(new_y) - 'A'] = true;
					dfs(array, visited, alpha, new_x, new_y, cnt + 1);
					visited[new_x][new_y] = false;
					alpha[array.get(new_x).charAt(new_y) - 'A'] = false;
				}
			}
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scanner = new Scanner(System.in);
		t = scanner.nextInt();
		String input;
		
		for (int i = 0; i < t; i ++) {
			r = scanner.nextInt();
			c = scanner.nextInt();
			
			List<String> array = new ArrayList<>();
			boolean[][] visited = new boolean[r][c];
			boolean[] alpha = new boolean[26];
			answer = 0;
			
			for (int j = 0; j < r; j ++) {
				input = scanner.next();
				array.add(input);
			}
			
			
			visited[0][0] = true;
			alpha[array.get(0).charAt(0) - 'A'] = true;
			
			dfs(array, visited, alpha, 0, 0, 1);
			
			System.out.printf("#%d %d\n", i + 1, answer);
		}
		
		scanner.close();
	}
}
