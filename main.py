import Database as f


# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():
    f.parse('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-13e20fa0ad.json')
    f.fill_fb(f.load_data("resources/Database.xlsx", "database"))


if __name__ == '__main__':
    main()
