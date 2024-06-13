#1 Eliminar los espacio en blanco de una sring y devolver una lista con los caracteres restantes


string = "Hello World im here!"

def eliminate_spaces(chars):
    chars = list(chars)
    for char in chars:
        char_list = [char for char in chars if char != " "]
        # print(char_list)
    return char_list
    

print(eliminate_spaces(string)) 