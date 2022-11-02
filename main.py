import Database as f
import algorithm as a


# PLACE ALL YOUR CODE TO RUN/TEST HERE!
def main():
    f.init('../Firebase key/mtisrb-firebase-adminsdk-u1zpn-13e20fa0ad.json', fill=True)
    # for i in range(15):
    #     f.upload("user_answers", i, f"Hello world {i}")
    a.Algorithm.init(data=[
        f.get_data("answers"),
        f.get_data("field_of_study"),
        f.get_data("question"),
        f.get_data("points"),
        f.get_data("user_answers"),
    ])

    a.Algorithm.cs()


if __name__ == '__main__':
    main()
