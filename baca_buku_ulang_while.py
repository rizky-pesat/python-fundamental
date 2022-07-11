"""
Program pengulangan baca buku

"""

jml_buku = 100
print('Ibu berkata "Baca semua bukumu"')

jml_buku_yg_dibaca = 0
print(f"jumlah buku yang sudah dibaca adalah {jml_buku_yg_dibaca}")

while jml_buku_yg_dibaca < jml_buku:
    jml_buku_yg_dibaca = jml_buku_yg_dibaca + 1
    print(f"buku ke-{jml_buku_yg_dibaca} sudah dibaca")

print(f"jumlah buku yang sudah dibaca sekarang adalah {jml_buku_yg_dibaca}")