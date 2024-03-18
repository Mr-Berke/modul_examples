def harf_kontrol(x):
    if x.isalpha() == True:
        print("karakter harftir")
    else:
        print("karakter harf değildir")


def kucult(x):
    if x.isalpha() == True:
        x = x.lower()
        print(x)
    else:
        print("harf giriniz!!")


def frekans_hesapla(ornek):

    metin = ""
    for karakter in ornek:
        if karakter.isalpha():
            metin += karakter

    metin = metin.lower()
    metin = metin.replace(" ", "")
    sozluk = {}
    metin = metin[:101]

    for kelime in metin:
        if kelime in sozluk:
            sozluk[kelime] += 1
        else:
            sozluk[kelime] = 1

    print("\nİlk 100 Kelimenin Frekansı (% olarak)\n")
    print(sozluk)

def hakkımda():
    print("211213011\nBerke TOPBAŞ\n")