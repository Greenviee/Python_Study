# Ver 1.2

import csv


def get_top100(filename):
    top100 = []
    with open(filename, "r", encoding="utf-8") as f:
        for i in csv.reader(f):
            top100.append(i)
    return top100


def get_artists(top100_lst):
    artist_list = []
    for line in top100_lst:
        artist_name = line[-1].strip('"')
        artist_list.append(artist_name)
    return artist_list


def find_top_artists(artist_list):
    artist_counts = []

    def find_artist(artist_name):
        for index, (artist, count) in enumerate(artist_counts):
            if artist == artist_name:
                return index
        return -1

    for artist in artist_list:
        index = find_artist(artist)
        if index != -1:
            artist_counts[index][1] += 1
        else:
            artist_counts.append([artist, 1])

    top_artist, max_songs = None, 0
    for artist, count in artist_counts:
        if count > max_songs:
            top_artist, max_songs = artist, count

    return [top_artist, max_songs]


if __name__ == "__main__":
    top100 = get_top100("20240502_melon_top100.csv")
    artists = get_artists(top100)
    print(artists)
    top_artists = find_top_artists(artists)
    print(top_artists)
