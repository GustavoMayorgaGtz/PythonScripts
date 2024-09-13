if __name__ == '__main__':
    s = str(input())

    # Comprobar y mostrar si la cadena tiene caracteres alfanuméricos
    print(any(char.isalnum() for char in s))

    # Comprobar y mostrar si la cadena tiene caracteres alfabéticos
    print(any(char.isalpha() for char in s))

    # Comprobar y mostrar si la cadena tiene dígitos
    print(any(char.isdigit() for char in s))

    # Comprobar y mostrar si la cadena tiene caracteres en minúscula
    print(any(char.islower() for char in s))

    # Comprobar y mostrar si la cadena tiene caracteres en mayúscula
    print(any(char.isupper() for char in s))
