umur = int(input("Masukkan umur anda: ")) 

if umur < 0: 
    print("anda belum lahir") 
elif umur > 60: 
    print("banyakin ibadah, bentar lagi mati") 
elif umur >= 18: 
    print("anda cukup umur") 
else: 
    print("anda belum cukup umur") 

print("Program selesai")