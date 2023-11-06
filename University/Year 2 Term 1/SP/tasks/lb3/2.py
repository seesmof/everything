def check_similarity(A, B):
    if len(A) == 0 and len(B) == 0:
        return True
    if len(A) == 0 or len(B) == 0:
        return False
    for i in range(len(A[0])):
        if A[0][i] in B[0]:
            B[0].remove(A[0][i])
            return check_similarity([row[1:] for row in A], [row[1:] for row in B])
        else:
            return False


A = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
B = [[1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]]
print(check_similarity(A, B))
