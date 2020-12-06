def get_passes():
    import os
    curr_dir = os.path.dirname(__file__)
    exp_file_name = "boardingpasses.txt"
    exp_file_path = os.path.join(curr_dir, exp_file_name)

    with open(exp_file_path, "r") as exp_file:
        expenses = [line.rstrip() for line in exp_file.readlines()]

    return expenses



seats = get_passes()
# seats = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
highest_seat = 0
for seat in seats:
    row_min = 0
    row_max = 127
    col_max = 7
    col_min = 0
    row = seat[0:7]
    col_digit = 0
    row_digit = 0
    col = seat[7:]
    for i, x in enumerate(row):
        if x == "B":
            row_min += (row_max-row_min)/2
            row_min = int(row_min) + 1
            row_digit = row_max
        else:
            row_max -= (row_max-row_min)/2
            row_max = int(row_max)
            row_digit = row_min

    for i in col:
        if i == "R":
            col_min += (col_max-col_min)/2
            col_min = int(col_min) + 1
            col_digit = col_max
        else:
            col_max -= (col_max-col_min)/2
            col_max = int(col_max)
            col_digit = col_min
    print(row_digit, col_digit)
    seat_id = (row_digit * 8) + col_digit
    if seat_id > highest_seat:
        highest_seat = seat_id

print(highest_seat)

highest_seat = 0
for seat in seats:
    row = seat[0:7]
    col = seat[7:]
    row = row.replace("B", "1")
    row = row.replace("F", "0")
    col = col.replace("R", "1")
    col = col.replace("L", "0")
    row_digit = int(row, 2)
    col_digit = int(col, 2)
    seat_id = (row_digit * 8) + col_digit
    if seat_id > highest_seat:
        highest_seat = seat_id
    #print(row_digit, col_digit)
print(highest_seat)

all_seats = list(range(highest_seat+1))
#print(all_seats)
for seat in seats:
    row = seat[0:7]
    col = seat[7:]
    row = row.replace("B", "1")
    row = row.replace("F", "0")
    col = col.replace("R", "1")
    col = col.replace("L", "0")
    row_digit = int(row, 2)
    col_digit = int(col, 2)
    seat_id = (row_digit * 8) + col_digit
    all_seats.remove(seat_id)

print(all_seats)
