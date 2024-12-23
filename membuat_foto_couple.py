# -*- coding: utf-8 -*-
"""Membuat foto couple.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_TIpTPGgu0ZxYB7vXQF5kZ9uGGFQM5nm
"""

pip install pillow

from PIL import Image

def create_couple_image(image1_path, image2_path, output_path):
    try:
        # Membuka gambar
        img1 = Image.open(image1_path).convert("RGB")  # Konversi ke RGB
        img2 = Image.open(image2_path).convert("RGB")  # Konversi ke RGB

        # Menyesuaikan ukuran kedua gambar agar sama
        img1 = img1.resize((512, 512))
        img2 = img2.resize((512, 512))

        # Membuat canvas untuk menggabungkan kedua gambar
        result_width = img1.width + img2.width
        result_height = max(img1.height, img2.height)
        result_image = Image.new("RGB", (result_width, result_height))

        # Menempelkan gambar ke canvas
        result_image.paste(img1, (0, 0))
        result_image.paste(img2, (img1.width, 0))

        # Menyimpan hasilnya
        result_image.save(output_path)
        print(f"Foto couple berhasil dibuat: {output_path}")

    except FileNotFoundError:
        print("Error: File gambar tidak ditemukan. Pastikan path-nya benar.")
    except PermissionError:
        print("Error: Tidak memiliki izin untuk membaca atau menulis file.")
    except Exception as e:
        print(f"Error tidak terduga: {e}")

# Path gambar dan output
image1_path = "image1.jpg"  # Ganti dengan path gambar pertama
image2_path = "image2.jpg"  # Ganti dengan path gambar kedua
output_path = "couple_photo.jpg"

# Membuat foto couple
create_couple_image(image1_path, image2_path, output_path)

import os
print(f"Direktori kerja saat ini: {os.getcwd()}")