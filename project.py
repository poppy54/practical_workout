# ------------------- General Programs -------------------


# 1. User's name and age
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name}, you are {age} years old.")


# 2. Sum of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)


# 3. Count words in a file
with open("sample.txt", "r") as f:
 words = f.read().split()
print("Word count:", len(words))



sentence = input("Enter a sentence: ")
with open("reversed.txt", "w") as f:
 f.write(sentence[::-1])


# 5. CSV to dictionary
import csv
csv_dict = {}
with open("sample.csv", newline="") as f:
 reader = csv.DictReader(f)
for row in reader:
 csv_dict[row[reader.fieldnames[0]]] = row
print(csv_dict)


# 6. Monitor log file for keyword
import time
keyword = "ERROR"
with open("log.txt", "r") as f:
    f.seek(0, 2)
while True:
    line = f.readline()
if keyword in line:
    print("ALERT! Keyword found:", line.strip())
time.sleep(1)




# ------------------- Strings -------------------


# 1. Reverse string
s = "hello"
print(s[::-1])


# 2. Count vowels
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for ch in s if ch in vowels)
print("Vowel count:", count)


# 3. Check anagrams
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
print(is_anagram("listen", "silent"))


# 4. Word occurrences
sentence = "this is a test this is"
words = sentence.split()
print(d1)


# VI. Swap keys and values
d = {'a':1, 'b':2, 'c':3}
print({v:k for k,v in d.items()})


# VII. Fibonacci with memoization
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
  if n <= 1:
   return n
  return fib(n-1) + fib(n-2)
print(fib(10))


# VIII. Pythagorean triplets
n = 20
triplets = [(a,b,c) for a in range(1,n) for b in range(a,n) for c in range(b,n) if a*a + b*b == c*c]
print(triplets)


# IX. Shopping cart
def shopping_cart():
 cart = {}
def add(item, price, qty):
    cart[item] = {"price":price, "qty":qty}
def remove(item):
    cart.pop(item, None)
def total():
    return sum(v["price"]*v["qty"] for v in cart.values())
    return {"add":add, "remove":remove, "total":total, "cart":cart}


shop = shopping_cart()
shop["add"]("apple", 2, 3)
shop["add"]("banana", 1, 5)
print("Cart:", shop["cart"])
print("Total:", shop["total"]())


# X. Dictionary-based LRU Cache
from collections import OrderedDict


class LRUCache:
    def init(self, max_size=3):
     self.cache = OrderedDict()
     self.max_size = max_size


def get(self, key):
 if key in self.cache:
  self.cache.move_to_end(key)
 return self.cache[key]
 return -1


def put(self, key, value):
 self.cache[key] = value
 self.cache.move_to_end(key)
if len(self.cache) > self.max_size:
    self.cache.popitem(last=False)


lru = LRUCache(2)
lru.put(1, "A")
lru.put(2, "B")
print(lru.cache)
lru.get(1)
lru.put(3, "C")

print(lru.cache)
