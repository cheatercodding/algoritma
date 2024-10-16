def calculate_class_average(grades):
    """
    Notların listesinden sınıf ortalamasını hesaplar.

    Args:
        grades (list): Notların listesi (float veya int)

    Returns:
        float: Sınıf ortalaması
    """
    # Adım 1: Tüm notların toplamını hesapla
    total = sum(grades)

    # Adım 2: Not sayısını hesapla
    num_grades = len(grades)

    # Adım 3: Sınıf ortalamasını hesapla
    average = total / num_grades

    return average

#kullanım şekli
grades = [80, 70, 90, 85, 75]
average = calculate_class_average(grades)
print(f"Sınıf ortalaması: {average:.2f}")