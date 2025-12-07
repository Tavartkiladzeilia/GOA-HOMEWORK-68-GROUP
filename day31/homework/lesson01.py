# პარამეტრი - ეს ცვლადი არის რომელიც ფუნქციის დეფინიციის დროს შეიქმნება და გამოიყენება იმისთვის  რომ ფუნქციაში გადაეცემა მონაცემები
# არგუმენტი - და არგუმენტი ეს არის ის მონაცემები  რომლებიც ფუნქციას გადაეცემა ფუნქციის გამოძახების დროს

# es aris 1 davaleba

# meore ver mivxvdi

def sum_of_numbers(numbers):
    return sum(numbers)

numbers = [1, 2, 3, 4]
print("Sum:", sum_of_numbers(numbers))


# es aris 3 davaleba


names = ["ilia", "giorgi", "noe", "vano", "nika", "mari"]

def filter_long_names(names):
    long_names = []
    for name in names:
        if len(name) > 5:
            long_names.append(name)
    return long_names

print(filter_long_names(names))


# es aris 4 davaleba


def filter_long_names(names):
    return [name for name in names if len(name) >= 5]

names = ["Nikoloz", "Luka", "Giorgi", "Ana", "David"]
print("Long names:", filter_long_names(names))


# es aris 5 davaleba

numbers = [1, 4, 7, 9, 13]
def reverse_list(nums):
    reverse_list-[]
    for i in range( len(numbers)):
        reverse_list.append(nums[(i+1) *-1])
    return reverse_list

print(reverse_list(numbers))



# es aris 6 davaleba