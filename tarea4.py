def es_palindromo():
    conteo = 0
    for x in range(24):
        for y in range(60):
            pal = str(x).zfill(2) + ':' + str(y).zfill(2) 
            if pal == pal[::-1]:
                print(f'{pal}')
                conteo += 1
    print(f'Hay {conteo} palindromos')
    
palindromo = es_palindromo()
