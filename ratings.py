"""Restaurant rating lister."""


file_obj = open("scores.txt")
result_dict = {}
for line in file_obj:
    restaurant = line.rstrip().split(":")
    name, rating = restaurant
    result_dict[name] = rating


def add_restaurant():
    new_restaurant = input('Enter a new restaurant: ')
    while True:
        new_rating = input("Enter a new rating: ")

        try:
            new_rating = int(new_rating)
        except ValueError:
            print("Invalid option. Try again")
            continue

        if new_rating > 5 or new_rating < 1:
            print("Invalid input. Please enter an integer between 1 and 5.")

        else:
            break

    result_dict[new_restaurant] = new_rating
    return result_dict


def print_dict(result_dict):

    for name, rating in sorted(result_dict.items()):
        print(f"{name} is rated at {rating}.")


def get_random():
    from random import choice
    restaurant_lst = []
    for key in result_dict:
        restaurant_lst.append(key)
    rand_one = choice(restaurant_lst)
    print(f"{rand_one} has a rating of {result_dict[rand_one]}.")
    updated_rating = int(input("Enter new rating: "))
    result_dict[rand_one] = updated_rating


# put your code here
while True:
    choice = input(
        "Enter 'V' to view ratings,'A' to add restaurant,'U' to update a random restaurant's rating, or 'Q' to quit: ")

    if choice == 'V':
        print_dict(result_dict)
    elif choice == 'A':
        add_restaurant()
    elif choice == 'U':
        get_random()
    elif choice == 'Q':
        break
