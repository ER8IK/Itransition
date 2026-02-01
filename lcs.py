from pathlib import Path
from zipfile import ZipFile
import hashlib

ZIP_PATH = Path("./task2.zip")
EMAIL = "dedppoolbhfg@gmail.com".lower()  # ⚠️⚠️⚠️ ОБЯЗАТЕЛЬНО ЗАМЕНИТЕ!!!

hashes = []

# 1. Читаем архив
with ZipFile(ZIP_PATH, "r") as zip_ref:
    file_names = zip_ref.namelist()
    
    # Фильтруем только файлы (без папок и скрытых файлов)
    file_names = [name for name in file_names 
                  if not name.endswith("/") 
                  and not name.startswith("__MACOSX")
                  and not name.startswith(".")
                  and not name.endswith(".DS_Store")]

    print(f"✓ Files count: {len(file_names)}")  # ДОЛЖНО быть 256!
    
    if len(file_names) != 256:
        print(f"⚠️ WARNING: Expected 256 files, got {len(file_names)}")
        print("File names:", file_names[:10], "...")

    for name in file_names:
        data = zip_ref.read(name)  # читаем как BYTES
        
        # 2. SHA3-256 для КАЖДОГО файла (НЕ SHA-256!)
        h = hashlib.sha3_256(data).hexdigest()
        hashes.append(h)

print(f"✓ Hashes collected: {len(hashes)}")

# 3. Функция сортировки - произведение (цифра + 1)
def sort_key(hex_hash: str) -> int:
    result = 1
    for ch in hex_hash:
        value = int(ch, 16) + 1  # 0->1, 1->2, ..., 9->10, a->11, ..., f->16
        result *= value
    return result

# Тест функции сортировки
test_hash = "63a6ba9e5de66b11ad6c6d3d1b39a5456f65f918fde6250565e365d89a5196c6"
expected_key = 71365623100112242680609229940949951316513259520000000000
calculated_key = sort_key(test_hash)
print(f"\n✓ Sort key test:")
print(f"  Expected:   {expected_key}")
print(f"  Calculated: {calculated_key}")
print(f"  Match: {expected_key == calculated_key}")

# 4. Сортируем хеши
hashes_sorted = sorted(hashes, key=sort_key)

# Показываем первые 3 отсортированных хеша
print(f"\n✓ First 3 sorted hashes:")
for i, h in enumerate(hashes_sorted[:3]):
    print(f"  {i+1}. {h[:32]}... (sort_key: {sort_key(h)})")

# 5. Склеиваем БЕЗ сепаратора
joined_hashes = "".join(hashes_sorted)

print(f"\n✓ Joined hashes length: {len(joined_hashes)}")
print(f"  Expected: {64 * 256} (64 chars × 256 hashes)")
print(f"  Match: {len(joined_hashes) == 64 * 256}")

# 6. Приклеиваем email В КОНЕЦ
final_string = joined_hashes + EMAIL

print(f"\n✓ Email: '{EMAIL}'")
print(f"✓ Email length: {len(EMAIL)}")
print(f"✓ Final string length: {len(final_string)}")
print(f"  Expected: {64 * 256 + len(EMAIL)}")

# Проверка: все символы в lowercase?
if final_string == final_string.lower():
    print(f"✓ All characters are lowercase")
else:
    print(f"⚠️ WARNING: String contains uppercase characters!")

# 7. Финальный SHA3-256 (НЕ SHA-256!)
final_hash = hashlib.sha3_256(final_string.encode('utf-8')).hexdigest()

print("\n" + "="*70)
print("FINAL RESULT (WITH EMAIL):")
print(final_hash)
print("="*70)
print(f"\nДля отправки используйте команду:")
print(f"!task2 {EMAIL} {final_hash}")
print("\n⚠️ УБЕДИТЕСЬ, что EMAIL выше - ваш настоящий email из регистрации!")