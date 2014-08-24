import java.util.*;

public class Solution {

    boolean[][] isOccupied;
    char[][] board;
    int N, M;

    public boolean exist(char[][] board, String word) {
        this.N = board.length;
        this.M = board[0].length;

        this.board = board;

        isOccupied = new boolean[N][M];

        for(int i = 0; i < N; i++){
            Arrays.fill(isOccupied[i], false);
        }

        for(int i = 0; i < N; i++){
            for(int j = 0 ; j< M; j++){
                if(board[i][j] == word.charAt(0) && isExist(0, i, j, word)){
                    return true;
                }
            }
        }
        return false;
    }

    public boolean isExist(int level, int i, int j, String word){
        isOccupied[i][j] = true;

        boolean is_exist = false;

        if(level == word.length() -1 && word.charAt(level) == board[i][j] ){
            isOccupied[i][j] = false;
            return true;
        }

        if(!is_exist && i-1 >= 0 && !isOccupied[i-1][j] && word.charAt(level+1) == board[i-1][j]){
            is_exist = this.isExist(level+1, i-1, j, word);
        }
        if(!is_exist && j-1 >= 0 && !isOccupied[i][j-1] && word.charAt(level+1) == board[i][j-1]){
            is_exist = this.isExist(level+1, i, j-1, word);
        }
        if(!is_exist && i+1 < N && !isOccupied[i+1][j] && word.charAt(level+1) == board[i+1][j]){
            is_exist = this.isExist(level+1, i+1, j, word);
        }
        if(!is_exist && j+1 < M && !isOccupied[i][j+1] && word.charAt(level+1) == board[i][j+1]){
            is_exist = this.isExist(level+1, i, j+1, word);
        }

        isOccupied[i][j] = false;
        return is_exist;
    }

    public static void main(String[] argv){
        char[][] board = new char[][]{{'A', 'B', 'C', 'E'}, {'S', 'F', 'C', 'S'}, {'A', 'D', 'E', 'E'} };
        Solution s = new Solution();

        System.out.println(s.exist(board, "ABCCED"));
        System.out.println(s.exist(board, "SEE"));
        System.out.println(s.exist(board, "ABCB"));

    }

}
