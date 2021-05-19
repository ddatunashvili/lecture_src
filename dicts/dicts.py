'''
>> სიების მსგავსად ლექსიკონი ინახავს ელემენტების კოლექციას.
>> ლექსიკონში ცალკეულ ელემენტს აქვს უნიკალური გასაღები,
რომელთან ასოცირებულია ზოგიერთი მნიშვნელობა.
>> ლექსიკონის განსაზღვრას აქვს შემდეგი სინტაქსი:
dictionary={გასაღები1:მნიშვნელობა1,გასაღები2:მნიშვნელობა2}
'''
'''
არ არის აუცილებელი, რომ გასაღები და სტრიქონი
იყოს ერთი ტიპის. ისინი შეიძლება წარმოადგენდნენ
სხვადასხვა ტიპებს
'''
objects = {1: "Tom", "2": True, 3: 100.6}
print(objects)
print(type(objects))
print('----------------------------------')

# სიის ლექსიკონად ქცევა
users_list = [
 [1, "Tom"],
 [2, "Bob"],
 [3, "Alice"]
]
users_dict = dict(users_list)
print('list to dict:',users_dict)
print('----------------------------------')


'''მსგავსად, შეიძლება ლექსიკონად გარდაიქმნას
ორგანზომილებიანი კორტეჟი ანუ კორტეჟი, რომელიც
თავის მხრივ შეიცავს ორ ელემენტიან კორტეჟებს:'''
users_tuple = (
 (1, "Tom"),
 (2, "Bob"),
 (3, "Alice")
)
users_dict = dict(users_tuple)
print('tuple to dict:',users_dict)
print('----------------------------------')

# დამატება
users_dict[4] = "Sam"
print('add:',users_dict)
print('----------------------------------')

'''
get() აბრუნებს ლექსიკონიდან ელემენტს key
გასაღებით. თუ ელემენტი ასეთი გასაღებით არ არის,
მაშინ აბრუნებს None მნიშვნელობას.
'''
# ელემენტის ამოღება
print('get:',users_dict.get(2))
print('----------------------------------')

# წაშლა
del users_dict[4]
print('del:',users_dict)
print('----------------------------------')

'''
pop(key) - წაშლის ელემენტს key გასაღების მიხედვით და
დააბრუნებს წაშლილ ელემენტს. თუ ელემენტი ასეთი
გასაღებით არ არის, გენერირდება შეცდომა;
'''
# წაშლა
users_dict.pop(3)
print('pop:',users_dict)
print('----------------------------------')

'''
თუ საჭიროა ყველა ელემენტის წაშლა, მაშინ
შეიძლება clear() მეთოდის გამოყენება:
'''

users_dict.clear()
print('clear:',users_dict)
print('----------------------------------')

# კოპირე
'''
copy() მეთოდი აკოპირებს ლექსიკონის
შემადგენლობას და აბრუნებს ახალ ლექსიკონს
'''

users={1:"Tom",2: "Bob",3:"Alice"}
users2 = users.copy()
print('copy():',users2)
print('----------------------------------')


'''
update() მეთოდი აერთიანებს ორ ლექსიკონს:
'''
users={1:"Tom",2: "Bob",3:"Alice"}
users2 = {4: "Sam",5: "Kate"}
users.update(users2)
print('update():',users)

'''
items() მეთოდი აბრუნებს კორტეჟების ნაკრებს,
ცალკეული კორტეჟი შეიცავს გასაღებს და ელემენტის
მნიშვნელობას, რომელიც გადარჩევისას იქვე შეიძლება
მივიღოთ key და value ცვლადებში.
'''
print(users.items())

# მეთოდები ლექსიკონებთან სამუშაოდ
'''
dict.clear() - ასუფთავებს ლექსიკონს;
dict.copy() - აბრუნებს ლექსიკონის ასლს;
classmethod dict.fromkeys(seq[, value]) - ქმნის ლექსიკონს
გასაღებით seq და მნიშვნელობით value (დუმილით None).
dict.get(key[, default]) - აბრუნებს გასაღების მნიშვნელობას,
მაგრამ იგი თუ არ არის, აბრუნებს default მნიშვნელობას
(დუმილით None);
dict.items() - აბრუნებს წყვილს - გასაღები, მნიშვნელობა;
dict.keys() - აბრუნებს გასაღებებს ლექსიკონიდან;
dict.pop(key[, default]) - წაშლის გასაღებს და აბრუნებს
მნიშვნელობას. თუ გასაღები არ არის აბრუნებს default
(დუმილით აგენერირებს გამონაკლისს KeyError);
dict.popitem() - წაშლის და აბრუნებს წყვილს: გასაღები,
მნიშვნელობა. თუ ლექსიკონი ცარიელია აგენერირებს
გამონაკლისს KeyError. ლექსიკონი არ არის დალაგებული;
dict.setdefault(key[, default]) - აბრუნებს გასაღების
მნიშვნელობას. თუ იგი არ არის, არ აგენერირებს
გამონაკლისს, არამედ ქმნის გასაღებს default
მნიშვნელობით. (დუმილით None);
dict.update([other]) - განაახლებს ლექსიკონს: გასაღები,
მნიშვნელობა წყვილის დამატებით other-დან. არსებული
გასაღებები გადაიწერება. აბრუნებს None (არა ახალი
ლექსიკონი!);
dict.values() - აბრუნებს მნიშვნელობას ლექსიკონიდან.
'''