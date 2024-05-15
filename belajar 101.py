a = 10
b = 2 * a
c = b // 4
d = a ** c
e = 10.4

print('Nilai a + b + c + d adalah ', a + b + c + d)

#apakah anda sudah umur 18 tahun?
trueOrFalse = input('Apakah anda sudah berumur 18 tahun? Iya/Tidak')
if trueOrFalse == str('Iya'):
    print('Selamat, anda telah menginjak masa dewasa')
if trueOrFalse == str('Tidak'):
    print('Mohon maaf, anda belum cukup umur')

x = 0
while x <= 50:
    print(x)
    x += 5
if x == 50:
    print(x)
range(1, 10)