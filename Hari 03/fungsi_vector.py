def penjumlahan_vector(vector_1,vector_2):
    panjang_vector_1 = len(vector_1)
    panjang_vector_2 = len(vector_2)
    vector_3 = []

    if panjang_vector_1 == panjang_vector_2:
        print("jumlah vector")

        for i in range(panjang_vector_1):
            hasil = vector_1[i] + vector_2[i]
            vector_3.append(hasil)

    else:
        print("tidak bisa")
    
    return vector_3