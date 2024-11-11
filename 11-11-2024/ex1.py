# num = [1,2,3,4]
# z = [5,6,7]
# ok = list(filter(lambda x,y: (y+x)%2==0 , num, z))
# print(ok)

# products = [1,5,3,4]
# sorted_products = sorted(products, key=lambda x: x)

# products = [{101: 'Widget'}, {102: 'Gadget'}, {105: 'Doodad'}, {104: 'Thingamajig'}]
# sorted_products = sorted(products, key=lambda x: x.items()[0])
# print(sorted_products)
a=[1,3,5]
b=[x**2 else 1 for x in a if x<5]
print(b)
# x = ["hello", "hi"]


# def func(x):
#     return len(x)>3
# y = filter(func, x)
# print(list(y))