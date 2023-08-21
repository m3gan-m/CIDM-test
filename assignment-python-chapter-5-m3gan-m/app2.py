# Edit this file according to the instructions
# Import various modules needed for this lesson
from random import random
from array import array
from collections import deque
# start coding below this line
# Megan Moore
#chapter 5.8 Lambda Functions
print("\nChapter 5.8 Lambda Functions"+"-"*20)
items=[("Product1",10),("Product2",9),("Product3",12)]
#sort by quantity
items.sort(key=lambda item: item[1])
print(items)
#sort by sales
star_wars_box_office = [
    ["Star Wars", 1300],
    ["The Empire Strikes Back", 704.2],
    ["Return of Jedi", 723.2],
    ["The Phantom Menace", 757.5]]
star_wars_box_office.sort(key=lambda item:item[1])
print(star_wars_box_office)
#sort by movie name
star_wars_box_office.sort(key=lambda item:item[0])
print(star_wars_box_office)

#Chapter 5.9 Map Function
print("\nChapter 5.9 Map Function"+"-"*20)
items=[("Product1",10),("Product2",9),("Product3",12)]
#transform the list into a new list, using for loop
prices=[]
for item in items:
    prices.append(item[1])

#transform list into new list using lambda
items=[("Product1",10),("Product2",9),("Product3",12)]
prices=list(map(lambda item:item[1],items))
print(prices)

#chapter 5.10 FIlter Function
print("\nChapter 5.10 Filter Function"+"-"*20)
items=[("Product1",10),("Product2",9),("Product3",12)]
filtered = list(filter(lambda item:item[1] >= 10,items))
print(filtered)

#anotehr example
sw = [
    ["Star Wars", 1300],
    ["The Empire Strikes Back", 704.2],
    ["Return of Jedi", 723.2],
    ["The Phantom Menace", 757.5]]
sw_filtered = list(filter(lambda item:item[1] >=750.0, sw))
print(sw_filtered)

#Chapter 5.11 List COmprehensions
print("\nChapter 5.11 List Comprehensions"+"-"*20)
#mapping means to create a new list from another, or transform the list
#THis is also called "List Comprehension"
items=[("Product1",10),("Product2",9),("Product3",12)]
#mapping using lambda
prices = list(map(lambda item:item[1], items))
#mapping using pythong's list comprehension
prices = [item[1] for item in items]
print(prices)

#real example of list comprehension
#create 10 random numbers
random_numbers = [random() for item in range(10)]
print(random_numbers)

#filter using lambda
filtered = list(filter(lambda item:item[1] >=10, items))
#filter using python list comprehension
filtered = [item for item in items if item[1] >=10]
print(filtered)
#another example
sw_filtered = list(filter(lambda item:item[1] >=750.0, sw))
sw_filtered = [item for item in sw if item[1] >=750.0]
print(sw_filtered)

#
#Chapter 5.12 Zip Function
print("\nChapter 5.12 Zip FUnction"+"-"*20)
#zipping means combining two or more lists into a list of tuple pairs
list1 = [1,2,3]
list2 = [10,20,30]
list_combined=list(zip(list1,list2))
print()
#example
products = ["product1","product2","product3","product4","product5"]
sales=[435,665,13,2425,598]
quantity_sold = [5,19,1,30,15]
product_sales_quantity_combined = list(zip(products,sales, quantity_sold))
print(product_sales_quantity_combined)
#extra practive with for loop
for product, sale, quantity in product_sales_quantity_combined:
    print(f"Sales for {product} were $ {sale} with {quantity} units sold.")

