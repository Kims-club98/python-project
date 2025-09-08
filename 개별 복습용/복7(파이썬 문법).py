list1=[1,2,3,4,5]
list2=[7,8,9,10,11]

# 1.
a= list1 + list2
print(a)
# 출력 [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

# 2.
b=list1 * 3
print(b)
# 출력 [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]  

# 3.
c=list1[0:4:2]
print(c)
# 출력 [1, 3]
d=list2[::2]
print(d)
#출력 [7, 9, 11]
# list[시작위치{0에서 시작}:끝 숫자:출력 단위]

# 4.
e=2 in list1
print(e)
# in list에 2가 있는지 T/F 추출(boold 함수)

#5.
f=list1.append(10)
print(list1)
#출력 [1, 2, 3, 4, 5, 10] 뒤에 항목 추가

#6.
list2.insert(2,'happy')
print(list2)
#출력 [7, 8, 'happy', 9, 10, 11] 해당 위치에 문자열 추가(0부터)

#7.
list3=[1,2,3]
list3.extend([1,2,'house'])
print(list3)
#출력[1, 2, 3, 1, 2, 'house'] 리스트의 함수 뒤에서 추가

#8.
list3.remove('house')
print(list3)
#출력 [1, 2, 3, 1, 2] 첫번쨰 일치 항목 제거

# 9.
list4=[1,2,3,4,5,6,7,8]
list4.pop()
print(list4)
#출력 [1, 2, 3, 4, 5, 6, 7] 가장 마지막 항목제거

#10.
list5=[4,2,6,3,8,99]
list5.sort()
print(list5)
#출력 [2, 3, 4, 6, 8, 99] 순행 정렬

#11. 
list5.reverse()
print(list5)