print('\n====ALAT KONVERSI TEMPERATUR====\n')

fahrenheit = float(input('1.Masukkan nilai temperatur fahrenheit: '))

celcius = 5 / 9 * (fahrenheit - 32)
print('-Nilai temperatur dalam celcius adalah: ', celcius)

reamur = 4 / 9 * (fahrenheit - 32)
print('-Nilai temperatur dalam r/eamur adalah: ', reamur)

kelvin = celcius + 273
print('-Nilai temperatur dalam kelvin adalah: ', kelvin)

kelvin = float(input('\n2.Masukkan nilai temperatur kelvin: '))

celcius = kelvin - 273 
print('-Nilai temperatur dalam celcius adalah: ', celcius)

reamur = 4 / 5 * celcius
print('-Nilai temperatur dalam reamur adalah: ', reamur)

fahrenheit = 9 / 5 * celcius
print('-Nilai temperatur dalam fahrenheit adalah: ', fahrenheit)



