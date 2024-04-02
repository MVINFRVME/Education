text = 'это питон.'
shift = 3

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й',
            'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
            'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

cipher_list = [alphabet[(alphabet.index(sym) + shift) % 33] if sym in alphabet
               else sym
               for sym in text]
cipher = ''

for sym in cipher_list:
    cipher += sym
    
print(cipher)