from datastruct.classes.lists import LinkedList


def add_two_numbers(l1: LinkedList[int], l2: LinkedList[int]) -> LinkedList[int]:

    lista = LinkedList(0)
    actual = lista
    count = 0

    while l1 or l2 or count:
        verl1 = l1.data
        verl2 = l2.data

        total = verl1 + verl2
        actual.next = LinkedList(total % 10)
        actual = actual.next
