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

def detail_produk(request, id):
    """View untuk menampilkan detail produk"""
    # Kamus produk sederhana untuk demo
    produk_dict = {
        1: {
            'id': 1,
            'nama': 'Laptop ASUS ROG',
            'harga': 'Rp 15.000.000',
            'deskripsi': 'Laptop gaming dengan performa tinggi, dilengkapi dengan prosesor Intel Core i7 dan kartu grafis NVIDIA RTX 3070.',
            'gambar': '/produk/images/laptop.jpeg',
            'spesifikasi': [
                'Prosesor: Intel Core i7',
                'RAM: 16GB DDR4',
                'SSD: 1TB',
                'Grafis: NVIDIA RTX 3070',
                'Layar: 15.6 inch, 144Hz'
            ]
        },
        2: {
            'id': 2,
            'nama': 'Smartphone Samsung Galaxy S21',
            'harga': 'Rp 12.000.000',
            'deskripsi': 'Smartphone premium dengan kamera beresolusi tinggi dan layar Super AMOLED 6.2 inch.',
            'gambar': '/produk/images/smartphone.jpeg',
            'spesifikasi': [
                'Layar: 6.2 inch Super AMOLED',
                'Prosesor: Exynos 2100',
                'RAM: 8GB',
                'Penyimpanan: 128GB',
                'Kamera: 64MP + 12MP + 12MP'
            ]
        },
        3: {
            'id': 3,
            'nama': 'Apple MacBook Pro',
            'harga': 'Rp 20.000.000',
            'deskripsi': 'Laptop premium untuk kreator konten, dilengkapi dengan chip M1 Pro dan layar Retina display.',
            'gambar': '/produk/images/macbook.jpeg',
            'spesifikasi': [
                'Chip: Apple M1 Pro',
                'RAM: 16GB',
                'SSD: 512GB',
                'Layar: 14 inch Retina XDR',
                'Battery: Up to 17 hours'
            ]
        },
        4: {
            'id': 4,
            'nama': 'Monitor LG 27 inch',
            'harga': 'Rp 3.500.000',
            'deskripsi': 'Monitor dengan panel IPS, resolusi 4K, dan refresh rate 144Hz untuk pengalaman visual yang optimal.',
            'gambar': '/produk/images/monitor.jpeg',
            'spesifikasi': [
                'Ukuran: 27 inch',
                'Resolusi: 4K UHD (3840 x 2160)',
                'Panel: IPS',
                'Refresh Rate: 144Hz',
                'Response Time: 1ms'
            ]
        },
        5: {
            'id': 5,
            'nama': 'Keyboard Mechanical Logitech',
            'harga': 'Rp 1.200.000',
            'deskripsi': 'Keyboard gaming dengan switch mechanical untuk kenyamanan mengetik dan responsivitas tinggi.',
            'gambar': '/produk/images/keyboard.jpeg',
            'spesifikasi': [
                'Switch: Logitech GX Blue Clicky',
                'Tipe: Mechanical',
                'Backlight: RGB',
                'Koneksi: USB-C',
                'Layout: TKL (Tenkeyless)'
            ]
        }
    }
    
    produk = produk_dict.get(id)
    
    if produk:
        # Data contoh untuk produk terkait
        produk_terkait = [
            {'id': 3, 'nama': 'Apple MacBook Pro', 'harga': 'Rp 20.000.000', 'gambar': '/produk/images/macbook.jpeg'},
            {'id': 5, 'nama': 'Keyboard Mechanical Logitech', 'harga': 'Rp 1.200.000', 'gambar': '/produk/images/keyboard.jpeg'},
        ]
        
        context = {
            'produk': produk,
            'produk_terkait': produk_terkait,
            'judul_halaman': produk['nama']
        }
        return render(request, 'produk/detail_produk.html', context)
    else:
        context = {
            'judul_halaman': 'Produk Tidak Ditemukan'
        }
        # Anda bisa membuat template khusus untuk error, atau gunakan template yang ada
        return render(request, 'produk/404.html', context, status=404)

def kontak(request):
    """View untuk halaman kontak"""
    pesan_sukses = None
    
    if request.method == 'POST':
        # Handle form submission
        nama = request.POST.get('nama', '')
        email = request.POST.get('email', '')
        pesan = request.POST.get('pesan', '')
        
        # Simulasi pengiriman pesan sukses
        pesan_sukses = "Pesan Anda telah berhasil dikirim. Kami akan segera menghubungi Anda."
    
    context = {
        'judul_halaman': 'Kontak Kami',
        'pesan_sukses': pesan_sukses
    }
    return render(request, 'produk/kontak.html', context)

def cari_produk(request):
    """View untuk pencarian produk"""
    query = request.GET.get('q', '')
    
    # Data contoh untuk simulasi pencarian
    if query:
        produk_list = [
            {'id': 1, 'nama': 'Laptop ASUS ROG', 'harga': 'Rp 15.000.000', 'gambar': '/static/produk/images/laptop.jpeg'},
            {'id': 3, 'nama': 'Apple MacBook Pro', 'harga': 'Rp 20.000.000', 'gambar': '/static/produk/images/macbook.jpeg'},
        ]
    else:
        produk_list = []
    
    context = {
        'produk_list': produk_list,
        'query': query,
        'judul_halaman': f'Hasil Pencarian: {query}'
    }
    return render(request, 'produk/daftar_produk.html', context)
