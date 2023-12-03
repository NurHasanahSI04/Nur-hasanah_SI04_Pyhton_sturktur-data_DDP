#1
def lulus_saja(hasil_akhir):
    peserta_lulus = []
    for data in hasil_akhir:
        if data['nilai'] > 65:
            peserta_lulus.append(data['nama'])
    return print(peserta_lulus)
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40},
]
lulus_saja(hasil_akhir)

#2
def balikan(buah):
    index = len(buah)
    list_buah = []
    for i in buah:
        index -= 1
        print(buah[index])
        

balikan(['pepaya' , 'mangga', 'pisang', 'durian','jambu'])

#3
def duplikasi(buah):
    index = len(buah)
    list_buah = []
    for i in range(len(buah)):
        list_buah.append(buah[i])
        list_buah.append(buah[i])
    print(list_buah)

duplikasi(['pepaya' , 'mangga' , 'pisang' , 'durian' , 'jambu'])

#4
def konsonan(kata):
    value_kata = kata
    vokal = ['a' , 'e' , 'i' , 'o' , 'u' , '']
    for x in kata.lower():
        if x in vokal:
            value_kata = value_kata.replace(x,"")
    print(value_kata)

konsonan("Nurul Fikri")