import math


def kalkulator():
    lagi = True
    
    while lagi: 
        
        print("Selamat datang di Kalkulator Sederhana")
        print("Pilih operasi:")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")
        print("5. Modulus")
        print("6. Akar Kuadrat")
        print("7. Logaritma Alami")
        print("8. Logaritma Basis 10")
        print("9. Lebih Besar")
        print("10. Lebih Kecil")
        print("11. Perpangkatan")
        print("12. Keluar")

        pilihan = input("Masukkan nomor operasi yang diinginkan (1-12): ")

        if pilihan in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'):
            jumlah_operan = int(input("Masukkan jumlah operan: "))
            operan = [float(input(f"Masukkan operan ke-{i + 1}: ")) for i in range(jumlah_operan)]

        if pilihan == '1':
            hasil = sum(operan)
            print(f"Hasil penjumlahan: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")
        elif pilihan == '2':
            hasil = operan[0] - sum(operan[1:])
            print(f"Hasil pengurangan: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")

        elif pilihan == '3':
            hasil = 1
            for num in operan:
                hasil *= num
            print(f"Hasil perkalian: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")

        elif pilihan == '4':
            hasil = operan[0]
            for num in operan[1:]:
                hasil /= num
            print(f"Hasil pembagian: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")

        elif pilihan == '5':
            hasil = operan[0] % operan[1]
            print(f"Hasil modulus: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")

        elif pilihan == '6':
            hasil = operan[0] ** 0.5
            print(f"Akar kuadrat: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")

        elif pilihan == '7':
            hasil = math.log(operan[0])
            print(f"Logaritma alami: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")

        elif pilihan == '8':
            hasil = math.log10(operan[0])
            print(f"Logaritma basis 10: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")

        elif pilihan == '9':
            hasil = max(operan)
            print(f"Nilai maksimum dari operan: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")

        elif pilihan == '10':
            hasil = min(operan)
            print(f"Nilai minimum dari operan: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")

        elif pilihan == '11':
            hasil = operan[0] ** operan[1]
            print(f"Hasil perpangkatan: {hasil}")
            lanjut = input("lanjut menggunakan kalkulator? (y/n): ")
            if lanjut == "y": 
                lagi = True
            elif lanjut == "n":
                print("jazakumullah khairan katsiran")
                break
            else: 
                print("masukan salah!")

        elif pilihan == '12':
            print("Terima kasih telah menggunakan kalkulator.")
            exit()

        else:
            print("Pilihan tidak valid. Silakan pilih nomor 1-12.")
            kalkulator()

if __name__ == "__main__":
    kalkulator()
