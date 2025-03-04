from datastruct.classes.lists import LinkedList, Node


def add_two_numbers(l1: LinkedList[int], l2: LinkedList[int]) -> LinkedList[int]:
    lista = Node(0)
    actual = lista
    acarreo = 0

    n1, n2 = l1.head, l2.head

    while n1 or n2 or acarreo:
        valor_l1 = n1.data if n1 else 0
        valor_l2 = n2.data if n2 else 0

        total = valor_l1 + valor_l2 + acarreo
        acarreo = total // 10
        actual.next = Node(total % 10)
        actual = actual.next

        if n1: n1 = n1.next
        if n2: n2 = n2.next

    resultado = LinkedList[int]()
    resultado.head = lista.next
    return resultado
