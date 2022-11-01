import Database as f


# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():

    f.parse('../Scrolls5_key.json')
    f.fill_fb(f.load_data("resources/Database.xlsx", "database"))
    f.query()

if __name__ == '__main__':
    main()
