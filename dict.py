names = open('names.txt', 'r',encoding="utf-8")
surNames = open('surNames.txt', 'r',encoding="utf-8")
imiona = []
nazwiska = []
def imie():

    for i in range(10):
        namText = names.readline()
        imiona.append(namText.replace("\n", ''))
    return imiona
def nazwisko():

    for i in range(10):
        text = surNames.readline()
        nazwiska.append(text.replace("\n", ''))
    return nazwiska
def typ():
    type=['Techniczny','porządkowy','kasjer']
    return type