# 25%
def solution(A):
	store = []
	store.insert(0, A[0])
	for i in range(1, len(A)):
		store.insert(i, store[i - 1])
		for minus in range(2,6):
			if i >= minus:
				store.insert(i, max(store[i], store[i - minus]))
			else:
				break
		store[i] += A[i]
	return store[len(A) - 1]