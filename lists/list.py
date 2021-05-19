'''
>> სახელწოდება სია პირდაპირი მნიშვნელობითაა გამოყენებული
- ეს არის კონტეინერი, რომელშიც ყველა ობიექტი დანომრილია
>> სია განისაზღვრება კვადრატური ფრჩხილებით [...], და მისი ელემენტები ერთმანეთისგან მძიმითაა გამოყოფილი.
>> სიის მეთოდებია: append, clear, count, extend, index, insert, pop, remove, reverse, sort.
!სიის ელემენტად შეიძლება ისევ სია იყოს!  list = [[1, 2, 3], 4, 5, 6]
'''
# სიის დაწერის მაგალითი:
# ინდექსები  0  1  2  3  4
the_count = [1, 2, 3, 4, 5]

fruits = ['apple', 'grape', 'berry', 'banana']
change = [1, '10ge', 2, '20gel', 3, '50gel']

'''
სტარტი
სტარტი:დასასრული
სტარტი:დასასრული:ბიჯი
'''
print(the_count)
# სტარტი
print("3:",the_count[3:])
print("1:3",the_count[1:3])
print("0:4:2",the_count[0:4:2])
print('----------------------------------')
# for-ის ციკლს თვითონ შემოაქვს ცვლადი ციკლის დასაწყისში და ეს ცვლადი გამოიყენება მანამ, სანამ ციკლი მუშაობს
# for-ციკლის ეს მაგალითი სია the_count-ში ყველა ელემენტს ჩამოივლის
for number in the_count:
    print("number",number)
print('----------------------------------')
# იგივეა რაც ზემოთ
for fruit in fruits:
    print(f"fruit name: {fruit}")

# მუშაობს ასევე შერეულ სიებზეც
for i in change:
    print("all elements: ",i)
print('----------------------------------')

# ჩვენ სიის შექმნაც შეგვიძლია. თავიდან ცარიელით ვიწყებთ
elements = []
# შემდეგ ვიყენებთ range-ფუნქციას, რომ 0-დან 5-მდე დაგვითვალოს
for i in range (0, 6):
    # append - ქართ., დამატება. ეს ფუნქცია უბრალოდ ამატებს ელემენეტს სიის ბოლოში.
    elements.append(i)
    print(f" {i} added")

# ახლა კი ამ ელემენტების ამობეჭდვაც შეგვიძლია
for i in elements:
    print(f" element {i}")
print('----------------------------------')
# ორგანზომილებიანი სია
list = [[1, 2, 3], [4, 5, 6]]
print("list in list and element in it ", list[0][1])

print('----------------------------------')

# clear
list = [1,2,4,5]
print("clear",list.clear())

# count
list = [1,2,2,4,5]
print("count",list.count(2))

# extend
list = [1,2,2,4,5]
list.extend([6,7,8,9,'10'])
print("extend",list)

# index
print("index",list.index(2))

# insert
fruits = ['apple', 'banana', 'cherry']
fruits.insert(0, "orange")
print("insert ",fruits)

# pop
fruits.pop()
print("pop ",fruits)

# remove
fruits.remove('apple')
print("remove ",fruits)

# reverse
num = [3,4,57,1,2]
print("list", num)
num.reverse()
print("reverse ",num)

# sort
num = [3,4,57,1,2]
num.sort()
print("sort ",num)

'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

''''
