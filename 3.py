#-----3++++++1-----

# input = float(input('Masukkan angka bernilai kurang dari 3 atau lebih dari 10: '))
# if input < 3 or input > 10:
#     print(True)
# else:
#     print(False)

# input = float(input('Masukkan angka bernilai kurang dari 3 atau lebih dari 10: '))
# nilai = input < 3 or input > 10
# print(nilai)

#-----3++++++10------

# input = float(input('Masukkan angka yang bernilai di antara 3 dan 10: '))
# hasil = 3 < input < 10
# print(hasil)

#-----0+++++5-----8+++++11-----
inputUser = float(input('Masukkan angka yang bernilai di antara 0 sampai 5 atau 8 sampai 11: '))

nolSampaiLima = 0 < inputUser < 5
print('Di antara 0 sampai 5: ',nolSampaiLima)
delapanSampaiSebelas = 8 < inputUser < 11
print('Di antara 8 sampai 11: ',delapanSampaiSebelas)
hasil = nolSampaiLima or delapanSampaiSebelas
print('Kualitas simpulan: ',hasil)




#+++++0-----5+++++8-----11+++++
inputUser = float(input('Masukkan angka yang bernilai kurang dari 0, 5 sampai 8, atau lebih dari 11: '))

kurangDariNol = inputUser < 0
print('Kurang dari 0: ',kurangDariNol)
limaSampaiDelapan = 5 < inputUser < 8
print('Di antara 5 sampai 8: ',limaSampaiDelapan)
lebihDariSebelas = inputUser > 11
print('Lebih dari 11: ',lebihDariSebelas)
hasil = kurangDariNol or limaSampaiDelapan or lebihDariSebelas
print('Kualitas Simpulan: ',hasil)