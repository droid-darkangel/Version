"""
Пример базового использования класса Version

Этот файл демонстрирует основные возможности работы с классом Version,
который реализует функциональность аналогичную .NET Version.
"""

from ..src.version import Version
def main():
    print("=== Демонстрация работы класса Version ===")
    
    # 1. Создание объектов
    print("\n1. Создание объектов Version:")
    v1 = Version()
    v2 = Version(1, 2)
    v3 = Version(1, 2, 3)
    v4 = Version(1, 2, 3, 4)
    v5 = Version("1.5.0")
    
    for i, v in enumerate([v1, v2, v3, v4, v5], 1):
        print(f"v{i}: {v}")

    # 2. Доступ к свойствам
    print("\n2. Свойства версии v4 (1.2.3.4):")
    print(f"Major: {v4.major}")
    print(f"Minor: {v4.minor}")
    print(f"Build: {v4.build}")
    print(f"Revision: {v4.revision}")

    # 3. Сравнение версий
    print("\n3. Сравнение версий:")
    print(f"{v2} == {v3}: {v2 == v3}")
    print(f"{v3} == Version(1, 2, 3): {v3 == Version(1, 2, 3)}")

    # 4. Обработка ошибок
    print("\n4. Примеры ошибок:")
    try:
        Version("1.2.3.4.5")
    except ValueError as e:
        print(f"Ошибка при парсинге строки: {e}")
    
    try:
        Version(-1, 2)
    except ValueError as e:
        print(f"Ошибка при создании: {e}")

if __name__ == "__main__":
    main()