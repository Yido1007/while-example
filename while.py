i=0
piece=int(input("Enter the number of products: "))
products=[]
while i<piece:
    productName=input("Enter the product name:")
    Price=input("Enter the product price:")
    products.append({
        'productName':productName,
        'Price':Price
    })
    i+=1

for product in products:
    print(f"Product name: {product['productName']} price: {product['Price']}")