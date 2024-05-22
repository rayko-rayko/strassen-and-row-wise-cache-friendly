# Bu script, Strassen algoritması ve row-wise cache-friendly algoritmasını birleştirerek matris çarpımı gerçekleştiren fonksiyonları içerir.
#
# İçerdiği Fonksiyonlar:
#
# 1. conventional_multiply(A, B):
#    - Açıklama: Bu fonksiyon, iki matrisin blok bazlı (cache-friendly) çarpımını gerçekleştirir.
#    - Girdi: A ve B matrisleri (numpy dizileri).
#    - Çıktı: A ve B matrislerinin çarpımı sonucu elde edilen matris.
#
# 2. strassen_multiply(A, B):
#    - Açıklama: Bu fonksiyon, Strassen algoritmasını kullanarak matris çarpımı gerçekleştirir. Eğer matris boyutu belirli bir eşik değerin altındaysa, conventional_multiply fonksiyonunu kullanır.
#    - Girdi: A ve B matrisleri (numpy dizileri).
#    - Çıktı: A ve B matrislerinin çarpımı sonucu elde edilen matris.
#
# Bu script, matris boyutuna göre en uygun algoritmayı seçerek verimli matris çarpımı sağlar.
# Strassen algoritması, büyük boyutlu matrisler için hızlı sonuçlar elde ederken, row-wise cache-friendly algoritma, küçük boyutlu matrisler için önbellek performansını artırır.
# Bu iki algoritma birleştirilerek, her iki durumda da etkili bir matris çarpımı gerçekleştirilmiş olur.

import numpy as np

def conventional_multiply(A, B):
    """
    Blok bazlı matris çarpımı (cache-friendly).
    A ve B: Çarpılacak matrisler.
    """
    n = A.shape[0]
    C = np.zeros((n, n), dtype=np.int16)  # 16-bit tamsayı
    block_size = 64  # Blok boyutu, cache dostu olması için

    for i in range(0, n, block_size):
        for j in range(0, n, block_size):
            for k in range(0, n, block_size):
                for ii in range(i, min(i + block_size, n)):
                    for jj in range(j, min(j + block_size, n)):
                        temp_sum = np.int32(0)  # Geçici olarak daha geniş bir tür kullanıyoruz
                        for kk in range(k, min(k + block_size, n)):
                            temp_sum += np.int32(A[ii][kk]) * np.int32(B[kk][jj])
                        C[ii][jj] = np.int16(temp_sum % (2**16))  # 16-bit'e indirgeme, taşmayı kontrol etme
    return C

def strassen_multiply(A, B):
    """
    Strassen algoritması ile matris çarpımı.
    A ve B: Çarpılacak matrisler.
    """
    n = A.shape[0]
    if n <= 64:
        return conventional_multiply(A, B)
    else:
        new_size = n // 2
        A11 = A[:new_size, :new_size]
        A12 = A[:new_size, new_size:]
        A21 = A[new_size:, :new_size]
        A22 = A[new_size:, new_size:]
        B11 = B[:new_size, :new_size]
        B12 = B[:new_size, new_size:]
        B21 = B[new_size:, :new_size]
        B22 = B[new_size:, new_size:]

        M1 = strassen_multiply(A11 + A22, B11 + B22)
        M2 = strassen_multiply(A21 + A22, B11)
        M3 = strassen_multiply(A11, B12 - B22)
        M4 = strassen_multiply(A22, B21 - B11)
        M5 = strassen_multiply(A11 + A12, B22)
        M6 = strassen_multiply(A21 - A11, B11 + B12)
        M7 = strassen_multiply(A12 - A22, B21 + B22)

        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6

        C = np.zeros((n, n), dtype=np.int16)
        C[:new_size, :new_size] = C11
        C[:new_size, new_size:] = C12
        C[new_size:, :new_size] = C21
        C[new_size:, new_size:] = C22

        return C

if __name__ == "__main__":
    np.random.seed(0)
    size = 128  # Matris boyutu
    A = np.random.randint(0, 100, (size, size)).astype(np.int16)  # 16-bit tamsayı
    B = np.random.randint(0, 100, (size, size)).astype(np.int16)  # 16-bit tamsayı

    C = strassen_multiply(A, B)
    print("Strassen ve Row-Wise Cache-Friendly algoritmaları birleştirilmiş matris çarpımı sonucu:")
    print(C)