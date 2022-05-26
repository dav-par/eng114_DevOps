import csv

# with open("user_details.csv", newline="") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#
#     iterable_csv = iter(csvreader)
#     next(iterable_csv)
#     for row in iterable_csv:
#         print(row[-1])

def transform_user_data(csv_file_name):
    new_user_data = []

    with open("user_details.csv", newline="") as csvfile:
        user_details_csv = csv.reader(csv)

        for user in user_details_csv:
            transformation = []
            transformation.append(user[1])
            transformation.append(user[2])
            transformation.append(user[-1])
            new_user_data.append(transformation)

    return new_user_data

def create_new_user_data_csv(old_user_data_file="user_details.csv", new_file_name="new_user_data.csv"):

    new_user_data = transform_user_data(old_user_data_file)
    new_file = open(new_file_name, 'w')

    with new_file:
        csv_writer = csv.writer(new_file)
        csv_writer.writerow(new_user_data)

create_new_user_data_csv()