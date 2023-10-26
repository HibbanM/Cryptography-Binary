kunci = 'abcdefghijklmnopqrstuvwxyz'

def enc_cryp(n, pesan) :
    print (pesan)
    # kript dengan caesar
    isi_pesan = ''
    for l in pesan.lower():
        try:
            i = (kunci.index(l) + n) % 26
            isi_pesan += kunci[i]
        except ValueError:
            isi_pesan += l
        isi_pesan = isi_pesan.lower()
    print (isi_pesan)
    # kript dengan binary
    kript_pesan = isi_pesan.encode("utf-8")
    kript_pesan_biner = ''.join(format(byte, '08b') for byte in kript_pesan)
    print(kript_pesan_biner)

def dec_cryp(n, pesan_enkripsi) :
    print (pesan_enkripsi)
    # Split pesan_enkripsi ke bentuk 8-bit
    chunks_pesan = [pesan_enkripsi[i:i+8] for i in range(0, len(pesan_enkripsi), 8)]

    # Convert 8-bit ke integer
    nilai_integer = [int(chunk, 2) for chunk in chunks_pesan]

    # Create a bytes object from the integer values
    nilai_bytes = bytes(nilai_integer)

    # Decode the bytes object using UTF-8 encoding to obtain the original string
    dekript_pesan = nilai_bytes.decode("utf-8")

    print(dekript_pesan)
    isi_pesan = ''
    for l in dekript_pesan:
        try:
            i = (kunci.index(l) - n) % 26
            isi_pesan += kunci[i]
        except ValueError:
            isi_pesan += l
        isi_pesan = isi_pesan.lower()
    print(isi_pesan)

enc_cryp(6, "hai")
dec_cryp(6,"011011100110011101101111")
