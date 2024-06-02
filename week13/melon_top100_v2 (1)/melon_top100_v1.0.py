# Ver 1


def get_top100(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [i.strip().split(",") for i in f.readlines()]


def get_artists(top100_lst):
    return [line[-1] for line in top100_lst]


def find_top_artists(artist_list):
    return Counter(artist_list).most_common()[0]


if __name__ == "__main__":
    top100 = get_top100("20240502_melon_top100.csv")
    artists = get_artists(top100)
    print(artists)
    top_artists = find_top_artists(artists)
    print(top_artists)
