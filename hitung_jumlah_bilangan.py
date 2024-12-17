
"""
programmer: Faiq Irfan Fadhlurrohim

Jurusan Teknik Elektro
Kelas IK - 1B
Prodi Teknik Informatika
Politeknik Negeri Semarang

Dibuat Pada Mon Dec 16 15:13:49 2024

"""

n = int(input('Masukkan nilai n:'))
t = 0
i = 1

if i <= n:
    while i <= n:
        t +=1
        i +=1

else:
    t = 0

print(f"Jumlah bilangan dari 1 hingga {n} adalah: {t}")