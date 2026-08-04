class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def back(row, col,index_str):
            if index_str==len(word):
                return True
            if row>=len(board) or row<0 or col>=len(board[0]) or col<0:
                return False

            if board[row][col]!=word[index_str]:
                return False
            board[row][col]="#"
            c=back(row-1,col,index_str+1) or back(row+1,col,index_str+1) or back(row,col-1,index_str+1) or back(row,col+1,index_str+1)
            board[row][col]=word[index_str]
            return c










        for i in range(len(board)):
            for j in range(len(board[0])):
                if back(i,j,0)==True:
                    return True
        return False
        




















        # seen=set()
        # def check(i,row,col):
        #     directions=[(1,0),(0,1),(-1,0),(0,-1)]
        #     if w[i]==board[row][col]:
        #         seen.add((row,col))
        #         if len(word)-1==i:
        #             return True
        #         for dx,dy in directions :
        #             rc = row + dx
        #             rc2 = col + dy
        #             if 0<=rc<len(board) and 0<=rc2<len(board[0]) and (rc,rc2) not in seen:
        #                 d=check(i+1,rc,rc2)
        #                 if d==True:
        #                     return True
        #         seen.remove((row,col))           
        #     return False
        # w=list(word)
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #         if check(0,i,j)==True:
        #             return True
        # return False                            

                