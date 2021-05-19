'''
>> კორტეჟი tuple არის შეუცვლელი მონაცემთა
სტრუქტურა, რომელიც ძალიან ჰგავს სიას
>> მისი უპირატესობა არის ის რომ, იგი დაცულია
ცვლილებებისგან. ამავდროულად, მცირე ზომისაა
>> კორტეჟი მუშაობს უფრო სწრაფად, ვიდრე სიები. ანუ
ელემენტების გადარჩევაზე და სხვა ოპერაციებზე
იხარჯება ნაკლები დრო
'''

# კორტეჟის შექმნა
tupl = (1, 2, 3,3,3, 4, 5)
print(tupl)
print('----------------------------------')

'''კორტეჟის ელემენტების შეცვლა არ შეიძლება, რაც
ჩანს მაგალითში:
tuple[1] = "one"
print(tuple)
'''
print('----------------------------------')

# რომელი უფრო მძიმეა?
lst = [10, 20, 30]
tpl = (10, 20, 30)
print('list',lst.__sizeof__())
print('tuple',tpl.__sizeof__())
print('----------------------------------')

# კორტეჟის ელემენტებზე წვდომა ხორციელდებ ინდექსის მითითებით, სიების მსგავსად
print(tupl[1])
print('----------------------------------')

'''
ცალკეული ელემენტის წაშლა კორტეჟიდან
შეუძლებელია. რაც იძლევა შეცდომას:
a = (1, 2, 3, 4, 5)
del a[0]
'''
print('----------------------------------')

# ელემენტების ამოღება
print(tupl)
print("3:",tupl[3:])
print("1:3",tupl[1:3])
print("1:4:2",tupl[1:4:2])
print('----------------------------------')

# კორტეჟის შეცვლა
x = ("apple", "banana", "cherry")
# სიაში გადაყვანა
y = list(x)
# შეცვლა
y[1] = "kiwi"
# გაკორტეჟება
x = tuple(y)
print(x)
print('----------------------------------')

# ამოლაგება და ჩალაგება ცვლადში კორტეჟიდან
fruits = ("apple", "banana", "cherry")
# ცვლადის სახელები უნდა დაემთხვას ველიუებს
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print('----------------------------------')

# იტერაცია
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
print('----------------------------------')

'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''
tupl = (1, 2, 3,3,3, 4, 5)
# count
print(tupl.count(3))
# index
print(tupl.index(3))
