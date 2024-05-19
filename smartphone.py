import numpy as np

# Langkah 1: Definisikan matriks keputusan
# Alternatif (baris) dan Kriteria (kolom)
matriks_keputusan = np.array([
    [3, 4000, 12],
    [4, 4500, 16],
    [5, 4200, 13],
    [6, 5000, 20]
])

# Langkah 2: Hitung solusi rata-rata untuk setiap kriteria
solusi_rata_rata = np.mean(matriks_keputusan, axis=0)

# Langkah 3: Hitung PDAS dan NDAS
pdas = np.maximum(matriks_keputusan - solusi_rata_rata, 0)
ndas = np.maximum(solusi_rata_rata - matriks_keputusan, 0)

# Langkah 4: Normalisasi PDAS dan NDAS
pdas_ternormalisasi = pdas / np.max(pdas, axis=0)
ndas_ternormalisasi = ndas / np.max(ndas, axis=0)

# Definisikan bobot untuk kriteria
bobot = np.array([0.4, 0.3, 0.3])  # Bobot: Harga, Kapasitas Baterai, Kamera

# Langkah 5: Hitung jumlah tertimbang
pdas_tertimbang = np.dot(pdas_ternormalisasi, bobot)
ndas_tertimbang = np.dot(ndas_ternormalisasi, bobot)

# Langkah 6: Hitung skor penilaian
skor_penilaian = (pdas_tertimbang + (1 - ndas_tertimbang)) / 2

# Langkah 7: Urutkan alternatif
peringkat = np.argsort(skor_penilaian)[::-1]  # Urutkan dalam urutan menurun

# Output hasil
for i, rank in enumerate(peringkat):
    print(f"Smartphone {rank + 1}: Skor = {skor_penilaian[rank]:.4f}")

# Cetak peringkat akhir
print("\nPeringkat Akhir (dari terbaik ke terburuk):")
for i, rank in enumerate(peringkat):
    print(f"Peringkat {i + 1}: Smartphone {rank + 1}")
