import java.util.*;
import java.io.*;

class Main {
    static char[][] puzzle;
    static boolean[][] visited;
    static int rows, cols;
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    
    public static void main(String[] args) {
        try {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            
            String[] size = br.readLine().split(" ");
            rows = Integer.parseInt(size[0]);
            cols = Integer.parseInt(size[1]);
            
            puzzle = new char[rows][cols];
            for (int i = 0; i < rows; i++) {
                String line = br.readLine();
                for (int j = 0; j < cols; j++) {
                    puzzle[i][j] = line.charAt(j);
                }
            }
            
            int numWords = Integer.parseInt(br.readLine());
            String[] words = new String[numWords];
            for (int i = 0; i < numWords; i++) {
                words[i] = br.readLine();
            }
            
            Map<Character, List<int[]>> letterPositions = new HashMap<>();
            for (int r = 0; r < rows; r++) {
                for (int c = 0; c < cols; c++) {
                    char ch = puzzle[r][c];
                    if (!letterPositions.containsKey(ch)) {
                        letterPositions.put(ch, new ArrayList<>());
                    }
                    letterPositions.get(ch).add(new int[]{r, c});
                }
            }
            
            visited = new boolean[rows][cols];
            int count = 0;
            
            for (String word : words) {
                if (word.length() == 0) continue;
                
                char firstChar = word.charAt(0);
                List<int[]> positions = letterPositions.get(firstChar);
                
                if (positions == null) continue;
                
                boolean found = false;
                for (int[] pos : positions) {
                    if (dfs(word, 1, pos[0], pos[1])) {
                        found = true;
                        break;
                    }
                }
                if (found) count++;
            }
            
            System.out.println(count);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    static boolean dfs(String word, int pos, int row, int col) {
        if (pos == word.length()) {
            return true;
        }
        
        visited[row][col] = true;
        
        for (int i = 0; i < 4; i++) {
            int newRow = row + dr[i];
            int newCol = col + dc[i];
            
            if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols &&
                !visited[newRow][newCol] && puzzle[newRow][newCol] == word.charAt(pos)) {
                
                if (dfs(word, pos + 1, newRow, newCol)) {
                    visited[row][col] = false;
                    return true;
                }
            }
        }
        
        visited[row][col] = false;
        return false;
    }
}