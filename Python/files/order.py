def open_and_print_file(file):
    try:
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()

        for line in file_line_list:
            print(line.rstrip('\n'))

        opened_file.close()

    except FileNotFoundError as errmsg:
        print("File not found")
        print(errmsg)
        raise

def open2(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip("\n"))

    except:
        print("file not found")
        raise
    finally:
        print("\nFinished running")


def write_to_file(file, order_time):
    try:
        with open(file, "w") as file:
            file.write(order_time + "\n")

    except FileNotFoundError as errmsg:
        print(errmsg)



write_to_file("order.txt", "las")
open2("order.txt")