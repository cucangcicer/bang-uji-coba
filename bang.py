import sys

class bank:
    def __init__(self,saldo):
        self.saldo=saldo
        #self.ambil=ambil
        #self.masuk=masuk

    def saldomasuk(self):
        kampang=0
        #self.masuk=masuk
        #masuk=int(input('Masukan Jumlah Uang Yang Ingin Disetor: '))
        while True:
            try:
                masuk=int(input('Masukan uang yang ingin disetor: '))
                break
            except ValueError:
                print('Masukan Nominal Mhank !!!\n')
                kampang+=1
                if kampang>3:
                    print('YANG BENER KAMPANK !!!\n')
        self.saldo=self.saldoskr()+masuk

    def saldokeluar(self):
        kampang=0
        #self.keluar=keluar
        while True:
            try:
                ambil=int(input('Masukan uang yang ingin diambil: '))
                break
            except ValueError:
                print('Masukan Nominal Mhank !!!\n')
                kampang+=1
                if kampang>3:
                    print('YANG BENER KAMPANK !!!\n')
        if self.saldo<ambil:
            print('Saldo Anda Tidak Mencukupi\n')
        else:
            self.saldo=self.saldoskr()-ambil

    def saldoskr(self):
        return (self.saldo)
 
nasabah1=bank(0)
nasabah1.saldomasuk()
nasabah1.saldokeluar()
cetak=input('Ingin Cetak Saldo ?[y/n]: ')
if cetak=='y':
    print('Saldo sekarang adalah {}'.format(nasabah1.saldoskr()))
else:
    print('Terima kasih')


            
