print("Enter the number of people who watched show 1")
num_people_1 = int(input())
print("Enter the average rating for show 1")
avg_rating_1 = float(input())

print("Enter the number of people who watched show 2")
num_people_2 = int(input())
print("Enter the average rating for show 2")
avg_rating_2 = float(input())

print("Enter the number of people who watched show 3")
num_people_3 = int(input())
print("Enter the average rating for show 3")
avg_rating_3 = float(input())

overall_avg_rating = ((num_people_1 * avg_rating_1) + (num_people_2 * avg_rating_2) + (num_people_3 * avg_rating_3)) / (num_people_1 + num_people_2 + num_people_3)

print(f"The overall average rating for the show is {overall_avg_rating:.2f}")
