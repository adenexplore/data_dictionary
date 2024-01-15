siswa = {
    'nama': 'Aden',
    'umur': 18,
    'kelas': '12A',
    'nilai': {'matematika': 90, 'bahasa_inggris': 85, 'fisika': 88}
}

# Mengumpulkan hasil iterasi dalam satu string
result_string = ""
for key, value in siswa.items():
    result_string += f"{key}: {value}\n"

# Menampilkan hasil iterasi saat program ditutup
print("Informasi Siswa:")
print(result_string)
