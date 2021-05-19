'''


'''
# დუპლიკატებს  გააქრობს
users = {"Tom","Bob","Alice", "Tom"}
print(users) # {"Tom","Bob","Alice"}
print('----------------------------------')

# ელემენტის დამატება
users = set()
users.add("Sam")
print('add:',users)
print('----------------------------------')

'''
წაშლის remove() მეთოდი, რომელშიც გადაეცემა წასაშლელი ელემენტი.
მაგრამ უნდა იქნას გათვალისწინებული, რომ თუ ასეთი
ელემენტი არ არის სიმრავლეში, გენერირდება შეცდომა.
'''
users = {"Tom", "Bob", "Alice"}
user = "Tom"
if user in users:
    users.remove(user)
print('remove:',users)
print('----------------------------------')

'''
ასევე, წასაშლელად შეიძლება გამოყენებულ იქნას
discard() მეთოდი, რომელიც არ აგენერირებს შეცდომას
ელემენტის არ არსებობის დროს
'''
# ელემენტის წაშლა
user = "Tim"
users.discard(user)
print("discard:",users)
print('----------------------------------')

'''
union() მეთოდი აერთიანებს ორ სიმრავლეს და
აბრუნებს ახალ სიმრავლეს:
'''
users = {"Tom","Bob","Alice"}
users2 = {"Sam","Kate", "Bob"}
users3 = users.union(users2)
print('union:',users3)
print('----------------------------------')


'''
intersection()
მეთოდი ახდენს სიმრავლეთა თანაკვეთის ოპერაციას და
აბრუნებს ახალ სიმრავლეს:
'''
users = {"Tom","Bob","Alice"}
users2 = {"Sam","Kate", "Bob"}
users3 = users.intersection(users2)
print("intersection",users3)
print('----------------------------------')




'''
issubset მეთოდი დაადგენს არის თუ არა მიმდინარე
სიმრავლე სხვა სიმრავლის ქვესიმრავლე:
'''
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
print(users.issubset(superusers)) # True
print('issubset:',superusers.issubset(users)) # False
print('----------------------------------')


'''
issuperset მეთოდი, პირიქით, აბრუნებს True, თუ
მიმდინარე სიმრავლე შეიცავს ქვესიმრავლეს:
'''
users = {"Tom", "Bob", "Alice"}
superusers = {"Sam", "Tom", "Bob", "Alice", "Greg"}
print(users.issuperset(superusers)) # False
print('issuperset',superusers.issuperset(users)) # True
print('----------------------------------')




# ყველა ფუნქცია
'''
en(s)- სიმრავლეში ელემენტების რაოდენობა;
x in s - მიკუთვნება სიმრავლეზე;
set.isdisjoint(other) - ჭეშმარიტია, თუ set და other არა აქვთ
საერთო ელემენტი;
set == other – set ყველა ელემენტი ეკუთვნის other და
პირიქით;
set.issubset(other) ანუ set <= other - set ყველა ელემენტი
ეკუთვნის other;
set.issuperset(other) ან set >= other – other ყველა ელემენტი
ეკუთვნის set;
set.union(other, ...) ან set | other | - ყველა სიმრავლის
გაერთიანება;
set.intersection(other, ...) ან set & other & ...-სიმრავლეთა
თანაკვეთა;
set.difference(other, ...) ან set - other - აბრუნებს სიმრავლეს
ელემენტებისგან, რომლებიც არის set-ში და არ არის otherში;
set.symmetric_difference(other); set ^ other - აბრუნებს
სიმრავლეს ელემენტებისგან, რომლებიც გვხვდება ერთ
სიმრავლეში და არ გვხვდება ორივე სიმრავლეში.
set.copy() - სიმრავლის ასლი.
set.update(other, ...); set |= other | - სიმრავლეთა
გაერთიანება;
119
set.intersection_update(other, ...); set &= other & ...-
სიმრავლეთა თანაკვეთა;
set.difference_update(other, ...); set -= other | ..- სიმრავლეთა
გამოკლება;
set.symmetric_difference_update(other); set ^= other -
მიიღება სიმრავლე ელემენტებისგან, რომელიც გვხვდება
ერთ-ერთ სიმრავლეში, მაგრამ არ გვხვდება ორივეში;
set.add(elem) - დაამატებს ელემენტს სიმრავლეში;
set.remove(elem) - წაშლის ელემენტს სიმრავლედან;
set.discard(elem) - წაშლის ელემენტს. თუ იგი მდებარეობს
სიმრავლეში;
set.pop() - წაშლის სიმრავლედან პირველ ელემენტს,
რამდენადაც სიმრავლე არ არის მოწესრიგებული, არ
შეიძლება ითქვას თუ რომელი ელემენტი იქნება პირველი;
set.clear() - სიმრავლის გასუფთავება
'''
