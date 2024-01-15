# Membuat dictionary
siswa = {
    'nama': 'Aden',
    'umur': 20,
    'kelas': '1A',
    'nilai': {'matematika': 90, 'bahasa_inggris': 85, 'fisika': 88}
}

# Menampilkan informasi siswa
print("Nama:", siswa['nama'])
print("Umur:", siswa['umur'])
print("Kelas:", siswa['kelas'])

# Menampilkan nilai mata pelajaran
print("Nilai Matematika:", siswa['nilai']['matematika'])
print("Nilai Bahasa Inggris:", siswa['nilai']['bahasa_inggris'])
print("Nilai Fisika:", siswa['nilai']['fisika'])