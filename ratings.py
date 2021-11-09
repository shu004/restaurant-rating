"""Restaurant rating lister."""
FILE_NAME = "scores.txt"



# def restaurant_rating(FILE_NAME):
#     #this returns a list from user input
#     user_rating = user_input()

#     #this combs through the FILE_NAME and add items to a dictionary
#     rest_data = file_to_dict(FILE_NAME)

#     #adding user input to the restaurant data dictionary
#     user_input_name, user_input_score = user_rating
#     rest_data[user_input_name] = user_input_score

#     # sorted_rest_data = sorted((rest_data.items()))
#     # for restaurant in sorted_rest_data:
#     #     restaurant_name = restaurant[0]
#     #     restaurant_rating = restaurant[1]

#     #     print(f"{restaurant_name} is rated at {restaurant_rating}")

# def file_to_dict(filename):
#     new_dict = {}
#     with open(filename) as file:
#         for line in file:
#             key, value = line.rstrip().split(":")
#             new_dict[key] = value

#     return new_dict


def user_choice():

    # user_choose = True

    # while user_choose:
    user_choice = input("Enter N to enter new restaurant or V to view all ratings: ")
    if user_choice == "N" or "n":
        pass




    elif user_choice == "V" or "v":
        pass




    elif user_choice == "q" or "quit":
        #user_choose = False
        pass

    else:
        print("That's not a valid selection")



    #     ask_for_input = False
    #     while not ask_for_input:
    #         user_name = input("Enter restaurant name:").title()
    #         user_score = int(input("Enter score:"))
    #         if user_score < 1 or user_score > 5:
    #             print("Not a valid input, please enter again")
    #         else:
    #             ask_for_input = True
    #     return [user_name,user_score]

    # elif user_choice == "C":
    #     rest_data = file_to_dict(FILE_NAME)
    #     sorted_rest_data = sorted((rest_data.items()))
    #     for restaurant in sorted_rest_data:
    #         restaurant_name = restaurant[0]
    #         restaurant_rating = restaurant[1]

    #         print(f"{restaurant_name} is rated at {restaurant_rating}")

def add_rating():
    ask_for_input = True
    user_rating_dict = {}
    user_name = input("Enter restaurant name: ").title()

    while ask_for_input:
        user_score = int(input("Enter score from 1-5 (5 being the greatest): "))
        if user_score < 1 or user_score > 5:
            print("Not a valid input, please enter again")
        else:
            user_rating_dict[user_name] = user_score
            ask_for_input = False


    return {user_name: user_score}


def view_rating(filename):
    rating_dict = {}
    with open(filename) as file:
        for line in file:
            key, value = line.rstrip().split(":")
            rating_dict[key] = value

    return rating_dict

print(add_rating())