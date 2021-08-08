def order(array):
    array.sort()
    return array

def count_mayores(diccionario):
    count = 0
    for i in diccionario:
        if i.get("edad") < 18:
            pass
        else:
            count = count+1
    print("Hay un total de: ",count," personas mayores de edad.")
    return count