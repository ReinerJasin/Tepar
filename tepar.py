import numpy as np

print("---------   .--------   .-------.   .-------.   .-------.")
print("    |       |           |       |   |       |   |       |")
print("    |       |--------   |-------'   |-------|   |-.-----'")
print("    |       |           |           |       |   |  '.    ")
print("    |       '--------   |           |       |   |     '. ")
print("")
print("Selamat Datang Di Tepar")
print("")

parking_gate_in = {'x':18867, 'y':17360}
Spot1 = {'name':'Park_A', 'x':17464, 'y':14687}
Spot2 = {'name':'Park_B', 'x':18131, 'y':14687}
Spot3 = {'name':'Park_C', 'x':18798, 'y':14687}
Spot4 = {'name':'Park_D', 'x':19465, 'y':14687}
Spot5 = {'name':'Park_E', 'x':20132, 'y':14687}
Spot6 = {'name':'Park_F', 'x':20799, 'y':14687}
Spot7 = {'name':'Park_G', 'x':16650, 'y':15501}
Spot8 = {'name':'Park_H', 'x':16650, 'y':16163}
Spot9 = {'name':'Park_I', 'x':16650, 'y':16825}
Spot10 = {'name':'Park_J', 'x':16650, 'y':17487}
Spot11 = {'name':'Park_K', 'x':16650, 'y':18149}
Spot12 = {'name':'Park_L', 'x':16650, 'y':18811}
Spot13 = {'name':'Park_M', 'x':18867, 'y':16027}
Spot14 = {'name':'Park_N', 'x':20195, 'y':16027}
Spot15 = {'name':'Park_O', 'x':18866, 'y':18063}
Spot16 = {'name':'Park_P', 'x':18866, 'y':18778}
Lobi1 = {'name': 'Lobi1', 'x':15762, 'y':14519}
Lobi2 = {'name': 'Lobi2', 'x':17752, 'y':19183}
Lobi3 = {'name': 'Lobi3', 'x':21162, 'y':15295}

# Inisialisasi table log
User1 = {'name':'Reiner', 'prudent':60, 'meek':35}
User2 = {'name':'Hans', 'prudent':0, 'meek':0}
User3 = {'name':'Leo', 'prudent':0, 'meek':0}
typeUser = "prudent"

Log_A = {'name':'Log_A', 'jumlah_dipilih':1, 'jumlah_tersedia':2, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_B = {'name':'Log_B', 'jumlah_dipilih':1, 'jumlah_tersedia':3, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_C = {'name':'Log_C', 'jumlah_dipilih':1, 'jumlah_tersedia':4, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_D = {'name':'Log_D', 'jumlah_dipilih':1, 'jumlah_tersedia':5, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_E = {'name':'Log_E', 'jumlah_dipilih':1, 'jumlah_tersedia':6, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_F = {'name':'Log_F', 'jumlah_dipilih':1, 'jumlah_tersedia':7, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_G = {'name':'Log_G', 'jumlah_dipilih':1, 'jumlah_tersedia':8, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_H = {'name':'Log_H', 'jumlah_dipilih':1, 'jumlah_tersedia':9, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_I = {'name':'Log_I', 'jumlah_dipilih':1, 'jumlah_tersedia':10, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_J = {'name':'Log_J', 'jumlah_dipilih':1, 'jumlah_tersedia':11, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_K = {'name':'Log_K', 'jumlah_dipilih':1, 'jumlah_tersedia':12, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_L = {'name':'Log_L', 'jumlah_dipilih':1, 'jumlah_tersedia':13, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_M = {'name':'Log_M', 'jumlah_dipilih':1, 'jumlah_tersedia':14, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_N = {'name':'Log_N', 'jumlah_dipilih':1, 'jumlah_tersedia':15, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_O = {'name':'Log_O', 'jumlah_dipilih':1, 'jumlah_tersedia':1, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}
Log_P = {'name':'Log_P', 'jumlah_dipilih':1, 'jumlah_tersedia':17, 'status': 'free', 'jarak_ke_Lobi_1':0, 'jarak_ke_Lobi_2':0, 'jarak_ke_Lobi_3':0, 'jarak_mobil_parkir': 0}

Log_Parkiran = [Log_A, Log_B, Log_C, Log_D, Log_E, Log_F, Log_G, Log_H, Log_I, Log_J, Log_K, Log_L, Log_M, Log_N, Log_O, Log_P]
parkiran = [Spot1,Spot2,Spot3,Spot4,Spot5,Spot6,Spot7,Spot8,Spot9,Spot10,Spot11,Spot12,Spot13,Spot14,Spot15,Spot16]
lobi = [Lobi1, Lobi2, Lobi3]

# for i in Log_Parkiran:
for i in range(len(Log_Parkiran)):
  for j in range(len(lobi)):
    jarak_X = lobi[j]['x'] - parkiran[i]['x']
    jarak_Y = lobi[j]['y'] - parkiran[i]['y']

    jarak_kaki = np.sqrt(pow(jarak_X, 2) + pow(jarak_Y, 2))

    if (lobi[j]['name'] == Lobi1['name']):
      Log_Parkiran[i]['jarak_ke_Lobi_1'] = jarak_kaki

    elif (lobi[j]['name'] == Lobi2['name']):
      Log_Parkiran[i]['jarak_ke_Lobi_2'] = jarak_kaki

    elif (lobi[j]['name'] == Lobi3['name']):
      Log_Parkiran[i]['jarak_ke_Lobi_3'] = jarak_kaki

for k in range(len(Log_Parkiran)):
  jarak_X = parking_gate_in['x'] - parkiran[k]['x']
  jarak_Y = parking_gate_in['y'] - parkiran[k]['y']

  jarak_mobil = np.sqrt(pow(jarak_X, 2) + pow(jarak_Y, 2))

  Log_Parkiran[k]['jarak_mobil_parkir'] = jarak_mobil
  # index_k += 1

def printMenu(key, jarak1, jarak2, jarak3, jarak4, percentage):
        print("Parkiran " + key)
        print("Jarak ke lobi 1 : {:.2f}".format(jarak1))
        print("Jarak ke lobi 2 : {:.2f}".format(jarak2))
        print("Jarak ke lobi 3 : {:.2f}".format(jarak3))
        print("Jarak berkendara : {:.2f}".format(jarak4))
        print("Persentase favorit : {:.2f}".format(percentage) + "%")
        print("")

def printMenu1(key, jarak1, jarak4, percentage):
        print("Parkiran " + key)
        print("Jarak ke lobi 1 : {:.2f}".format(jarak1))
        print("Jarak berkendara : {:.2f}".format(jarak4))
        print("Persentase favorit : {:.2f}".format(percentage) + "%")
        print("")

def printMenu2(key, jarak2, jarak4, percentage):
        print("Parkiran " + key)
        print("Jarak ke lobi 2 : {:.2f}".format(jarak2))
        print("Jarak berkendara : {:.2f}".format(jarak4))
        print("Persentase favorit : {:.2f}".format(percentage) + "%")
        print("")

def printMenu3(key, jarak3, jarak4, percentage):
        print("Parkiran " + key)
        print("Jarak ke lobi 3 : {:.2f}".format(jarak3))
        print("Jarak berkendara : {:.2f}".format(jarak4))
        print("Persentase favorit : {:.2f}".format(percentage) + "%")
        print("")

# print(Log_A)
# print(Log_B)
# print(Log_C)
# print(Log_D)
# print(Log_E)
# print(Log_F)
# print(Log_G)
# print(Log_H)
# print(Log_I)
# print(Log_J)
# print(Log_K)
# print(Log_L)
# print(Log_M)
# print(Log_N)
# print(Log_O)
# print(Log_P)

def takeSpot():

    percent_prudent = User1["prudent"]/(User1["prudent"] + User1["meek"])
    percent_meek = 1 - percent_prudent

    print("Detail User ")
    print("   Total prudent    : " + str(User1["prudent"]))
    print("   Total meek       : " + str(User1["meek"]))

    jarak_kaki_min_prudent = 99999999999
    nama_spot_prudent = ""
    jarak_kaki_min_meek = 99999999999
    nama_spot_meek = ""

    # algoritman rekomendasi spot prudent
    for i in range(len(Log_Parkiran)):
      if(Log_Parkiran[i]['status'] == "free"):
        if(Log_Parkiran[i]['jarak_ke_Lobi_1'] < jarak_kaki_min_prudent):
          jarak_kaki_min_prudent = Log_Parkiran[i]['jarak_ke_Lobi_1']
          nama_spot_prudent = Log_Parkiran[i]['name']

        if(Log_Parkiran[i]['jarak_ke_Lobi_2'] < jarak_kaki_min_prudent):
          jarak_kaki_min_prudent = Log_Parkiran[i]['jarak_ke_Lobi_2']
          nama_spot_prudent = Log_Parkiran[i]['name']

        if(Log_Parkiran[i]['jarak_ke_Lobi_3'] < jarak_kaki_min_prudent):
          jarak_kaki_min_prudent = Log_Parkiran[i]['jarak_ke_Lobi_3']
          nama_spot_prudent = Log_Parkiran[i]['name']

        # print("index ke " + str(i))
        # print(jarak_kaki_min)
        # print(nama_spot)

    # algoritman rekomendasi spot meek
    for i in range(len(Log_Parkiran)):

      if(Log_Parkiran[i]['status'] == "free"):
        if(Log_Parkiran[i]['jarak_ke_Lobi_1'] + Log_Parkiran[i]['jarak_mobil_parkir'] < jarak_kaki_min_meek):
          jarak_kaki_min_meek = Log_Parkiran[i]['jarak_ke_Lobi_1'] + Log_Parkiran[i]['jarak_mobil_parkir']
          nama_spot_meek = Log_Parkiran[i]['name']

        if(Log_Parkiran[i]['jarak_ke_Lobi_2'] + Log_Parkiran[i]['jarak_mobil_parkir'] < jarak_kaki_min_meek):
          jarak_kaki_min_meek = Log_Parkiran[i]['jarak_ke_Lobi_2'] + Log_Parkiran[i]['jarak_mobil_parkir']
          nama_spot_meek = Log_Parkiran[i]['name']

        if(Log_Parkiran[i]['jarak_ke_Lobi_3'] + Log_Parkiran[i]['jarak_mobil_parkir'] < jarak_kaki_min_meek):
          jarak_kaki_min_meek = Log_Parkiran[i]['jarak_ke_Lobi_3'] + Log_Parkiran[i]['jarak_mobil_parkir']
          nama_spot_meek = Log_Parkiran[i]['name']


    if(percent_prudent >= percent_meek):
      typeUser = "prudent"
      print("Rekomendasi Prudent ")
      print("   Jarak Jalan Kaki : {:.2f}".format(jarak_kaki_min_prudent))
      print("   Nama Lokasi      : " + nama_spot_prudent)

      # print("SPOT YANG MEEK")
      # print(jarak_kaki_min_meek)
      # print(nama_spot_meek)
    else:
      typeUser = "meek"
      print("Rekomendasi Meek ")
      print("   Jarak Total : {:.2f}".format(jarak_kaki_min_meek))
      print("   Nama Lokasi : " + nama_spot_meek)

      # print("SPOT YANG PRUDENT")
      # print(jarak_kaki_min_prudent)
      # print(nama_spot_prudent)


    choice2 = input("Apakah kamu ingin mengambil rekomendasi parkiran ini : (y/n)")
    print("")
    if (choice2 == "y"):
      #tambah ke logy
      for j in Log_Parkiran:
          if(j['name'] == nama_spot_prudent):
              if(j['status'] == "free"):
                  j['jumlah_tersedia'] += 1

                  j['status'] = "occupied"
                  j['jumlah_dipilih'] += 1
      if (typeUser == "prudent"):
        User1['prudent'] = User1['prudent'] + 1
      else:
        User1['meek'] = User1['meek'] + 1

      # print(User1['prudent'])
      # print(User1['meek'])
    else:
      #nyuruh pilih parkiran dengan menampilkan semua parkiran
      # print("user pilih n")
      urutan = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0}
      key = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
      for i in range(len(Log_Parkiran)):
        dipilih = Log_Parkiran[i]['jumlah_dipilih']
        tersedia = Log_Parkiran[i]['jumlah_tersedia']

        try:
          percentage = dipilih / tersedia
        except:
          percentage = 0
        urutan[key[i]] = percentage
        # print(urutan[key[i]])

      urutan_sorted = dict(sorted(urutan.items(), key=lambda x: x[1], reverse = True))
      # print(urutan_sorted)
      print("Daftar Parkiran Ter-Favorit:")
      iteration = 0
      for i in urutan_sorted.keys():
        # print("DEBUG")
        # print(i)
        # listKey = list(urutan_sorted.keys())
        # print(urutan_sorted.keys()[i])
        for j in Log_Parkiran:
          # print(Log_Parkiran[j]['status'])
          # print(Log_Parkiran[j]['name'])
          # print(Log_Parkiran[j]['name'])
          if(j['status'] == "free" and j['name'] == "Log_" + i):

            # print("No. " + str(iteration + 1))

            # if(int.j['jarak_ke_Lobi_1'] < int.j['jarak_ke_Lobi_2'] & int.j['jarak_ke_Lobi_1'] < int.j['jarak_ke_Lobi_3']):
            #     printMenu1(i, j['jarak_ke_Lobi_1'], j['jarak_mobil_parkir'], (urutan[i] * 100))
            # elif(int.j['jarak_ke_Lobi_2'] < int.j['jarak_ke_Lobi_1'] & int.j['jarak_ke_Lobi_2'] < int.j['jarak_ke_Lobi_3']):
            #     printMenu2(i, j['jarak_ke_Lobi_2'], j['jarak_mobil_parkir'], (urutan[i] * 100))
            # elif(int.j['jarak_ke_Lobi_3'] < int.j['jarak_ke_Lobi_2'] & int.j['jarak_ke_Lobi_3'] < int.j['jarak_ke_Lobi_2']):
            #     printMenu3(i, j['jarak_ke_Lobi_3'], j['jarak_mobil_parkir'], (urutan[i] * 100))

            printMenu(i, j['jarak_ke_Lobi_1'],j['jarak_ke_Lobi_2'], j['jarak_ke_Lobi_3'], j['jarak_mobil_parkir'], (urutan[i] * 100))
            iteration += 1



        choice3_check = False

      while choice3_check == False:
        choice3 = input("Ketik nama parkiran yang ingin kamu ambil (contoh -> Log_B) : ")

        for i in Log_Parkiran:
          #dicek kalau namanya sama
          if(i['name'] == choice3):
              if( i['status'] == "free"):
                  print("Anda berhasil mengambil parkiran")
                  choice3_check = True

                  if choice3 == nama_spot_prudent:
                      User1['prudent'] = User1['prudent'] + 1
                  elif choice3 == nama_spot_meek:
                      User1['meek'] = User1['meek'] + 1

                  for j in Log_Parkiran:
                      if(j['status'] == "free"):
                          j['jumlah_tersedia'] += 1

                  i['status'] = "occupied"
                  i['jumlah_dipilih'] += 1
              else:
                print("Parkiran penuh")
      # Output table LOG
      #   for i in Log_Parkiran:
      #       print(i)

      print("")

abc = False
while abc == False:
    parkirq = input("Apakah anda sedang mencari parkiran? (y/n)")
    if (parkirq == "y"):
        print("")
        takeSpot()
    if (parkirq == "n"):
        abc = True
