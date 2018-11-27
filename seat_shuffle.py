import random


def read01():
    f = open("users_file.txt", mode="r")

    m_list = f.read()
    members = m_list.split("\n")

    choice1 = random.sample(members, 6)
    for i in range(0, len(choice1)):
        members.remove(choice1[i])

    choice2 = random.sample(members, 5)

    for i in range(0, len(choice2)):
        members.remove(choice2[i])

    choice3 = members

    print(f"table1 :{choice1}\n"
          f"table2 :{choice2}\n"
          f"table3 :{choice3}"
          )


    f.close()


if __name__ == "__main__":
    read01()
