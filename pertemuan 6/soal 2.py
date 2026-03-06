menu = [["Nasi Goreng", 15000],
        ["Es teh", 5000],
        ["Mie Goreng", 10000],
        ["Teh Panas", 4000],
        ["Ayam Penyet", 13000]]

def tampilan_menu(list_menu):
    print("=== Menu ===")
    y=1
    for i,j in list_menu: 
        print(f"{y}.", i,":", j)
        y+=1
    print("\n")
    harga = 0
    porsi1 = 0
    porsi2 = 0
    porsi3 = 0
    porsi4 = 0
    porsi5 = 0
    list_beli=[]
    while True:
        pilih = int(input("pilih menu: "))
        if pilih == 1:
            print(f"{list_menu[0][0]} : {list_menu[0][1]}")
            harga +=list_menu[0][1]
            porsi1+=1
            if list_menu[0][0] not in list_beli:
                list_beli.append([list_menu[0][0]])
        elif pilih == 2:
            print(f"{list_menu[1][0]} : {list_menu[1][1]}")
            harga +=list_menu[1][1]
            porsi2+=1
            if list_menu[1][0] not in list_beli:
                list_beli.append([list_menu[1][0]])
        elif pilih == 3:
            print(f"{list_menu[2][0]} : {list_menu[2][1]}")
            harga +=list_menu[2][1]
            porsi3+=1
            if list_menu[2][0] not in list_beli:
                list_beli.append([list_menu[2][0]])
        elif pilih == 4:
            print(f"{list_menu[3][0]} : {list_menu[3][1]}")
            harga +=list_menu[3][1] 
            porsi4 += 1
            if list_menu[3][0] not in list_beli:
                list_beli.append([list_menu[3][0]])
        elif pilih == 5:
            print(f"{list_menu[4][0]} : {list_menu[0][1]}")
            harga +=list_menu[4][1]
            porsi5+=1
            if list_menu[4][0] not in list_beli:
                list_beli[0].append([list_menu[4][0]])
        elif pilih == 0:
            break    
        else:
            print("Error. Menu tak ditemukan")  
            harga += 0
    if porsi1>0:
        list_beli[0][1]=porsi1
    if porsi2>0:
        list_beli[1][1]=porsi2
    if porsi3>0:
        list_beli[2][1]=porsi3
    if porsi4>0:
        list_beli[3][1]=porsi4
    if porsi5>0:
        list_beli[4][1]=porsi5
    print("\n","=== pesanan anda ===")
    x=0
    for a in list_beli: 
        print(f"{x}.", a[0],":",a[1])
        x+=1
    print("total harga : Rp. ", harga)   
      

tampilan_menu(menu)

