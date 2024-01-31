class FileHandler:
    def __init__(self, file_datahotel):
        self.file_datahotel = file_datahotel

    def baca_file(self):
        try:
            with open(self.file_datahotel, 'r') as file:
              konten = file.read()
              return konten
            
        except FileNotFoundError:
           return f"file {self. file_datahotel} tidak ditemukan" 

    def tulis_file(self, konten, mode):
        with open(self.file_datahotel, mode) as file:
            file.write(konten)
            file.write(mode)
        return f"file{self.file_datahotel} berhasil ditemukan "          