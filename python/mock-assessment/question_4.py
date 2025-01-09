class ColourPuzzle:
    """
    a class to represent a 4x4 colour puzzle
    
    attributes:
        _board: a 4x4 2D list representing the puzzle board

    methods:
        __init__(puzzle): a constructor to initialize the puzzle board
        matchPattern(pattern): a method to check if the centre 2x2 of the board matches pattern
        _find_empty(): a helper method to find the coordinates of the empty space (0)
        moveLowerTile(): a method to move the tile below the empty space
        moveLeftTile(): a method to move the tile to the left of the empty space
        moveUpperTile(): a method to move the tile above the empty space
        moveRightTile(): a method to move the tile to the right of the empty space
        solvable(pattern, n): a method to check if the puzzle can be solved in n moves
    """

    def __init__(self, puzzle):
        # validate puzzle dimensions (must be a 4x4 2D list)
        if not isinstance(puzzle, list) or len(puzzle) != 4 or \
           not all(isinstance(row, list) and len(row) == 4 for row in puzzle):
            raise ValueError("Puzzle must be a 4x4, 2D list")
        
        # count occurrences of each number
        counts = {0: 0, 1: 0, 2: 0, 3: 0}
        for row in puzzle:
            for val in row:
                if val not in counts:
                    raise ValueError("Invalid value in puzzle")
                counts[val] += 1
        
        # validate counts:
        # (5 of each color and 1 empty space):
        if counts[0] != 1 or any(counts[i] != 5 for i in range(1, 4)):
            raise ValueError("Puzzle must contain 5 tiles of each color and one empty space")
        
        # create a (deep) copy of the puzzle
        self._board = [[puzzle[i][j] for j in range(4)] for i in range(4)]
    
    def matchPattern(self, pattern):
        # check if centre 2x2 of the board matches pattern
        for i in range(2):
            for j in range(2):
                if self._board[i + 1][j + 1] != pattern[i][j]:
                    return False
        return True
    
    def _find_empty(self):
        # extra method to find coordinates of empty space (0)
        for i in range(4):
            for j in range(4):
                if self._board[i][j] == 0:
                    return i, j
        return -1, -1  
        # ^ should not happen if puzzle is valid
    
    def moveLowerTile(self):
        empty_row, empty_col = self._find_empty()
        # check if empty space is in bottom row or if move is impossible
        if empty_row == 3:
            return False
            
        # swap empty space with tile below it
        self._board[empty_row][empty_col], self._board[empty_row + 1][empty_col] = \
            self._board[empty_row + 1][empty_col], self._board[empty_row][empty_col]
        return True
    
    def moveLeftTile(self):
        empty_row, empty_col = self._find_empty()
        # check if empty space is in leftmost column
        if empty_col == 0:
            return False
            
        # swap empty space with tile to its left
        self._board[empty_row][empty_col], self._board[empty_row][empty_col - 1] = \
            self._board[empty_row][empty_col - 1], self._board[empty_row][empty_col]
        return True
    
    def moveUpperTile(self):
        empty_row, empty_col = self._find_empty()
        # check if empty space is in top row
        if empty_row == 0:
            return False
            
        # swap empty space with tile above it
        self._board[empty_row][empty_col], self._board[empty_row - 1][empty_col] = \
            self._board[empty_row - 1][empty_col], self._board[empty_row][empty_col]
        return True
    
    def moveRightTile(self):
        empty_row, empty_col = self._find_empty()
        # check if empty space is in rightmost column
        if empty_col == 3:
            return False
            
        # swap empty space with tile to its right
        self._board[empty_row][empty_col], self._board[empty_row][empty_col + 1] = \
            self._board[empty_row][empty_col + 1], self._board[empty_row][empty_col]
        return True

    def solvable(self, pattern, n):
        if n < 0:
            return False
        if self.matchPattern(pattern):
            return True
        if n == 0:
            return False
            
        # create copies of the current board state for each possible move
        original_board = [row[:] for row in self._board]
        
        # try each possible move
        moves = [self.moveLowerTile, self.moveLeftTile, self.moveUpperTile, self.moveRightTile]
        for move in moves:
            # try the move
            if move():
                # ff the move was successful, recursively check if can be solved with n-1 moves
                if self.solvable(pattern, n - 1):
                    return True
                # restore the board state for the next attempt
                self._board = [row[:] for row in original_board]
            
        return False