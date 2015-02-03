#!/usr/bin/python3


'''
how many combinations to get sum 100 using number 1 to 100 and using each number only
once
'''



def combinations2(sumK, denom, length):
	if sumK == 0:
		return 1
	if length < 1:
		return 0
	if sumK < 0:
		return 0

	k = combinations2(sumK, denom, length-1) + combinations2(sumK-denom[length-1], denom, length-1)
	print(sumK, denom[:length-1],sumK-denom[length-1], denom[:length-1], end="")	
	print(k)
	return k

def combinations(sumK, denom, length):
	if sumK == 0:
		return 1
	if length < 1:
		return 0
	if sumK < 0:
		return 0

	if dpTable[sumK][length]:
		return dpTable[sumK][length]
	#print(sumK, denom[:length])
	withoutUsing = combinations(sumK, denom, length-1)
	withUsing = combinations(sumK-denom[length-1], denom, length-1)

	dpTable[sumK][length] = withUsing + withoutUsing

	return withUsing + withoutUsing

	


if __name__ == '__main__':
	for sumK in range(100):
		denom = [i for i in range(1,sumK+1)]
		dpTable = []
		for i in range(sumK+1):
			dpTable.append([None] * (sumK+1))

		combinations(sumK, denom, len(denom))
		print(sumK, dpTable[sumK][len(denom)])
		
		#for i in range(sumK+1):
		#	print(dpTable[i])


		#print(combinations2(sumK, denom, len(denom)))



			
