import pickle


def main():
    with open('wawelength.pickle', 'rb') as fp:
        temp = pickle.load(fp)
        print(list(temp))


if __name__ == "__main__":
    main()
