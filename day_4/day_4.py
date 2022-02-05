class Game_board:
    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.score = [[0 for y in range(self.size)] for x in range(self.size)]
        self.marked_numbers = []
        self.won = False

    # assign 1 in each place the number matches a number that's been called
    def update_score(self, number):
        self.marked_numbers.append(number)
        self.score = [[int(self.board[x][y] in self.marked_numbers) for y in range(self.size)] for x in range(self.size)]

    # see if any row or column adds up to the size of the board
    def check_winner(self):
        # check columns
        for x in range(self.size):
            column_score = 0
            for y in range(self.size):
                column_score += self.score[x][y]
            if column_score == self.size: return True
        # check rows
        for y in range(self.size):
            row_score = 0
            for x in range(self.size):
                row_score += self.score[x][y]
            if row_score == self.size: return True
        # return False if neither score is 5
        return False

    # sum unmarked numbers:
    def sum_unmarked_numbers(self):
        sum = 0
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] not in self.marked_numbers:
                    sum += self.board[x][y]
        return sum

numbers = []
with open('numbers.txt') as input:
    numbers = input.readline().strip().split(',')
    numbers = [int(number) for number in numbers]

boards = []
# need to convert to boards from file
with open('boards.txt') as input:
    boards = input.readlines()

boards = [element.strip().split() for element in boards]
print()
game_boards = []
new_board = []
for column in boards:
    if len(column) > 0: new_board.append([int(element) for element in column])
    else: # if blank list, board is done, so append
        game_boards.append(Game_board(new_board))
        new_board = []
# one last one since it's the end of file
game_boards.append(Game_board(new_board))

# go through numbers and check winners (need first and last)
count = 0
for number in numbers:
    break_flag = False
    for board in game_boards:
        board.update_score(number)
        if board.check_winner() == True and board.won == False:
            count += 1
            print('Winner {} is {}'.format(str(count), str(board.sum_unmarked_numbers() * number)))
            board.won = True
        if count == len(game_boards):
            break_flag = True
            break
    if break_flag == True: break
