documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]


directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006', '5400 028765', '5455 002299'],
        '3': []
      }


def people():
    name_people = input("Введите номер документа")
    a = 0
    for i in documents:
        if i["number"] == name_people:
            res = i["name"]
            a +=1
    if a == 0:
        print("Такого элемента нет")
    return res

def list_function():
    for i in documents:
        print(f" {i['type']} \"{i['number']}\" \"{i['name']}\" ")
def shelf_n():
    number_ones = input("Введите номер документа")
    a = 0
    for i, j in directories.items():
        for m in j:
            if number_ones == m:
                print(i)
                a += 1




    if a == 0:
        print("Такой документ не лежит ни на одной из полок")
def add():
    x1 = input("Введите тип объекта")
    x2 = input("Введите номер объекта")
    x3 = input("Введите имя объекта")
    x4 = input("Полка на каторой лежит")
    documents.append({"type": x1, "number": x2, "name": x3})
    print(documents)
    directories[x4].append(x2)
    print(directories)
def delete():
    number_document = input("Введите номер документа, который нужно удалить")
    i = 0
    while i < len(documents):
        if documents[i]["number"] == number_document:
            del documents[i]
        i += 1
    print(documents)

    new_directories = {}
    for k, m in directories.items():
        b = []
        for n in m:
            if n == number_document:
                del n
            else:
                b.append(n)
        #print(b)
        new_directories[k] = b
    print(new_directories)
def add_shelf():
    number = input("Номер новой полки")
    n = []
    directories.setdefault(int(number),n)
    print(directories)

if __name__ == '__main__':
    comand = input("Введите команду действия")
    comand = 'p'
    if comand == 'p':
        print(people())
    elif comand == 'l':
        list_function()
    elif comand == 's':
        shelf_n()
    elif comand == 'a':
        add()
    elif comand == 'd':
        delete()
    elif comand == 'as':
        add_shelf()