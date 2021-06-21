import connection
import dict
import random

connection = connection.pol()
cursor = connection.cursor()

def widz(x):
    insert = open('insert.txt', 'a', encoding="utf-8")
    name = dict.imie()
    surName = dict.nazwisko()

    cursor.execute('SELECT MAX(ID_WIDZA) FROM WIDZ')
    index = cursor.fetchone()
    index2=int(index[0])
    for i in range(x):
        index2+=1
        name2 = random.choice(name)
        surname2 = random.choice(surName)
        mail=str(surname2)+'@gmail.com'
        phone = random.randint(100000000,999999999)
        id=random.randint(1,5)
        rows = [(index2, name2, surname2,phone,mail,id)]
        cursor.executemany("insert into WIDZ values(:1,:2,:3,:4,:5,:6)", rows)
        connection.commit()

        a="'"
        b="insert into WIDZ values "
        insertTXT= b+'('+str(index2)+','+a+str(name2)+a+','+a+str(surname2)+a+','+str(phone)+','+a+str(mail)+a+','+str(id)+')'+ ';'
        print(insertTXT)
        insert.write(insertTXT)
        insert.write('\n')
    print("Sukces!")
def artysta(x):

    name = dict.imie()
    surName = dict.nazwisko()
    insert = open('insert.txt', 'a', encoding="utf-8")
    cursor.execute('SELECT MAX(id_artysta ) FROM ARTYSTA')
    index = cursor.fetchone()
    index2 = int(index[0])
    for i in range(x):
        index2 += 1
        name2 = random.choice(name)
        surname2 = random.choice(surName)
        pse = str(surname2)+str(random.randint(0,99))
        phone = random.randint(100000000, 999999999)
        rows = [(index2, name2, surname2, pse, phone)]
        cursor.executemany("insert into ARTYSTA values(:1,:2,:3,:4,:5)", rows)
        connection.commit()

        a = "'"
        b = "insert into ARTYSTA values "
        insertTXT = b + '(' + str(index2) + ',' + a + str(name2) + a + ',' + a + str(surname2) + a + ',' + str(pse) + ',' + a + str(phone) + a + ')' + ';'
        insert.write(insertTXT)
        insert.write('\n')
    print("Sukces!")
def autobusy(x):
    insert = open('insert.txt', 'a', encoding="utf-8")
    cursor.execute('SELECT MAX(ID_AUTOBUSU ) FROM AUTOBUSY')
    index = cursor.fetchone()
    index2 = int(index[0])
    try:
        for i in range(x):
            index2 += 1
            max=random.randint(30,200)
            rows = [(index2, index2, max, index2)]
            cursor.executemany("insert into AUTOBUSY values(:1,:2,:3,:4)", rows)
            connection.commit()
            a = "'"
            b = "insert into AUTOBUSY values "
            insertTXT = b + '(' + str(index2) + ',' + str(index2) + ',' + str(max) +','+ str(index2) + ')' + ';'
            insert.write(insertTXT)
            insert.write('\n')
        print("Sukces!")
    except:
        print("Blad! prawdopodobnie chcesz przypisac autobus do nieistniejacego pracownika! sprobuj dodac pracownikow")
def pracownik(x):
    insert = open('insert.txt', 'a', encoding="utf-8")
    name = dict.imie()
    surName = dict.nazwisko()
    type = dict.typ()
    cursor.execute('SELECT MAX(ID_PRACOWNIK) FROM PRACOWNIK')
    index = cursor.fetchone()
    index2 = int(index[0])
    for i in range(x):
        index2 += 1
        name2 = random.choice(name)
        surname2 = random.choice(surName)
        date = str(random.randint(1950,2003))
        typ=random.choice(type)
        phone = random.randint(100000000, 999999999)
        id1=random.randint(1,5)
        id2=random.randint(1,5)
        id3=random.randint(1,5)
        rows = [(index2, name2, surname2, date,typ,phone,id1,id2,id3)]
        cursor.executemany("insert into PRACOWNIK values(:1,:2,:3,:4,:5,:6,:7,:8,:9)", rows)
        connection.commit()
        a = "'"
        b = "insert into PRACOWNIK values "
        insertTXT = b + '(' + str(index2) + ',' +a+ str(name2) +a+ ',' +a+ str(surname2) +a+ ',' + str(date)+ ',' +a+ str(typ)+a+',' + str(phone)+ ',' +str(id1)+ ',' +str(id2)+ ',' +str(id3) + ')' + ';'
        insert.write(insertTXT)
        insert.write('\n')
    print("Sukces!")









