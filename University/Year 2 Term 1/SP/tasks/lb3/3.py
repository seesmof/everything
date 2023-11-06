def find_k(family_of_sets, k=1):
    for set_of_letters in family_of_sets:
        if len(set_of_letters) == k:
            return k
    return find_k(family_of_sets, k + 1)
