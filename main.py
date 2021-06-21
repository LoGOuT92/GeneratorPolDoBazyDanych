import tables

while 1==1:
    print("1 - dodaj x wierszy do tabeli widz")
    print("2 - dodaj x wierszy do tabeli artysta")
    print("3 - dodaj x wierszy do tabeli autobusy")
    print("4 - dodaj x wierszy do tabeli pracownik")
    print("0 - zakoncz program")
    x=input("co Chcesz zrobić?")
    if x=="1":
        number=int(input("ile rekordow chcesz dodac to tabeli widz?"))
        tables.widz(number)
    if x=="2":
        number=int(input("ile rekordow chcesz dodac to tabeli artysta?"))
        tables.artysta(number)
    if x=="3":
        number=int(input("ile rekordow chcesz dodac to tabeli autobusy?"))
        tables.autobusy(number)
    if x=="4":
        number=int(input("ile rekordow chcesz dodac to tabeli pracownik?"))
        tables.pracownik(number)
    if x=="0":
        break





