alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'x', 'y', 'z', 'å', 'ä','ö']

test_text = 'abc'.lower()

def encryption(text, shift):
    encrypted = ''
    for char in text: 
        position = alphabet.index(char)
        new_position = position + shift
        new_letter = alphabet[new_position]
        encrypted += new_letter
    return encrypted

        
        
print(encryption(test_text, 5))