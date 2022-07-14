"""
Program pengulangan baca buku

"""

jml_buku = 15
print('Ibu berkata "Baca semua bukumu"')

jml_buku_yg_dipahami = 0
print(f"jumlah buku yang sudah dibaca adalah {jml_buku_yg_dipahami}")

while jml_buku_yg_dipahami < jml_buku:
    jml_buku_yg_dipahami = jml_buku_yg_dipahami + 1
    if jml_buku_yg_dipahami == 10:
        print(f"buku ke-{jml_buku_yg_dipahami} belum dibaca sampai paham")
    else:
        print(f"buku ke-{jml_buku_yg_dipahami} sudah dibaca dan dipahami")

print(f"jumlah buku yang sudah dibaca sekarang adalah {jml_buku_yg_dipahami}")