def merge_sort(array):
    if len(array) <= 1:
        return array

    meio = len(array) // 2
    meioEsquerda = array[:meio]
    meioDireita = array[meio:]

    meioEsquerda = merge_sort(meioEsquerda)
    meioDireita = merge_sort(meioDireita)

    return merge(meioEsquerda, meioDireita)


def merge(esquerda, direita):
    ordenado = []
    indexEsquerda = 0
    indexDireita = 0

    while indexEsquerda < len(esquerda) and indexDireita < len(direita):
        if esquerda[indexEsquerda] <= direita[indexDireita]:
            ordenado.append(esquerda[indexEsquerda])
            indexEsquerda += 1
        else:
            ordenado.append(direita[indexDireita])
            indexDireita += 1

    while indexEsquerda < len(esquerda):
        ordenado.append(esquerda[indexEsquerda])
        indexEsquerda += 1

    while indexDireita < len(direita):
        ordenado.append(direita[indexDireita])
        indexDireita += 1

    return ordenado


def is_anagram(first_string, second_string):

    primeiraString = "".join(merge_sort(list(first_string.lower())))
    segundaString = "".join(merge_sort(list(second_string.lower())))

    if first_string == "" or second_string == "":
        return (primeiraString, segundaString, False)

    isAnagram = primeiraString == segundaString
    return (primeiraString, segundaString, isAnagram)
