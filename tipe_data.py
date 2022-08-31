daftar_buku = ['Matematika','IPA','Bahasa Inggris']
print("\n============================\n")
print("daftar semua buku\n")
print(daftar_buku)

print("\n============================\n")
print("list semua buku\n")
for buku in daftar_buku:
    print(buku)

print("\n============================\n")
print("buku tertentu\n")
print(daftar_buku[0])
print(daftar_buku[2])


print("\n============================\n")
print("daftar semua buku menggunakan range\n")
daftar_buku2 = ("Bahasa Indonesia","IPS")
for buku2 in daftar_buku2:
    daftar_buku.append(buku2)


for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\n*CLear list*')
daftar_buku.clear()
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nGanti Elemen Pertama')
daftar_buku = ['MTK','IPA','IPS','ING','IND','PKN']
daftar_buku[0] = 'ALJBR'
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nAmbil buku elemen kedua')
buku = daftar_buku.pop(1)
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nBuku yang diambil tadi')
print(buku)


print('\npop doang')
daftar_buku.pop()
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del')
daftar_buku = ['MTK','IPA','IPS','ING','IND','PKN']
del daftar_buku[0]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del list comp')
daftar_buku = ['MTK','IPA','IPS','ING','IND','PKN']
del daftar_buku[:]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del list comp dari list kedua')
daftar_buku = ['MTK','IPA','IPS','ING','IND','PKN']
del daftar_buku[1:]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del menampilkan  genap')
daftar_buku = ['MTK','IPA','IPS','ING','IND','PKN']
del daftar_buku[1::2]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

