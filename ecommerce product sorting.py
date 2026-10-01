# E-Commerce Product Sorting using Divide and Conquer
# Strategy: Merge Sort

def merge_sort(products):
    # Base condition
    if len(products) <= 1:
        return products

    # Divide
    mid = len(products) // 2
    left = merge_sort(products[:mid])
    right = merge_sort(products[mid:])

    # Conquer and Combine
    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i]["price"] <= right[j]["price"]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Product data
products = [
    {"name": "Laptop", "price": 55000},
    {"name": "Smartphone", "price": 25000},
    {"name": "Headphones", "price": 3000},
    {"name": "Smart Watch", "price": 7000},
    {"name": "Keyboard", "price": 1500}
]

print("Products before sorting:")
for product in products:
    print(product["name"], "₹", product["price"])

sorted_products = merge_sort(products)

print("\nProducts sorted by price:")
for product in sorted_products:
    print(product["name"], "₹", product["price"])