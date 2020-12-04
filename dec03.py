def findTreesHelper(input_array, x, y):
    current_x, current_y, tree_count = 0, 0, 0
    line_width = len(input_array[0])
    while current_y < len(input_array):
        if input_array[current_y][current_x % line_width] == "#":
            tree_count += 1
        current_y += y
        current_x += x
    return tree_count


with open('input_dec03.txt') as input_file:
    #parse the file
    line = [lines.strip() for lines in input_file]
    print(findTreesHelper(line,3,1))

    print(findTreesHelper(line,1,1) * findTreesHelper(line,3,1) * findTreesHelper(line,5,1)
           * findTreesHelper(line,7,1) * findTreesHelper(line,1,2))

