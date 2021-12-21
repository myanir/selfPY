def amount_of_oranges(big_glass=10, small_glass=20):
    orange_result = small_glass+big_glass * 3
    kg_result = orange_result / 5
    print("today you'll need ", orange_result, "oranges")
    print("buy", kg_result, "kg of oranges")
    return orange_result, kg_result


#oranges_number, kg_oranges = amount_of_oranges(3, 5)
#print("oranges_number", oranges_number, "\nkg_oranges", kg_oranges)
amount_of_oranges()