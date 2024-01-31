import operasi_file as of
file_datahotel = "datahotel.txt"
file_handler = of.FileHandler(file_datahotel)

#membaca file
isi_file = file_handler.baca_file()
print(f"isi file {file_datahotel}: {isi_file}")

#menulis file
konten_baru = "\nhi ini konten baru!"
status_tulis = file_handler.tulis_file(konten_baru, "a")
print(status_tulis)
