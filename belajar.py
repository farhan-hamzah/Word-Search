from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def dfs(r, c, i):
            # jika semua huruf cocok
            if i == len(word):
                return True
            # jika di luar boundary atau huruf tidak cocok
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            
            # simpan dan tandai huruf yang sudah dikunjungi
            temp = board[r][c]
            board[r][c] = "#"  # tanda sudah dikunjungi
            
            # arah: atas, bawah, kiri, kanan
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            
            # backtrack (kembalikan huruf semula)
            board[r][c] = temp
            
            return found
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and dfs(row, col, 0):
                    return True
        return False
