# NAMA : ALDIAN RAMADAN PUTRA
# KELAS : TI B (SEMESTER 3)

def input_matriks():
    baris_1 = [int(input(f"Masukkan baris 1 kolom {i + 1}: ")) for i in range(3)]
    baris_2 = [int(input(f"Masukkan baris 2 kolom {i + 1}: ")) for i in range(3)]
    baris_3 = [int(input(f"Masukkan baris 3 kolom {i + 1}: ")) for i in range(3)]
    return baris_1, baris_2, baris_3

def print_matriks(matriks):
    for baris in matriks:
        print(f"[{baris[0]}] [{baris[1]}] [{baris[2]}]")

def determinan_sarrus(b1_1, b1_2, b1_3, b2_1, b2_2, b2_3, b3_1, b3_2, b3_3):
    return b1_1 * b2_2 * b3_3 + b1_2 * b2_3 * b3_1 + b1_3 * b2_1 * b3_2 - b3_1 * b2_2 * b1_3 - b3_2 * b2_3 * b1_1 - b3_3 * b2_1 * b1_2

def hitung_minor(b1, b2, b3):
    return [
        [b2[1] * b3[2] - b2[2] * b3[1], b2[0] * b3[2] - b2[2] * b3[0], b2[0] * b3[1] - b2[1] * b3[0]],
        [b1[1] * b3[2] - b1[2] * b3[1], b1[0] * b3[2] - b1[2] * b3[0], b1[0] * b3[1] - b1[1] * b3[0]],
        [b1[1] * b2[2] - b1[2] * b2[1], b1[0] * b2[2] - b1[2] * b2[0], b1[0] * b2[1] - b1[1] * b2[0]]
    ]

def kofaktor(matriks_minor):
    return [
        [matriks_minor[0][0], -matriks_minor[1][0], matriks_minor[2][0]],
        [-matriks_minor[0][1], matriks_minor[1][1], -matriks_minor[2][1]],
        [matriks_minor[0][2], -matriks_minor[1][2], matriks_minor[2][2]]
    ]

def invers_adjoin(kofaktor_matriks, det):
    inv = 1 / det
    return [
        [inv * kofaktor_matriks[i][j] for j in range(3)] for i in range(3)
    ]

def print_matriks_lengkap(nama, matriks):
    print(f"{nama} =")
    print_matriks(matriks)
    print("\n")

# program utama
print("==|PROGRAM MENCARI INV.ADJOIN|==\n")

# Input matriks
print_matriks_lengkap("Matrik ordo 3x3", input_matriks())

# Mencari determinan
det = determinan_sarrus(*input_matriks())
print(f"Det = {det}\n\n")

# Mencari minor
minor = hitung_minor(*input_matriks())
print_matriks_lengkap("MINOR", minor)

# Mencari kofaktor
kofaktor_matriks = kofaktor(minor)
print_matriks_lengkap("KOFAKTOR", kofaktor_matriks)

# Mencari invers adjoin
inv_adjoin = invers_adjoin(kofaktor_matriks, det)
print_matriks_lengkap("INV.ADJOIN", inv_adjoin)

print("SELESAI :)\n___________________________")
