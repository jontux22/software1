def hae_data():
    sqp= "SELECT"
    tulos=kursori.fetchall()


    print(tulos)
    print(tulos[0])
    print(tulos[0][0])


    for rivi in tulos:
        print(rivi)


        for alkio in rivi:
            print("  ", alkio)
