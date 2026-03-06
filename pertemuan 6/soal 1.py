#1. Menampilkan menu warung
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
    pilih = int(input("pilih menu: "))
    if pilih == 1:
        print(f"{list_menu[0][0]} : {list_menu[0][1]}")
    elif pilih == 2:
        print(f"{list_menu[1][0]} : {list_menu[1][1]}")
    elif pilih == 3:
        print(f"{list_menu[2][0]} : {list_menu[2][1]}")
    elif pilih == 4:
        print(f"{list_menu[3][0]} : {list_menu[3][1]}") 
    elif pilih == 5:
        print(f"{list_menu[0][0]} : {list_menu[0][1]}")
    else:
        print("Error. Menu tak ditemukan")           

tampilan_menu(menu)

