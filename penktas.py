if __name__ == '__main__':
    list_mano = ["a","b","c","d", "ab"]
    list_tavo = ["vilnius","kaunas", "nida"]
    naujas_kintamasis = list_mano + list_tavo
    print(naujas_kintamasis)
    naujas_kintamasis.append(23)
    print(naujas_kintamasis)
    naujas_kintamasis +=["Siauliai"]
    print(naujas_kintamasis)
    naujas_kintamasis.insert(0, "lietuvis")
    print(naujas_kintamasis)
    del naujas_kintamasis[5]
    print(naujas_kintamasis)
