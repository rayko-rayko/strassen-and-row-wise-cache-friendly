from strassen_rowwise import strassen_multiply
import numpy as np
from cleaning_robot_example import CleaningRobot


def run_matrix_multiplication(size):
    np.random.seed(0)
    A = np.random.randint(0, 100, (size, size)).astype(np.int16)
    B = np.random.randint(0, 100, (size, size)).astype(np.int16)

    C = strassen_multiply(A, B)
    print(
        f"Strassen ve Row-Wise Cache-Friendly algoritmaları birleştirilmiş matris çarpımı sonucu ({size}x{size} boyutunda):")
    print(C)


def run_cleaning_robot():
    robot = CleaningRobot(threshold=20)

    # Farklı boyutlardaki odalar için temizlik yap
    room_sizes = [10, 25, 15, 30]  # Örnek oda boyutları
    for size in room_sizes:
        robot.clean_room(size)


if __name__ == "__main__":
    matrix_size = 128  # İstediğiniz matris boyutunu burada belirleyebilirsiniz
    print("Matris Çarpımı Sonuçları:")
    run_matrix_multiplication(matrix_size)
    print("\nTemizlik Robotu Sonuçları:")
    run_cleaning_robot()