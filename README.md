# DATA

Data terdiri dari 2 sumber berbeda yang berbentuk Json

sumber pertama data covid-19 : "https://storage.googleapis.com/dqlab-dataset/covid19_worldwide_2020.json"

sumber kedua data negara dan kode negara : "https://storage.googleapis.com/dqlab-dataset/country_details.json"

# Extract dan Transform
data di extract menggunakan library pandas

data di gabungkan menggunakan fuction merge 

# Denormalisasi

# kasus di dunia
fatal ratio digunakan untuk menentukan tingkat resiko penyebaran covid-19 disuatu negara. kolom fatal ratio dibuat dari hasil pembagian antara jumlah kematian dengan kasus yang tercatat perhari.

# kasus di asean
untuk menampilkan kasus yang terjadi di asean, kita perlu menyaring data yang ada. ini akan mudah jika kita menyaring menggunakan kode negara (geo_id) dengan hanya mengambil geo_id asean.

# visualisasi
![Grafik_dunia](dunia/Grafik_dunia.png)
![Grafik_kasus_asean](asean/Grafik_kasus_asean.png)






