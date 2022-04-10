//
// Created by 29715 on 2022/4/10.
//

class Solution {
public:
    static void precessing(
            vector<vector<bool>> &rows,
            vector<vector<bool>> &cols,
            vector<vector<bool>> &boxes,
            vector<vector<char>> &board
    ) {
        for (int i = 0; i < 9; ++i) {
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    int x = board[i][j] - '1';
                    int bi = i / 3 * 3 + j / 3;
                    rows[i][x] = true;
                    cols[j][x] = true;
                    boxes[bi][x] = true;
                }
            }
        }
    }

    static bool dfs(
            vector<vector<bool>> &rows,
            vector<vector<bool>> &cols,
            vector<vector<bool>> &boxes,
            vector<vector<char>> &board,
            int x, int y
    ) {
        if (y >= 9) {
            y = 0;
            x++;
        }
        if (x >= 9) {
            print_matrix(board);
            return true;
        }

        if (board[x][y] != '.') {
            bool succeed = dfs(rows, cols, boxes, board, x, y + 1);
            return succeed;
        }

        int bi = x / 3 * 3 + y / 3;
        for (int i = 0; i < 9; i++) {
            if (rows[x][i] == false && cols[y][i] == false && boxes[bi][i] == false) {
                rows[x][i] = true;
                cols[y][i] = true;
                boxes[bi][i] = true;
                board[x][y] = i + '1';
                bool succeed = dfs(rows, cols, boxes, board, x, y + 1);
                if (succeed)
                    return true;
                rows[x][i] = false;
                cols[y][i] = false;
                boxes[bi][i] = false;
                board[x][y] = '.';
            }

        }
        return false;
    }

    static void solveSudoku(vector<vector<char>> &board) {
        // false: 可选. visited
        vector<vector<bool>> rows(9, vector<bool>(9));
        vector<vector<bool>> cols(9, vector<bool>(9));
        vector<vector<bool>> boxes(9, vector<bool>(9));
        precessing(rows, cols, boxes, board);
        dfs(rows, cols, boxes, board, 0, 0);
    }
};

int main() {
    vector<vector<char>> board = {
            {'5', '3', '.', '.', '7', '.', '.', '.', '.'},
            {'6', '.', '.', '1', '9', '5', '.', '.', '.'},
            {'.', '9', '8', '.', '.', '.', '.', '6', '.'},
            {'8', '.', '.', '.', '6', '.', '.', '.', '3'},
            {'4', '.', '.', '8', '.', '3', '.', '.', '1'},
            {'7', '.', '.', '.', '2', '.', '.', '.', '6'},
            {'.', '6', '.', '.', '.', '.', '2', '8', '.'},
            {'.', '.', '.', '4', '1', '9', '.', '.', '5'},
            {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
    };
    Solution::solveSudoku(board);
    print_matrix(board);
}