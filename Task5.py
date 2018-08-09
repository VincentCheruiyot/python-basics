#index as per video no. 13

#strings have multiple characters "apple"
#lists have multiple members [1,2,3,4,5]

alpha='abcde'
print(alpha.index('d'))

alpha_list=list(alpha)
print(alpha_list.index('b'))

print(alpha[0])

print(alpha_list[2])

print(alpha)

#python has around 30 keywords such as del,trash,etc

alpha_list=list('abcde')
del alpha_list[2]
print(alpha_list)