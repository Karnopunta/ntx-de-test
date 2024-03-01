--- menggunakan CTE untuk memilih 5 top_countries dengan total pendapatan terbesar
with top_countries as (
    select 						---masukkan kolom yang ingin ditampilkan
        country,
        SUM("totalTransactionRevenue") total_pendapatan
    from 
        public.data_ecommerce 	--sumber database
    group by 
    	country 				---mengelompokkan pendapatan berdasarkan kolom country
    order by 
    	total_pendapatan  		---mengurutkan data berdasarkan kolom pendapatan
    desc 				  		---urutan dimulai dari yang terbesar ke kecil
    limit 5				  		---memilih 5 baris teratas
),
total_pendapatan_per_channel as (	---membuat tabel pendapatan 
    select							---memasukkan kolom yang akan ditampilkan
        "channelGrouping",
        country,
        SUM("totalTransactionRevenue") total_pendapatan --menjumlah kolom totalTransactionRevenue
    from 
        public.data_ecommerce
    where							---country dipilih dari table top_countries yang dibuat diatas
        country in (select country from top_countries)
    group by
        "channelGrouping",  ---mengelompokkan kolom totalTransactionRevenue dengan channelGrouping
        country			    ---dan country yang sama
)
select 						---memilih kolom yang akan ditampilkan
    "channelGrouping",		
    country,
    SUM(total_pendapatan) total_pendapatan
from 
    total_pendapatan_per_channel
group by 					---mengelompokkan pendapatan berdasarkan kolom channerGrouping dan country
    "channelGrouping",  
    country
order by 					---mengurutkan baris berdasarkan kolom total_pendapatan
    total_pendapatan desc 	--mengurutkan dari terbesar ke kecil
limit 15;
