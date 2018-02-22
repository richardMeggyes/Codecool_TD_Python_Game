def get_path_from_map(map):
    sorted_list = []

    # start tile
    for iter, row in enumerate(map):
        for iter2, col in enumerate(row):
            if col == '2':
                sorted_list.append([iter2, iter])
                break

    finished_parsing = False
    # get tiles in order
    while not finished_parsing:

        last_x = int(sorted_list[-1][0])
        last_y = int(sorted_list[-1][1])

        try:
            # Check to right
            if map[last_x + 1][last_y] == '1' and [last_x + 1, last_y] not in sorted_list:
                sorted_list.append([last_x + 1, last_y])
            elif map[last_x + 1][last_y] == '3':
                finished_parsing = True

        except:
            pass

        try:
            # Check to left
            if map[last_x - 1][last_y] == '1' and [last_x - 1, last_y] not in sorted_list:
                sorted_list.append([last_x - 1, last_y])
            elif map[last_x - 1][last_y] == '3':
                finished_parsing = True
        except:
            pass

        try:
            # Check to down
            if map[last_x][last_y + 1] == '1' and [last_x, last_y + 1] not in sorted_list:
                sorted_list.append([last_x, last_y + 1])
            elif map[last_x][last_y + 1] == '3':
                finished_parsing = True
        except:
            pass
        try:
            # Check to up
            if map[last_x][last_y - 1] == '1' and [last_x, last_y - 1] not in sorted_list:
                sorted_list.append([last_x, last_y - 1])
            elif map[last_x][last_y - 1] == '3':
                finished_parsing = True
        except:
            pass

    # end tile
    for iter, row in enumerate(map):
        for iter2, col in enumerate(row):

            if col == '3':
                sorted_list.append([iter2, iter])
                break

    return sorted_list


def import_map(filename):
    return_me = []
    infile = open(filename, 'r')
    for line in infile:
        line = line.strip('\n')
        newline = []
        for c in line:
            newline.append(c)
        return_me.append(newline)
    infile.close()
    return return_me