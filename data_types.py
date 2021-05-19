'ამ ლინკზე არის კარგი სავარჯიშოები თავისი პასუხებით'
# https://www.w3schools.com/python/exercise.asp?filename=exercise_lists1
'''
>> სია list() დალაგებული, შეცვლადი, დუპლიკატები მოსულა
>> კორტეჟი Tuple() დალაგებული, *შეუცვლადი, დუპლიკატები მოსულა
>> ლექსიკონი dict() დალაგებული, შეცვლადი, #დუპლიკატები არ მოსულა
>> სიმრავლე Set() *არადალაგებული, *შეუცვლადი,*დუპლიკატები არ მოსულა
'''
#	list
x = ["apple", "apple", False, 5]
print("list",x)

print(type(x))
print('----------------------------------')
#	tuple
x = ("apple", "apple", False, 41)
print("tuple",x)

print(type(x))
print('----------------------------------')
#	dict
x = {"name" : "John", "age" : 36}
print("dict",x)

print(type(x))
print('----------------------------------')
#	set
x = {"apple", "banana", "cherry"}
print("set",x)

print(type(x))
