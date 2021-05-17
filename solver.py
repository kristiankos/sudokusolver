import math
# Esimerkki sudoku
# 201063580000210340000500190900000700013800020082905401020004610000002800059006004

def get_input():
    return input('Anna sudoku: ')    

def string_to_list(sudoku):
    sudoku_as_list = []
    sudoku_as_list = list(map(int, sudoku))
    return sudoku_as_list


# Tämä tulostaa sudokun konsoliin helpommin luettavassa muodossa
def print_sudoku(sudoku):
    print('')
    for i in range(10):
        row = get_row(sudoku, i)
        for j in range(len(row)):
            print(row[j], end = ' ')
        print('')


def solve(sudoku):
    # Haetaan sudokusta seuraava tyhjä solu...
    empty_cell = next_empty_cell(sudoku)
    # ... jos tyhjää solua ei löydy, sudoku on valmis ja poistutaan
    if empty_cell is None:
        return True

    for number in range(1, 10):
        # Yritetään täyttää tyhjä solu luvulla yhdestä yhdeksään
        if can_fill_cell(sudoku, empty_cell, number):
            # Jos sopiva luku löytyy, asetetaan se soluun
            sudoku[empty_cell] = number

            # Seuraavaksi jatketaan sudokun ratkaisua tekemällämme muutoksella kutsumalla funktiota uudestaan
            if solve(sudoku):
                return True
            # Jos mikään luvuista ei sovi tyhjään soluun, on haara on vääri ja palaamme edelliseen tilaan (tyhjä solu)
            else:
                sudoku[empty_cell] = 0



# Tämä etsii sudokun seuraavan tyhjän solun ja palauttaa sen indeksin (0-80)
def next_empty_cell(sudoku):
    for i in range(81):
        if (sudoku[i] == 0):
            return i


# Tarkistetaan, sopiiko ehdotettu numero tyhjään soluun 
def can_fill_cell(sudoku, empty_cell, number):
    if check_row(sudoku, empty_cell, number):
        if check_column(sudoku, empty_cell, number):
            if check_box(sudoku, empty_cell, number):
                return True

# Tarkistetaan sopiiko ehdotettu numero tyhjän solun riviin
def check_row(sudoku, empty_cell, number):
    row_index = get_row_index(empty_cell)
    row = get_row(sudoku, row_index)
    if (number in row):
        return False
    else:
        return True

# Haetaan parametrina annettavan tyjän solun rivi-indeksi (0-8)
def get_row_index(cell):
    return math.floor(cell / 9)

# Haetaan sudokusta koko rivi listana, rivi-indeksin mukaan
def get_row(sudoku, index):
    row = sudoku[index * 9 : (index + 1) * 9]
    return row


# Tämä tarkistaa sopiiko ehdotettu numero tyhjän solun sarakkeeseen
def check_column(sudoku, empty_cell, number):
    column_index = get_column_index(empty_cell)
    column = get_column(sudoku, column_index)
    if (number in column):
        return False
    else:
        return True

# Haetaan parametrina annettavan tyhjän solun sarakeindeksi (0-8)
def get_column_index(cell):
    return cell % 9

# Haetaan sudokusta koko sarake listana, sarakeindeksin mukaan
def get_column(sudoku, index):
    column = []
    for i in range(len(sudoku)):
        if(i % 9 == index):
            column.append(sudoku[i])
    return column



# Tämä tarkistaa sopiiko ehdotettu numero tyhjän solun 3x3 laatikkoon
def check_box(sudoku, empty_cell, number):
    box = get_box(sudoku, empty_cell)
    if (number in box):
        return False
    else:
        return True

# Haetaan parametrina annettavan solun 3x3 laatikon "koordinaatit" tuplena muodossa ("rivi", "sarake")
def get_box_index(cell):
    box_row = math.floor(get_row_index(cell) / 3)
    box_column = math.floor(get_column_index(cell) / 3)
    box_index = (box_row, box_column)
    return box_index

# Haetaan sudokusta listana ne luvut, jotka ovat samassa 3x3 laatikossa kuin parametrina annettu tyhjä solu
def get_box(sudoku, cell):
    box = []
    box_tuple = get_box_index(cell)
    for i in range(len(sudoku)):
        if (get_box_index(i) == box_tuple):
            box.append(sudoku[i])
    return box



def main():
    sudoku_str = get_input()
    s = string_to_list(sudoku_str)
    print_sudoku(s)
    input('Yritä ratkaista?')
    if (solve(s)):
        print('\nValmis ratkaisu:')
        print_sudoku(s)
    else:
        print('\nRatkaisua ei löytynyt')

if __name__ == "__main__":
    main()