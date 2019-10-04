initial_permutation_table = {
    58: 1,
    50: 2,
    42: 3,
    34: 4,
    26: 5,
    18: 6,
    10: 7,
    2: 8,
    60: 9,
    52: 10,
    44: 11,
    36: 12,
    28: 13,
    20: 14,
    12: 15,
    4: 16,
    62: 17,
    54: 18,
    46: 19,
    38: 20,
    30: 21,
    22: 22,
    14: 23,
    6: 24,
    64: 25,
    56: 26,
    48: 27,
    40: 28,
    32: 29,
    24: 30,
    16: 31,
    8: 32,
    57: 33,
    49: 34,
    41: 35,
    33: 36,
    25: 37,
    17: 38,
    9: 39,
    1: 40,
    59: 41,
    51: 42,
    43: 43,
    35: 44,
    27: 45,
    19: 46,
    11: 47,
    3: 48,
    61: 49,
    53: 50,
    45: 51,
    37: 52,
    29: 53,
    21: 54,
    13: 55,
    5: 56,
    63: 57,
    55: 58,
    47: 59,
    39: 60,
    31: 61,
    23: 62,
    15: 63,
    7: 64
}

final_permutation_table = {
    40: 1,
    8: 2,
    48: 3,
    16: 4,
    56: 5,
    24: 6,
    64: 7,
    32: 8,
    39: 9,
    7: 10,
    47: 11,
    15: 12,
    55: 13,
    23: 14,
    63: 15,
    31: 16,
    38: 17,
    6: 18,
    46: 19,
    14: 20,
    54: 21,
    22: 22,
    62: 23,
    30: 24,
    37: 25,
    5: 26,
    45: 27,
    13: 28,
    53: 29,
    21: 30,
    61: 31,
    29: 32,
    36: 33,
    4: 34,
    44: 35,
    12: 36,
    52: 37,
    20: 38,
    60: 39,
    28: 40,
    35: 41,
    3: 42,
    43: 43,
    11: 44,
    51: 45,
    19: 46,
    59: 47,
    27: 48,
    34: 49,
    2: 50,
    42: 51,
    10: 52,
    50: 53,
    18: 54,
    58: 55,
    26: 56,
    33: 57,
    1: 58,
    41: 59,
    9: 60,
    49: 61,
    17: 62,
    57: 63,
    25: 64
}

binary = [
    1, 0, 1, 0,
    1, 1, 0, 1,
    0, 1, 0, 1,
    0, 1, 1, 0,
    1, 1, 0, 0,
    1, 0, 0, 1,
    1, 1, 0, 1,
    1, 0, 1, 0,
    1, 0, 0, 1,
    0, 0, 0, 1,
    1, 0, 1, 1,
    1, 0, 1, 1,
    0, 0, 0, 1,
    1, 0, 0, 1,
    1, 0, 1, 1,
    1, 0, 1, 0
]

slideEight = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 1, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 1
]

slideNine = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    1, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 1, 0
]


def get_output_from_permutation_table(binary, permutation_table):
    output = []
    for n in range(64):
        output.insert(n, 0)

    for i in range(64):
        if binary[i] is 1:
            index = permutation_table[i + 1] - 1
            output[index] = 1

    return output


# def get_output_from_final_permutation():
#     for i in range(64):
#         if initial_output[i] is 1:
#             index = final_permutation_table[i + 1] - 1
#             final_output[index] = 1


def print_list(list):
    for i in range(len(list)):
        print(str(list[i]) + " ", end="", flush=True)
        if i % 4 is 3:
            print("    ", end="", flush=True)


def get_left_right(list):
    left = []
    right = []
    for i in range(len(list)):
        if i < 32:
            left.append(list[i])
        else:
            right.append(list[i])
    return left, right

initial_output = get_output_from_permutation_table(binary, initial_permutation_table)
final_output = get_output_from_permutation_table(initial_output, final_permutation_table)

print("\nINITIAL OUTPUT")
print_list(initial_output)
(initial_left, initial_right) = get_left_right(initial_output)
print("\n\nLEFT")
print_list(initial_left)
print("\n\nRIGHT")
print_list(initial_right)

print("\n\n------------------------------------------------------------------------------------------")

print("\nFINAL OUTPUT")
print_list(final_output)
(final_left, final_right) = get_left_right(final_output)
print("\n\nLEFT")
print_list(final_left)
print("\n\nRIGHT")
print_list(final_right)
