# jantung
class Jantung(object):
    def pompa_darah(self):
        return "Jantung bertugas untuk memompa darah ke selurh tubuh"
    def atur_detak_jantung(self):
        return "Jantung bertugas untuk mengatur ritme jantung"
    
# otak
class Otak(object):
    def kendali_tubuh(self):
        return "Otak mengendalikan seluruh bagian tubuh"
    def proses_informasi(self):
        return "Otak memproses informasi yang diterima dari indera"
    
# declare
otak = Otak()
jantung = Jantung()

# tes
print(otak.kendali_tubuh())
print(otak.proses_informasi())
print(jantung.pompa_darah())
print(jantung.atur_detak_jantung())

# -------------------------------------------------=

# Organ
class Organ(object):
    def __init__(self, nama):
        self.nama = nama

    def info(self):
        return f"{self.nama} adalah organ vital"
    
class Jantung(Organ):
    def __init__(self):
        super().__init__("Jantung") # contoh = "(Jantung) adalah organ vital"
    def pompa_darah(self):
        return "Jantung bertugas untuk memompa darah ke selurh tubuh"
    def atur_detak_jantung(self):
        return "Jantung bertugas untuk mengatur ritme jantung"

class Otak(Organ):
    def __init__(self):
        super().__init__("Otak")
    def kendali_tubuh(self):
        return "Otak mengendalikan seluruh bagian tubuh"
    def proses_informasi(self):
        return "Otak memproses informasi yang diterima dari indera"

jantung = Jantung()
otak = Otak()

print(otak.info())
print(otak.kendali_tubuh())
print(otak.proses_informasi())

print(jantung.info())
print(jantung.atur_detak_jantung())
print(jantung.pompa_darah())