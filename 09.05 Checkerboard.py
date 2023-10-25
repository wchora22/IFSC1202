def create_checkerboard(size):
    if size <= 0:
        return []
    
    checkerboard=[]

    top_border= '+' + '-' * size + '+'
    checkerboard.append(list(top_border))
    for row in range(size):
        interior_row=['|']
        for col in range(size):
            if (row+col)% 2==0:
                interior_row.append('*')
            else:
                interior_row.append(' ')
        interior_row.append('|')
        checkerboard.append(interior_row)
    bottom_border= '+'+'-'*size + '+'
    checkerboard.append(list(bottom_border))
    return checkerboard
def print_checkerboard(checkerboard):
    for row in checkerboard:
        print(''.join(row))
size = int(input("Enter size: "))
checkerboard=create_checkerboard(size)
print_checkerboard(checkerboard)