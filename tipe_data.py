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

