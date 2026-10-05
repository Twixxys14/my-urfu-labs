# ```python
# def detect_language(text):
#     for char in text.lower():
#         if "а" <= char <= "я":
#             return "ru"
#         elif "a" <= char <= "z":
#             return "en"
#     return "ru" 

# def caesar_cipher(text, shift, mode="encode"):
#     if mode == "decode":
#         shift = -shift
#     lang = detect_language(text)
#     if lang == "ru":
#         alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#         alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#     else:
#         alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
#         alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     result = []
#     alphabet_len = len(alphabet_lower)

#     for char in text:
#         if char in alphabet_lower:
#             old_index = alphabet_lower.index(char)
#             new_index = (old_index + shift) % alphabet_len
#             result.append(alphabet_lower[new_index])
#         elif char in alphabet_upper:
#             old_index = alphabet_upper.index(char)
#             new_index = (old_index + shift) % alphabet_len
#             result.append(alphabet_upper[new_index])
#         else:
#             result.append(char)

#     return "".join(result)

# def main():
#     print("ШИФР ЦЕЗАРЯ")
#     text = input("введите текст: ")

#     try:
#         shift = int(input("ввелите длину сдвига: "))
#     except ValueError:
#         print("ошибка, сдвиг должен быть числом!")
#         shift = 3

#     print("\nвыберите действие:")
#     print("1. зашифровать")
#     print("2. расшифровать")

#     choice = input("(1 или 2)?: ").strip()
#     mode = "encode" if choice == "1" else "decode"

#     detected_lang = (
#         "русский" if detect_language(text) == "ru" else "английский"
#     )
#     print(f"\n[Автоопределение языка]: {detected_lang}")

#     result_text = caesar_cipher(text, shift, mode)
#     print(f"Результат: {result_text}")

# if __name__ == "__main__":
#    main()
#    ```


```python
def get_lang(text):
    for c in text.lower():
        if "а" <= c <= "я" or c == "ё":
            return "ru"
        elif "a" <= c <= "z":
            return "en"
    return "ru"

def caesar(text, shift, mode="encode"):
    if mode == "decode":
        shift = -shift
    lang = get_lang(text)
    if lang == "ru":
        al_low = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        al_up = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    else:
        al_low = "abcdefghijklmnopqrstuvwxyz"
        al_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    n = len(al_low)
    for char in text:
        if char in al_low:
            idx = al_low.index(char)
            new_idx = (idx + shift) % n
            res += al_low[new_idx]
        elif char in al_up:
            idx = al_up.index(char)
            new_idx = (idx + shift) % n
            res += al_up[new_idx]
        else:
            res += char
    return res

def main():
    print("=== ШИФР ЦЕЗАРЯ ===")
    t = input("Введите текст: ")
    s = int(input("Введите сдвиг (число): "))
    print("\n1. Зашифровать")
    print("2. Расшифровать")
    c = input("Выбор (1 или 2): ")
    if c == "1":
        m = "encode"
    else:
        m = "decode"
    l = get_lang(t)
    if l == "ru":
        print("\nЯзык: Русский")
    else:
        print("\nЯзык: Английский")
    out = caesar(t, s, m)
    print("Результат:", out)

if __name__ == "__main__":
    main()```










