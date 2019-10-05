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

compression = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26,
    8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45,
    33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

compression_permutation = {
    14: 1, 17: 2, 11: 3, 24: 4, 1: 5, 5: 6, 3: 7, 28: 8,
    15: 9, 6: 10, 21: 11, 10: 12, 23: 13, 19: 14, 12: 15, 4: 16,
    26: 17, 8: 18, 16: 19, 7: 20, 27: 21, 20: 22, 13: 23, 2: 24,
    41: 25, 52: 26, 31: 27, 37: 28, 47: 29, 55: 30, 30: 31, 40: 32,
    51: 33, 45: 34, 33: 35, 48: 36, 44: 37, 49: 38, 39: 39, 56: 40,
    34: 41, 53: 42, 46: 43, 42: 4, 50: 45, 36: 46, 29: 47, 32: 48
}

expansion_p_box = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

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
s_boxes = [
    [
        14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7,
        0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8,
        4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0,
        15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13
    ],

    [
        15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10,
        3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5,
        0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15,
        13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9
    ],

    [
        10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8,
        13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1,
        13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7,
        1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12
    ],

    [
        7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15,
        13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9,
        10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4,
        3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14
    ],

    [
        2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9,
        14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6,
        4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14,
        11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3
    ],

    [
        12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11,
        10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8,
        9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6,
        4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13
    ],

    [
        4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1,
        13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6,
        1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2,
        6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12
    ],

    [
        13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7,
        1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2,
        7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8,
        2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11
    ]
]


straight_permutation = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]



def get_output_from_permutation_table(binary, permutation_table, size):
    output = []
    for n in range(size):
        output.insert(n, 0)

    for i in range(size):
        if binary[i] is 1:
            index = permutation_table[i + 1] - 1
            output[index] = 1

    return output


def permute(binary, permutation_table, size):
    output = []
    for i in range(size):
        output.append(binary[permutation_table[i] - 1])
    return output


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


def get_cipher_key(binary):
    cipher_key = []
    for n in range(64):
        if (n + 1) % 8 is not 0:
            cipher_key.append(binary[n])
    return cipher_key


def shift_bits_left(list):
    first = list.pop(0)
    list.append(first)
    return list


def expand(list):
    r_expanded = []
    for index in expansion_p_box:
        r_expanded.append(list[index - 1])
    return r_expanded


def xor(l1, l2, size):
    xor_list = []
    for index in range(size):
        xor_list.append(int(l1[index]) ^ int(l2[index]))
    return xor_list


def groups_of_six(list):
    return [list[0:6], list[6:12], list[12:18], list[18:24], list[24:30], list[30:36], list[36:42], list[42:48]]



def s_box_output(groups):
    output = []
    ans = ""
    for index in range(8):
        group = groups[index]
        binary = ''.join(str(s) for s in group)
        row = int(binary[0] + binary[-1], 2)
        col = int(binary[1: -1], 2)

        array = '{0:04b}'.format(s_boxes[index][row*16 + col])
        for b in array:
            output.append(b)
    return output


print("ORIGINAL BINARY")
print_list(binary)
print("\n")
print("K1 (PARITY DROP)")
k1 = get_cipher_key(binary)
print_list(k1)
(left, right) = get_left_right(k1)
left = shift_bits_left(left)
right = shift_bits_left(right)
k1 = left + right
k1 = permute(k1, compression, 48)
print("\n\nCOMPRESSED K1")
print_list(k1)

print("\n")
print("L0")
(left, right) = get_left_right(binary)
print_list(left)
print("\n")
print("R0")
print_list(right)
print("\n")
print("EXPAND R0 TO GET E[R0]")
right_expanded = expand(right)
print_list(right_expanded)
print("\n")
print("A = E[R0] XOR K1")
xor_list = xor(right_expanded, k1, 48)
print_list(xor_list)

groups = groups_of_six(xor_list)
print("\n\nS BOX SUBSTITUTIONS")
B = s_box_output(groups)
print_list(B)

print("\n\nP(B)")
PB = permute(B, straight_permutation, 32)
print_list(PB)
print("\n\n")
print("R1 = P(B) XOR L0")
xor_list = xor(PB, left, 32)
print_list(xor_list)
# print("USING BINARY")
# print_list(slideEight)
# print("\n")
# initial_output = get_output_from_permutation_table(slideEight, initial_permutation_table)
# final_output = get_output_from_permutation_table(initial_output, final_permutation_table)
#
# print("\nINITIAL OUTPUT")
# print_list(initial_output)
# (initial_left, initial_right) = get_left_right(initial_output)
# print("\n\nLEFT")
# print_list(initial_left)
# print("\n\nRIGHT")
# print_list(initial_right)
# print("\n\n")
# print_list(expand(initial_right))
# print("\n\n------------------------------------------------------------------------------------------")
# print("USING THE INITIAL OUTPUT")
# print_list(initial_output)
# print_list("\n\n")
# print("\nFINAL OUTPUT")
# print_list(final_output)
# (final_left, final_right) = get_left_right(final_output)
# print("\n\nLEFT")
# print_list(final_left)
# print("\n\nRIGHT")
# print_list(final_right)
