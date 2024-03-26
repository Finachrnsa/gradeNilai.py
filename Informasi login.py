# Informasi login
username = "admin"
password = "Admin"

# Meminta input dari pengguna
input_username = input("Masukkan username: ")
input_password = input("Masukkan password: ")

# Memeriksa kecocokan username dan password
if input_username == username and input_password == password:
    print("Selamat datang,", username)
    print("Password anda adalah", password)
    login_status = True
else:
    print("Login gagal. Silakan coba lagi.")
    login_status = False

# Menampilkan pesan sesuai status login
if login_status:
    print("Login berhasil.")
else:
    print("Login berhasil.")
