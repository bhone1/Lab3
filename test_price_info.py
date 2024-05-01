import price_info

def test_total_cost_shopping():
    assert(price_info.total_cost_shopping() == 46.75)

def test_cost_of_fruits():
    fruit_costs = { 'apple' : 6.00, 'orange':7.00, 'watermelon': 6.50, 'pineapple': 5.40, 'pear' : 9.00, 'papaya': 2.95, 'pomegranate': 9.90 }
    for key in price_info.price_list.keys():
        assert(price_info.cost_of_fruits(key,price_info.quantity_list[key]) == fruit_costs[key])