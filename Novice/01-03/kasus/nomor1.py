class siswa():
    def __init__(self,nama,alamat,umur,jenis_kelamin):
        self.nama = nama
        self.alamat = alamat
        self.umur = umur
        self.jenis_kelamin = jenis_kelamin
        print('(siswa ini namanya : {})'.format(self.nama))
    
    def tell(self):
        print('Nama: "{}" alamat:"{}"'.format(self.nama,self.alamat), end=" ")

class sekolah(siswa):
    def __init__(self,nama,alamat,no_telepon,kode_pos):
        siswa.__init__(self,nama,alamat,no_telepon,kode_pos)
        self.no_telepon = no_telepon
        self.kode_pos = kode_pos
        print('(bersekolah di : {})'.format(self.nama))
    
    def tell(self):
        siswa.tell(self)
        print('no telepon : "{}"'.format(self.no_telepon))
        print('Kode pos : "{}"'.format(self.kode_pos))

sw = siswa('nita','bantul',17,'P')
sk = sekolah('uad','bantul',123,54621)

print()

total = [sw,sk]
for anggota in total:
    anggota.tell()