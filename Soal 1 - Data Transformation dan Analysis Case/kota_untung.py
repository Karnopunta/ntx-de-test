import pandas as pd
from analyst import df

# Grouping dan menghitung total pendapatan per kota
total_pendapatan_per_kota = df.groupby('kota')['total_pendapatan'].sum().reset_index()

# Mengurutkan kota berdasarkan total pendapatan
kota_teruntung = total_pendapatan_per_kota.sort_values(by='total_pendapatan', ascending=False)

# Menampilkan kota yang paling menguntungkan
print("Kota yang paling menguntungkan:")
print(kota_teruntung.head(10))
