"""Restaurant rating lister."""


# put your code here
def restaurant_rating(filename):
    user_name = input("Enter restaurant name:")
    user_score = input("Enter score:")

#empty dictionary, open file name, unpack list
    rest_data = {}
    with open(filename) as file:
        for line in file:
            name, rating = line.rstrip().split(":")
            rest_data[name] = rating

        rest_data[user_name] = user_score

        sorted_rest_data = sorted((rest_data.items()))
        for restaurant in sorted_rest_data:
            restaurant_name = restaurant[0]
            restaurant_rating = restaurant[1]

            print(f"{restaurant_name} is rated at {restaurant_rating}")
