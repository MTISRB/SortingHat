import Database.firebase as f


# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():
    f.parse("Database/key/mtisrb-firebase-adminsdk-u1zpn-c585cb5c8c.json")
    my_tup = f.query()
    print(my_tup[0].get())


if __name__ == '__main__':
    main()
