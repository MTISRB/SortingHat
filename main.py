import Database.firebase as f


# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():
    f.load_data("resources/Database.xlsx", "database")
    # f.fill_fb(f.load_data("resources/Database.xlsx", "database"))

if __name__ == '__main__':
    main()
