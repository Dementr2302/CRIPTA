# реализация DES

# PI (Initial Permutation Matrix for the Data)
PI = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# CP_1 (Initial Permutation Made on the Key)
CP_1 = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# CP_2 (Permutation Applied on Shifted Key)
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

# E (Expand Matrix)
E = [32, 1, 2, 3, 4, 5,
     4, 5, 6, 7, 8, 9,
     8, 9, 10, 11, 12, 13,
     12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21,
     20, 21, 22, 23, 24, 25,
     24, 25, 26, 27, 28, 29,
     28, 29, 30, 31, 32, 1]

# SBOX (Substitution Boxes)
S_BOX = [

    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
     ],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
     ],

    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
     ],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
     ],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
     ],

    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
     ],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
     ],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
     ]
]

# P (Permut After SBox Substitution)
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

# PI_1 (Final Permutation for Datas)
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


# преобразование строки в список битов
def string_to_bit_array(text):
    array = list()
    for char in text:
        binval = binvalue(char, 8)
        array.extend([int(x) for x in list(binval)])
    return array

# обратное преобразование: из списка битов возвращается строка, полученная из этих битов
def bit_array_to_string(array):
    res = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in nsplit(array, 8)]])
    return res

# бинарное представление значения в виде строки заданного размера
def binvalue(val, bitsize):
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0" + binval
    return binval

# выделение подстрок в строке s длиной n
def nsplit(s, n):
    return [s[k:k + n] for k in range(0, len(s), n)]

# флаги для шифровки/дешифровки
ENCRYPT = 1
DECRYPT = 0

# класс, реализующий шаги алгоритма DES
class des():
    def __init__(self):
        self.password = None
        self.text = None
        self.keys = list()

    # замену блоков данных после применения S-блоков
    def substitute(self, d_e):
        subblocks = nsplit(d_e, 6)
        result = list()
        for i in range(len(subblocks)):
            block = subblocks[i]
            row = int(str(block[0]) + str(block[5]), 2)
            column = int(''.join([str(x) for x in block[1:][:-1]]), 2)
            val = S_BOX[i][row][column]
            bin = binvalue(val, 4)
            result += [int(x) for x in bin]
        return result

    # перестановка для заданного блока данных (block) с использованием указанной таблицы (table)
    def permut(self, block, table):
        return [block[x - 1] for x in table]

    # перестановка для заданного блока данных (block - увеличение размер блока в соответствии порядка таблицы (table)
    def expand(self, block, table):
        return [block[x - 1] for x in table]

    # побитовая операция xor
    def xor(self, t1, t2):
        return [x ^ y for x, y in zip(t1, t2)]

    # циклический сдвиг битов
    def shift(self, g, d, n):
        return g[n:] + g[:n], d[n:] + d[:n]

    # добавление заполнений во входных данных
    def addPadding(self):
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)

    # удаление заполнений из заданных данных
    def removePadding(self, data):
        pad_len = ord(data[-1])
        return data[:-pad_len]

    def run(self, key, text, action=ENCRYPT, padding=False):
        # проверка длины ключа и обрезка
        if len(key) < 8:
            raise "Ключ должен иметь длину 8 байт"
        elif len(key) > 8:
            key = key[:8]

        self.password = key
        self.text = text

        # добавление заполнений (в случае шифрования)
        if padding and action == ENCRYPT:
            self.addPadding()
        elif len(self.text) % 8 != 0:
            raise "Размер данных должен быть кратен 8"

        # генерация подключей
        self.generatekeys()

        # разделение текста на блоки
        text_blocks = nsplit(self.text, 8)

        result = list()
        # для каждого блока
        for block in text_blocks:
            # преобразование в список байтов
            block = string_to_bit_array(block)
            # начальная перестановка PI
            block = self.permut(block, PI)
            # разделение блоков на половины g и d
            g, d = nsplit(block, 32)
            tmp = None
            # в цикле (в течении 16 раундов)
            for i in range(16):
                # расширение половины d
                d_e = self.expand(d, E)
                # шифрование/дешифрование
                # выполнение операции XOR с ключом
                if action == ENCRYPT:
                    tmp = self.xor(self.keys[i], d_e)
                else:
                    tmp = self.xor(self.keys[15 - i], d_e)
                # замена с использованием S-блоков
                tmp = self.substitute(tmp)
                # перестановка (P)
                tmp = self.permut(tmp, P)
                # XOR с половиной g
                tmp = self.xor(g, tmp)
                # обновление g и d
                g = d
                d = tmp
            # объединение g и d и применение конечной перестановки (PI_1)
            result += self.permut(d + g, PI_1)
        # преобразование в строку
        final_res = bit_array_to_string(result)

        # удаление заполнений (в случае дешифрования)
        if padding and action == DECRYPT:
            return self.removePadding(final_res)
        else:
            return final_res

    # генерация подключей (16)
    def generatekeys(self):
        self.keys = []
        # преобразование в список битов
        key = string_to_bit_array(self.password)
        # начальная перестановка (CP_1) ключа
        key = self.permut(key, CP_1)
        # выделение половин g и d
        g, d = nsplit(key, 28)
        # в цикле(16 раундов)
        for i in range(16):
            # циклический сдвиг битов в g и d
            g, d = self.shift(g, d, SHIFT[i])
            # объединение g и d
            tmp = g + d
            self.keys.append(self.permut(tmp, CP_2))

    # функция шифрования
    def encrypt(self, key, text, padding=False):
        return self.run(key, text, ENCRYPT, padding)

    # функция дешифрования
    def decrypt(self, key, text, padding=False):
        return self.run(key, text, DECRYPT, padding)

# открытый текст
plaintext = "Hello, World!"
# ключ
key = "SecretKey"

# преобразование в двоичные последовательности
key_bits = string_to_bit_array(key)
print("Двоичная последовательность ключа:")
print(key_bits)
plaintext_bits = string_to_bit_array(plaintext)
print("Двоичная последовательность открытого текста:")
print(plaintext_bits)

# преобразование обратно в строку
ciphertext = bit_array_to_string(plaintext_bits)
print("Зашифрованный текст:", ciphertext)

# # Ввод двоичных последовательностей ключа и открытого текста
# key_binary = input("Введите двоичную последовательность ключа: ")
# plaintext_binary = input("Введите двоичную последовательность открытого текста: ")
#
# # Преобразование в список битов
# key_bits = [int(bit) for bit in key_binary]
# plaintext_bits = [int(bit) for bit in plaintext_binary]
#
# # Преобразование обратно в строку
# ciphertext = bit_array_to_string(plaintext_bits)
# print("Зашифрованный текст:", ciphertext)
