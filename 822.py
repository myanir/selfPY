def sort_prices(list_of_tuples):
    sortedproducts = sorted(list_of_tuples, key=price, reverse=True)
    print(sortedproducts)
    for i in sortedproducts:
        print(i[0], i[1])


def price(mytuple):
    return float(mytuple[1])


products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
sort_prices(products)
