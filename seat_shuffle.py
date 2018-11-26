import random


def read01():
    f = open("users_file.txt", mode="r")

    m_list = f.read()
    members = m_list.split("\n")
    print(random.sample(members, 6))
    for member in members:
        print(random.sample(member, 2))

    f.close()


if __name__ == "__main__":
    read01()
