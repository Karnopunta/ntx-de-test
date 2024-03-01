# Gunakan python:3.11.4 sebagai base image
FROM python:3.11.4

# Menyimpan direktori kerja
WORKDIR /app

# Menyalin file requirements.txt ke direktori kerja
COPY requirements.txt .

# Menginstal dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin kode sumber aplikasi ke direktori kerja
COPY etl.py .

# Menambahkan perintah untuk menunggu kontainer API siap sebelum memulai
CMD ["python", "etl.py"]
