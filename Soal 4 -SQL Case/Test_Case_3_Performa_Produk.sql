--- Test Case 3: Performa Produk
--- menghitung total pendapatan yang dihasilkan oleh setiap produk
select 
    "v2ProductName" nama_produk,
    SUM("totalTransactionRevenue") total_pendapatan,	---sum() digunakan untuk menjumlahkan nilai didalam kolom
    SUM("productQuantity") kuantitas_terjual,
    SUM("productRefundAmount") pengembalian,
    (SUM("totalTransactionRevenue") - SUM("productRefundAmount")) pendapatan_bersih,
    case 
	    --- mendefinikan pengembalian lebih besar dari 10%
        when SUM("productRefundAmount") > 0.1 * SUM("totalTransactionRevenue") 
        then 'Ya'									--- jika hasilnya ya maka print ya
        else 'Tidak'								--- jika tidak maka print tidak
    end jumlah_pengembalian_lebih_dari_10_persen 	--- nama kolom 
from 
    public.data_ecommerce 							---sumber data
group by 											---mengelompokkan berdasarkan nama produk
    "v2ProductName"
order by 											---mengurutkan berdasarkan kolom total_pendapatan
    kuantitas_terjual desc;							---urutan menurun
