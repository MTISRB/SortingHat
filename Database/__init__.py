from Database.fb_db import fill_fb, load_data, parse, query, reference, upload, print_db, retrieve_data, MAIN_ROOT


def init(fb_key: str):
    parse(fb_key)
    fill_fb(load_data("resources/Database.xlsx", "database"))


def get_data(key) -> tuple:
    data = retrieve_data()
    for x in data:
        if key in x:
            return x
    else:
        print("The key doesn't exist in the database!")
        return ()