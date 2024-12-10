import os
import glob
import random
import string
from numpy import sin, linspace, pi
import matplotlib.pyplot as plt

# Fungsi untuk membuat grafik sine
def sine_plot(A, B, C):
    # Generate nama file secara acak
    fname = "static/" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)) + ".png"

    # Membuat data untuk grafik
    x = linspace(0, 4 * pi, 500)
    y = (A * sin(B * x)) + C

    # Plot grafik
    plt.figure()
    plt.plot(x, y)
    plt.title(f"Sine wave with A={A}, B={B}, C={C}")

    # Cek apakah direktori 'static' ada
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        # Hapus file PNG lama di direktori 'static'
        for filename in glob.glob(os.path.join('static', '*.png')):
            os.remove(filename)

    # Simpan grafik ke file
    plt.savefig(fname)
    plt.close()  # Tutup figure untuk menghemat memori

    return fname
