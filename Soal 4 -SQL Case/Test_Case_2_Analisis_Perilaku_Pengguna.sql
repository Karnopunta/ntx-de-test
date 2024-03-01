---menggunakan CTE untuk membuat table rata-rata setiap pengunjung  
---dan tabel rata-rata keseluruhan pengunjung

with rata2_per_pengunjung as ( 
	--- membuat tabel rata-rata untuk setiap pengunjung
    select
    	-- Menghitung rata-rata kunjungan setiap pengunjung
        "fullVisitorId" id_pengunjung,
        AVG("timeOnSite") rata2_time_on_site,
        AVG(pageviews) rata2_pageviews,
        AVG("sessionQualityDim") rata2_session_quality
    from 
        public.data_ecommerce
    group by
    	--- id_pengunjung dijadikan acuan untuk mengelompokkan metriknya
        id_pengunjung
),
--membuat table rata-rata untuk seluruh pengunjung
rata2_keseluruhan as (
    select
    	-- Menghitung rata-rata keseluruhan dari semua pengunjung
        AVG("timeOnSite") rata2_seluruh_time_on_site,
        AVG(pageviews) rata2_seluruh_pageviews,
        AVG("sessionQualityDim") rata2_session_quality
    from 
        public.data_ecommerce
)
--- membuat tabel baru dimana kolom-kolomnya diambil dari table rata2_per_pengunjung 
--- dan table rata2_keseluruhan 
select
    rp.id_pengunjung,
    rp.rata2_time_on_site,
    rp.rata2_pageviews,
    rp.rata2_session_quality
from 
    rata2_per_pengunjung rp
---Menggabungkan kedua table dengan 
join
    rata2_keseluruhan rk on 1=1
where
	-- Hanya memilih data dengan rata-rata waktu di situs di atas rata-rata keseluruhan
    -- dan rata-rata jumlah tampilan halaman di bawah rata-rata keseluruhan
    rp.rata2_time_on_site > rk.rata2_seluruh_time_on_site
    and rp.rata2_pageviews < rk.rata2_seluruh_pageviews
--hanya menampilkan 10 baris teratas
limit 10;
