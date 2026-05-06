from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/produk')
def produk():
    data_produk = [
        {"nama": "E-book Digital Marketing", "deskripsi": "Belajar bisnis online dari nol", "harga": "Rp50.000"},
        {"nama": "Template Website", "deskripsi": "Website siap pakai", "harga": "Rp75.000"},
        {"nama": "Kelas Canva", "deskripsi": "Belajar desain mudah", "harga": "Rp100.000"}
    ]
    return render_template('produk.html', produk=data_produk)

@app.route('/kontak', methods=['GET', 'POST'])
def kontak():
    if request.method == 'POST':
        nama = request.form.get('nama')
        email = request.form.get('email')
        return render_template('hasil.html', nama=nama, email=email)

    return render_template('kontak.html')

if __name__ == '__main__':
    app.run(debug=True)
