def findFourElements(arr, n, X):

	mp = {}
	for i in range(n - 1):
		for j in range(i + 1, n):
			mp[arr[i] + arr[j]] = [i, j]

	for i in range(n - 1):
		for j in range(i + 1, n):
			summ = arr[i] + arr[j]

			if (X - summ) in mp:

				p = mp[X - summ]
				if (p[0] != i and p[0] != j and p[1] != i and p[1] != j):
					print(arr[i], ", ", arr[j], ", ",
						arr[p[0]], ", ", arr[p[1]], sep="")
					return


arr = [10, 20, 30, 40, 1, 2]
n = len(arr)
X = 91

findFourElements(arr, n, X)
