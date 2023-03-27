from random import randint


def display_board(board):
    # Funkcja, która przyjmuje jeden parametr zawierający bieżący stan tablicy
    # i wyświetla go w oknie konsoli.
    print("+-----+-----+-----+")
    print(f"|  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |")
    print("+-----+-----+-----+")
    print(f"|  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |")
    print("+-----+-----+-----+")
    print(f"|  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |")
    print("+-----+-----+-----+")
    # kontrolne wyświetlenie liczby pozostałych pól:
    print(f"{fields_left} fields left.")


def enter_move(board):
    # Funkcja, która przyjmuje parametr odzwierciedlający bieżący stan tablicy,
    # prosi użytkownika o wykonanie ruchu,
    # sprawdza dane wejściowe i aktualizuje tablicę zgodnie z decyzją użytkownika.
    global fields_left
    free_fields_list = make_list_of_free_fields(board)
    while True:
        try:
            move = int(input("Choose empty field from 1-9:"))
        except:
            print("your choice has to be number, try again!")
            continue
        if move in free_fields_list:
            match move:
                case 1:
                    if board[0][0] == 1:
                        board[0][0] = 'O'
                        break
                    else:
                        continue
                case 2:
                    if board[0][1] == 2:
                        board[0][1] = 'O'
                        break
                    else:
                        continue
                case 3:
                    if board[0][2] == 3:
                        board[0][2] = 'O'
                        break
                    else:
                        continue
                case 4:
                    if board[1][0] == 4:
                        board[1][0] = 'O'
                        break
                    else:
                        continue
                case 5:
                    if board[1][1] == 5:
                        board[1][1] = 'O'
                        break
                    else:
                        continue
                case 6:
                    if board[1][2] == 6:
                        board[1][2] = 'O'
                        break
                    else:
                        continue
                case 7:
                    if board[2][0] == 7:
                        board[2][0] = 'O'
                        break
                    else:
                        continue
                case 8:
                    if board[2][1] == 8:
                        board[2][1] = 'O'
                        break
                    else:
                        continue
                case 9:
                    if board[2][2] == 9:
                        board[2][2] = 'O'
                        break
                    else:
                        continue
            break
        else:
            if free_fields_list:
                print("Field occupied, try again!")
            else:
                break
    fields_left -= 1
    display_board(board)
    victory_for(board, 'O')



def make_list_of_free_fields(board):
    # Funkcja, która przegląda tablicę i tworzy listę wszystkich wolnych pól;
    # lista składa się z krotek, a każda krotka zawiera parę liczb odzwierciedlających rząd i kolumnę.
    # Dlaczego musi to być krotka???
    free_fields_list = []
    for column in board:
        for row in column:
            if row in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                free_fields_list.append(row)
            else:
                continue
    return free_fields_list


def victory_for(board, sign):
    # Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia,
    # czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.
    global end_flag
    if fields_left > 0:
        if board[0][0] == board[1][0] == board[2][0] == sign:
            who_wins(sign)
        elif board[0][1] == board[1][1] == board[2][1] == sign:
            who_wins(sign)
        elif board[0][2] == board[1][2] == board[2][2] == sign:
            who_wins(sign)
        elif board[0][0] == board[0][1] == board[0][2] == sign:
            who_wins(sign)
        elif board[1][0] == board[1][1] == board[1][2] == sign:
            who_wins(sign)
        elif board[2][0] == board[2][1] == board[2][2] == sign:
            who_wins(sign)
        elif board[0][0] == board[1][1] == board[2][2] == sign:
            who_wins(sign)
        elif board[2][0] == board[1][1] == board[0][2] == sign:
            who_wins(sign)
    # else:
    #     display_board(board)
    #     print("Draw!")
    #     end_flag = False


def who_wins(sign):
    # W sytuacji, kiedy pojawią się trzy identyczne symbole w jednej linii, funkcja rozpoznaje, do którego z graczy
    # one należą, i na tej podstawie przydziela zwycięstwo.

    global end_flag
    if sign == 'X':
        display_board(board)
        print("Comp won!")
        end_flag = False
    elif sign == 'O':
        print("You won!")
        end_flag = False


def draw_move(board):
    # Funkcja, która wykonuje ruch za komputer i aktualizuje tablicę.
    global fields_left
    while True:
        comp_move = randint(1, 9)
        if comp_move in make_list_of_free_fields(board):
            match comp_move:
                case 1:
                    board[0][0] = 'X'
                    break
                case 2:
                    board[0][1] = 'X'
                    break
                case 3:
                    board[0][2] = 'X'
                    break
                case 4:
                    board[1][0] = 'X'
                    break
                case 5:
                    board[1][1] = 'X'
                    break
                case 6:
                    board[1][2] = 'X'
                    break
                case 7:
                    board[2][0] = 'X'
                    break
                case 8:
                    board[2][1] = 'X'
                    break
                case 9:
                    board[2][2] = 'X'
                    break
        else:
            # print("Comp has choosen occupied field, another try.")
            continue
    fields_left -= 1
    victory_for(board, 'X')
    if fields_left == 0 and not end_flag:
        return
    return board


# Przebieg gry
print("Welcome to the Tic-Tac-Toe game!\nComputer just made it's first move.")
board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
end_flag = True
fields_left = 8
while end_flag:
    display_board(board)
    enter_move(board)
    if not end_flag:
        break
    draw_move(board)
    # if fields_left == 0 and end_flag:
    #     print("Draw!")
    #     break

print("SEE YOU NEXT TIME! :)")


#   Naprawic: poprawic warunek zwyciestwa w ostatnim ruchu -> zeby bylo zwyciestwo, a nie remis
