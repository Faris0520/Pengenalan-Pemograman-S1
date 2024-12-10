def valid(s):
    def helper(s, count):
        # Jika string kosong, cek apakah count 0
        if not s:
            return count == 0
        # Jika count negatif, berarti ada lebih banyak ')' daripada '('
        if count < 0:
            return False
        # Jika karakter pertama '(', tambah count dan lanjutkan rekursi
        if s[0] == '(':
            return helper(s[1:], count + 1)
        # Jika karakter pertama ')', kurangi count dan lanjutkan rekursi
        else:
            return helper(s[1:], count - 1)
    
    # Panggil helper dengan count awal 0
    return helper(s, 0)

# Contoh penggunaan
print(valid("(()())")) # Output: True
print(valid("(()"))    # Output: False
print(valid(")("))     # Output: False
