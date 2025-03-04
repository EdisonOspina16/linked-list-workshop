from datastruct.classes.lists import LinkedList, Node


def swap_nodes_in_pairs(linked_list: LinkedList[int]) -> LinkedList[int]:
    lista = Node(0)
    lista.next = linked_list.head
    anterior = lista

    while anterior.next and anterior.next.next:
        primero = anterior.next
        segundo = primero.next

        # Intercambio de nodos
        anterior.next, primero.next, segundo.next = segundo, segundo.next, primero

        # Avanzar al siguiente par
        anterior = primero

    linked_list.head = lista.next
    return linked_list
