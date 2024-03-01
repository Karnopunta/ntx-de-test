import pandas as pd

# extract data dari file CSV ke dalam DataFrame
df = pd.read_csv('ecommerce-session-bigquery.csv') 
#mengubah format tanggal 
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
# mengganti nama kolom
df.rename(columns={'date': 'Tanggal',
                    'v2ProductName': 'nama_produk',
                    'fullVisitorId': 'ID_pengunjung',
                    'totalTransactionRevenue': 'total_pendapatan',
                    'city': 'kota'}, inplace=True)

#mengelompokkan data berdasarkan kolom "tanggal" dan "nama_produk" 
#selanjutnya menjumlahkan hasil agregat kolom "total_pendapatan"
total_pendapatan_per_hari = df.groupby(['Tanggal', 'nama_produk'])['total_pendapatan'].sum().reset_index()

# menampilkan satu produk dengan total transaksi per hari teratas 
produk_teratas_per_tanggal = total_pendapatan_per_hari.loc[total_pendapatan_per_hari.groupby('Tanggal')['total_pendapatan'].idxmax()]
# Mengubah format angka total pendapatan
produk_teratas_per_tanggal['total_pendapatan'] = produk_teratas_per_tanggal['total_pendapatan'].map('RP. {:,.2f}'.format)
# Menampilkan produk teratas per hari
print( " ")
print("total pendapatan produk terbanyak per hari")
print("disini saya hanya menampilkan satu produk disetiap tanggal dengan ketentuan yaitu produk dengan total pendapatan transaksi terbanyak")
print( " ")
print(produk_teratas_per_tanggal.head(20))


# mencari produk dengan transaksi terbesar
# Mengelompokkan data berdasarkan tanggal dan produk, kemudian menghitung total pendapatan transaksi per hari
total_pendapatan_per_produk = df.groupby(['Tanggal','nama_produk'])['total_pendapatan'].sum().reset_index()
# Mengurutkan produk berdasarkan total pendapatan transaksi
produk_teratas = total_pendapatan_per_produk.sort_values(by='total_pendapatan', ascending=False)
# Menampilkan 5 produk teratas
print(" ")
print("menampilkan produk dengan transaksi terbanyak per hari")
print(produk_teratas.head())