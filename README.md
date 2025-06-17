# Proyek Akhir Semantic Web

Aplikasi web pembelajaran Aksara Kawi berbasis semantik web yang menggunakan SPARQL dan Streamlit.

## 📋 Daftar Isi
- [Deskripsi Proyek](#deskripsi-proyek)
- [Instalasi](#instalasi)
- [Cara Menjalankan Aplikasi](#cara-menjalankan-aplikasi)
- [Panduan Penggunaan](#panduan-penggunaan)
- [Hasil Applikasi](#Hasil-Applikasi)
  

---

## 📖 Deskripsi Proyek

Aplikasi ini memungkinkan pengguna untuk:
- Mencari arti aksara Kawi berdasarkan input keyboard visual
- Mencari transliterasi dari teks Latin ke Aksara Kawi
- Mencari arti kata berbahasa Indonesia dari dataset berbasis RDF

---
## Link Deploy Website
Applikasi sudah full di deploy pada link dibawah sehingga tidak perlu melakukan instalasi apapun

https://aksara-kebon-kopi-2.streamlit.app/

## ⚙️ Instalasi

1. **Install Java JDK versi terbaru**
2. **Install Apache Jena**
   - Unduh dari: [https://jena.apache.org/download/index.cgi](https://jena.apache.org/download/index.cgi)
3. Jalankan Apache Jena Fuseki:
   ```bash
   fuseki-server --update --mem /ds
4. **Akses Apache Jena pada browser**
   - [http://localhost:3030/]( http://localhost:3030/)
5. Masuk page dataset untuk melihat daftar dataset
   ![1](https://github.com/user-attachments/assets/1fc6f256-2940-4f39-8356-5da763c94784)

6. Klik Manage pada navbar dan klik new dataset untuk membuat dataset baru
   ![2](https://github.com/user-attachments/assets/834bd81f-bf50-4494-a141-22565f481b14)

7. Beri nama projekSemweb pada kolom DatasetName
    ![3](https://github.com/user-attachments/assets/50079cf0-ddc4-4fe1-8317-94f84aeb6588)

8. Lakukan addData pada dataset yang sudah kita buat dan masukan file **prasasti_aksara_kawi.ttl**
    ![4](https://github.com/user-attachments/assets/4d1ad6c2-9ea4-4cad-8c2b-1e36a031706e)

9. Buka folder pada Vscode dan jalankan command 
      **a. Pip install streamlit**
      **b. Pip install SPARQLWrapper**
   
10. Buka terminal dan jalankan command **streamlit run main_app.py** pada terminal

## Panduan Penggunaan

1. Home Page
![5](https://github.com/user-attachments/assets/dd590b8f-b305-4e5e-9c0c-882c26be5520)

2. User dapat memilih sesuai kebutuhan pengguna
![6](https://github.com/user-attachments/assets/bd164d57-101a-47e0-b4a9-61195bae952c)

3. Jika memilih cari berdasarkan Aksara Kawi, masukan aksara dengan cara memilih aksara pada keyboard kawi yang sudah di    sediakan
![7](https://github.com/user-attachments/assets/99bb97cb-facc-4bbb-be98-884dd760d392)
![8](https://github.com/user-attachments/assets/73a88689-52db-4a04-a0e0-13b4997c9ccf)
![9](https://github.com/user-attachments/assets/34b9a9d0-0971-4742-8c7a-82614a9d985f)
![10](https://github.com/user-attachments/assets/f53292d2-e006-4816-ae7f-ac14bc19e876)

4. Aksara yang di klik akan muncul pada bagian sidebar di sisi kiri dan terdapat 2 tombol bantuan untuk menghapus jika terjadi kesalahan
   
![11](https://github.com/user-attachments/assets/55e97252-b36e-4dd6-8d22-83ebb0a5544a)

5. Jika akasara yang dirasa sudah benar silahkan klik tombol “cari aksara kawi di database”
![12](https://github.com/user-attachments/assets/4c23bf57-2d18-42e4-89c2-b55c40f888ac)

6. Untuk Transliterasi dari bahasa latin, dapat langsung mengetik di bagian yang sudah disediakan dan terdapat 2 tombol untuk menghapus dan juga mencari arti pada dataset

![16](https://github.com/user-attachments/assets/8f5e7817-d8e0-41fa-a581-8086cfc7ed65)

7. Untuk mencari arti dari bahasa indonesia,dapat langsung mengetik di bagian yang sudah disediakan dan terdapat 2 tombol untuk menghapus dan juga mencari arti pada dataset

## Hasil Applikasi
![13](https://github.com/user-attachments/assets/1379a993-b8f1-409d-85af-be2048d4acdd)
![14](https://github.com/user-attachments/assets/0dd64a36-df7d-4e6e-9cf9-7a27e6b5ae65)
![15](https://github.com/user-attachments/assets/d8b0b2bc-337b-4782-9a21-90f16766f0f8)



