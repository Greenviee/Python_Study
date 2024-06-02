# Ver 1.2

import csv

# 1. CSV -> 딕셔너리 {"가수명": [곡,,,,]}
def get_top100(filename):
    top100 = []
    with open(filename, "r", encoding="utf-8") as f:
        for i in csv.DictReader(f):
            top100.append(i)
    return top100

# 3. 이거 개선 가능
# len(top100.value)
def find_top_artists(artist_list):
    top_artist, max_songs = None, 0
    for artist, songs in artist_list.items():
        if len(songs) > max_songs:
            top_artist, max_songs = artist, len(songs)
    return [top_artist, max_songs]

# 4. 이거 top5 구해보세요!
def find_top5_artists(artist_list):
    def second_element(d):
        return d[1]
    count_dict = {}
    for key in artist_list:
        if isinstance(artist_list[key], list):
            count_dict[key] = len(artist_list[key])
    return list(sorted(count_dict.items(), key=second_element, reverse=True))[:5]

if __name__ == "__main__":
    top100 = get_top100("20240502_melon_top100.csv")
    print(top100[0])
    # top_artists = find_top_artists(top100)
    # topk_artists = find_top5_artists(top100)
    # print(topk_artists)
