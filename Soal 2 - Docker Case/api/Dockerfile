# Gunakan image python
FROM python:3.11.4

# Atur direktori kerja
WORKDIR /app

# Salin file requirements.txt ke direktori kerja
COPY requirements.txt .

# Install dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin kode sumber aplikasi ke direktori kerja
COPY api.py .

# Jalankan aplikasi ketika container dijalankan
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "6000"]
