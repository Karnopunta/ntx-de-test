import pandas as pd
import matplotlib.pyplot as plt
from analyst import df

# Menghitung deviasi standar untuk setiap produk (transaksi - transaksi_rata2)
std_deviasi_per_produk = df.groupby('nama_produk')['transactions'].std()
# Mengurutkan produk berdasarkan deviasi
produk_teratas = std_deviasi_per_produk.nlargest(5)

# Buat DataFrame kosong untuk menyimpan data produk dengan anomali
data_anomali = pd.DataFrame(columns=['Nama Produk', 'Jumlah Transaksi'])

# Set untuk melacak produk yang sudah ditambahkan
produk_tertambah = set()

# Loop untuk memilih 5 produk teratas
for produk_tertentu in produk_teratas.index:
    if produk_tertentu not in produk_tertambah:  # Memastikan produk belum ditambahkan sebelumnya
        # Filter data untuk produk tertentu
        df_produk_tertentu = df[df['nama_produk'] == produk_tertentu]

        # Identifikasi anomali
        mean_transactions = df_produk_tertentu['transactions'].mean()
        std_transactions = df_produk_tertentu['transactions'].std()
        threshold_upper = mean_transactions + 2 * std_transactions
        anomalies = df_produk_tertentu[df_produk_tertentu['transactions'] > threshold_upper]
        df_produk_tertentu = df_produk_tertentu.sort_values(by='Tanggal')


        if not anomalies.empty:  # Jika ada anomali
            # Tambahkan data produk dengan anomali ke DataFrame
            data_anomali = pd.concat([data_anomali, pd.DataFrame({'Nama Produk': [produk_tertentu],
                                                                  'Jumlah Transaksi': [anomalies['transactions'].iloc[0]]})],
                                                                  ignore_index=True)
            # Tandai produk sebagai sudah ditambahkan
            produk_tertambah.add(produk_tertentu)
        # Plot jumlah transaksi terhadap waktu untuk semua produk dengan anomali
        plt.figure(figsize=(10, 6))
        plt.plot(df_produk_tertentu['Tanggal'], df_produk_tertentu['transactions'], marker='o', linestyle='-')
        plt.title('Jumlah Transaksi untuk Produk: ' + produk_tertentu)
        plt.xlabel('Tanggal')
        plt.ylabel('Jumlah Transaksi')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()

# Tampilkan tabel produk dengan anomali
print("Tabel Produk dengan Anomali:")
print(produk_teratas)
