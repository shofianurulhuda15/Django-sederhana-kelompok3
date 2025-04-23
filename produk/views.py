from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

def home(request):
    """View untuk halaman beranda"""
    # Data contoh untuk produk terbaru (sebelum Anda menggunakan database)
    produk_terbaru = [
        {'id': 1, 'nama': 'Laptop ASUS ROG', 'harga': 'Rp 15.000.000', 'gambar': '/images/laptop.jpeg'},
        {'id': 2, 'nama': 'Smartphone Samsung Galaxy S21', 'harga': 'Rp 12.000.000', 'gambar': '/images/smartphone.jpeg'},
        {'id': 3, 'nama': 'Apple MacBook Pro', 'harga': 'Rp 20.000.000', 'gambar': 'images/macbook.jpeg'},
    ]
    
    # Kategori contoh
    kategori_list = [
        {'id': 1, 'nama': 'Laptop'},
        {'id': 2, 'nama': 'Smartphone'},
        {'id': 3, 'nama': 'Monitor'},
        {'id': 4, 'nama': 'Aksesoris'},
    ]
    
    context = {
        'produk_terbaru': produk_terbaru,
        'kategori_list': kategori_list,
        'judul_halaman': 'Beranda'
    }
    return render(request, 'produk/home.html', context)

def daftar_produk(request):
    """View untuk menampilkan daftar produk"""
    # Data contoh untuk produk
    produk_list = [
        {'id': 1, 'nama': 'Laptop ASUS ROG', 'harga': 'Rp 15.000.000', 'gambar': '/images/laptop.jpeg'},
        {'id': 2, 'nama': 'Smartphone Samsung Galaxy S21', 'harga': 'Rp 12.000.000', 'gambar': '/images/smartphone.jpeg'},
        {'id': 3, 'nama': 'Apple MacBook Pro', 'harga': 'Rp 20.000.000', 'gambar': '/images/macbook.jpeg'},
        {'id': 4, 'nama': 'Monitor LG 27 inch', 'harga': 'Rp 3.500.000', 'gambar': '/images/monitor.jpeg'},
        {'id': 5, 'nama': 'Keyboard Mechanical Logitech', 'harga': 'Rp 1.200.000', 'gambar': '/images/keyboard.jpeg'},
    ]
    
    # Filter berdasarkan kategori
    kategori_id = request.GET.get('kategori')
    if kategori_id:
        # Ini hanya simulasi filter. Di implementasi yang sebenarnya, 
        # Anda akan melakukan query ke database
        judul = "Produk dalam kategori tertentu"
    else:
        judul = "Semua Produk"
    
    kategori_list = [
        {'id': 1, 'nama': 'Laptop'},
        {'id': 2, 'nama': 'Smartphone'},
        {'id': 3, 'nama': 'Monitor'},
        {'id': 4, 'nama': 'Aksesoris'},
    ]
    
    context = {
        'produk_list': produk_list,
        'kategori_list': kategori_list,
        'judul_halaman': judul
    }
    return render(request, 'produk/daftar_produk.html', context)
