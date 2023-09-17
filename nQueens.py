# CPSC 460/560 AI project 1 - Constrained N_Queens using backtracking
#                             Constraint: 1st queen's position is fixed
# Author: Michael Connolly
#
# Do not change the following part. NO other package is allowed.
import sys
import pandas as pd
# ---------------------------------------------------------------


# Get the length of a board
# @param: board you're using
# return: the board length
def getN(board):
    return len(board)


# Get the constraint queen's index
# @param: board you're using
# return: the initial queen index
def getInitialQueen(board):
    N = getN(board)

    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                return row, col

    # No queen on board
    return None


# Check if the queen is safe to place
# @param: board you're placing the queen on
# @param: column of the board
# @param: row of the board
# return: true / false depending on if the queen is safe
def isSafe(board, row, col):
    N = getN(board)

    # Check row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left
    for i, j in zip(range(row + 1, N, 1), range(col - 1, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check right side
    for i in range(col + 1, N):
        if board[row][i] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i][j] == 1:
            return False

    # Check lower-right diagonal
    for i, j in zip(range(row + 1, N), range(col + 1, N)):
        if board[i][j] == 1:
            return False

    return True


# Place queens on the board
# @param: board you're placing the queens on
# @param: column of the board
# @param: index of initial queen
# return: true / false depending on if the queens are placed
def placeQueens(board, col, initialQueen):
    N = getN(board)

    # Base case: All queens are placed, return True
    if col >= N:
        return True

    for row in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1

            # Continue to place queens until all queens are placed
            if placeQueens(board, col + 1, initialQueen):
                return True

            # Don't backtrack if initial queen
            if col == initialQueen[1] and row == initialQueen[0]:
                continue

            # Backtrack to previous queen
            board[row][col] = 0

    # Queens can't be placed for a solution
    return False


# Backtracking nQueens problem solver | Constraints: 1st queen position is fixed
# @param: board you're using | initial board must have 1st queen
# @return: solution in a pandas.DataFrame / None if no solution
def nQueens_solver(board):
    initialQueen = getInitialQueen(board)

    # Invalid starting board
    if not initialQueen:
        return None

    if placeQueens(board, 0, initialQueen):
        # Solution found
        solution = pd.DataFrame(board)
        return solution
    else:
        # No solution found
        return None


# No need to change the main function. Do not change output filename.
def main():
    fileName_initial_Queen_pos, = sys.argv[1:]
    print('input filename: '+fileName_initial_Queen_pos)
    input_df = pd.read_csv(fileName_initial_Queen_pos, header=None)
    #
    # solution_df is the dataframe that stores your solution to the n-Queens problem (1-queen, 0-blank)
    solution_df = nQueens_solver(input_df)
    #
    if solution_df is None:
        print("No solution!")
    else:
        output_fname = 'solution__' + str(solution_df.shape[0]) + '.csv'
        print('output file name: ' + output_fname)
        solution_df.to_csv(output_fname, sep=',', header=None, index=False)


if __name__ == '__main__':
    main()

