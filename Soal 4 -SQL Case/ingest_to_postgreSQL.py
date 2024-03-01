# memanggil library yang dibutuhkan
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.types import String, DateTime, Integer, Float

# membuat fungsi untuk ekstrak data dari csv
def get_dataframe():
    df = pd.read_csv("ecommerce-session-bigquery.csv", sep=",")
    return df

# membuat fungsi untuk memanipulasi data
def get_manipulate_data(df):
    # Memastikan nilai kolom numerik tidak memiliki nilai null
    df['totalTransactionRevenue'] = df['totalTransactionRevenue'].fillna(0).astype(float)
    df['transactions'] = df['transactions'].fillna(0).astype(int)
    df['timeOnSite'] = df['timeOnSite'].fillna(0).astype(int)
    df['pageviews'] = df['pageviews'].fillna(0).astype(int)
    df['productRefundAmount'] = df['productRefundAmount'].fillna(0).astype(int)
    df['productQuantity'] = df['productQuantity'].fillna(0).astype(int)
    df['productPrice'] = df['productPrice'].fillna(0).astype(int)
    df['productRevenue'] = df['productRevenue'].fillna(0).astype(int)
    df['itemQuantity'] = df['itemQuantity'].fillna(0).astype(int)
    df['itemRevenue'] = df['itemRevenue'].fillna(0).astype(int)
    df['transactionRevenue'] = df['transactionRevenue'].fillna(0).astype(int)
    df['sessionQualityDim'] = df['sessionQualityDim'].fillna(0).astype(int)
    
    # Memastikan kolom tanggal memiliki tipe data yang sesuai
    df['time'] = pd.to_datetime(df['time'])
    df['date'] = pd.to_datetime(df['date'])
    
    # Mengubah tipe data kolom string
    string_columns = ['fullVisitorId','visitId', 'channelGrouping', 'country', 'city', 'sessionQualityDim',
                      'type', 'productSKU', 'v2ProductName', 'v2ProductCategory', 'productVariant',
                      'currencyCode', 'transactionId', 'pageTitle', 'searchKeyword', 'pagePathLevel1',
                      'eCommerceAction_type', 'eCommerceAction_step', 'eCommerceAction_option']
    for col in string_columns:
        df[col] = df[col].astype(str)
    return df

# Menginisialisasi koneksi ke database PostgreSQL menggunakan SQLAlchemy
def get_postgres_conn():
    user = 'postgres'
    password = 'admin'
    host = 'localhost'
    database = 'mydb'
    port = 5432
    conn_string = f'postgresql://{user}:{password}@{host}:{port}/{database}'
    engine = create_engine(conn_string)
    return engine

#Menyiapkan skema DataFrame dan memuatnya ke dalam database PostgreSQL
def load_to_postgres(engine, clean_data):
    df_schema = {
            'fullVisitorId': String,
            'channelGrouping': String,
            'time': DateTime,
            'country': String,
            'city': String,
            'totalTransactionRevenue': Float, 
            'transactions': Integer,
            'timeOnSite': Integer,
            'pageviews': Integer,
            'sessionQualityDim': Integer,
            'date': DateTime,  
            'visitId': String,
            'type': String,
            'productRefundAmount': Integer,  
            'productQuantity': Integer,
            'productPrice': Integer,  
            'productRevenue': Integer,
            'productSKU': String,
            'v2ProductName': String,
            'v2ProductCategory': String,
            'productVariant': String,
            'currencyCode': String,
            'itemQuantity': Integer,
            'itemRevenue': Integer,
            'transactionRevenue': Integer,
            'transactionId': String,
            'pageTitle': String,
            'searchKeyword': String,
            'pagePathLevel1': String,
            'eCommerceAction_type': String,
            'eCommerceAction_step': String,
            'eCommerceAction_option': String
        }
    clean_data.to_sql(name='data_ecommerce', con=engine, if_exists='replace', index=False, schema='public', dtype=df_schema, method=None, chunksize=20000)

# Membaca data dari file CSV
df = get_dataframe()
print('-------------------------------------')
# membersihkan data  
clean_data = get_manipulate_data(df)
# mendapatkan koneksi ke database
postgres_conn = get_postgres_conn()
print(postgres_conn)
# memuat data ke dalam database
load_to_postgres(postgres_conn, clean_data)