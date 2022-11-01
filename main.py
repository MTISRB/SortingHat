import Database.firebase as f


# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():
    f.parse("mtisrb-firebase-adminsdk-u1zpn-69584df402.json")
    my_tup = f.query()
    print(my_tup[0].get())


if __name__ == '__main__':
    main()
