import csv


class MelonTop100:
    def __init__(self, filename="20240502_melon_top100.csv"):
        self.filename = filename
        self.top100 = self.load_top100()
        self.artist_list = self.get_artists()

    def load_top100(self):
        top100 = []
        with open(self.filename, "r", encoding="utf-8") as f:
            for i in csv.reader(f):
                top100.append(i)
        return top100

    def get_artists(self):
        return [line[-1].strip('"') for line in self.top100]

    def find_top_artist(self):
        artist_counts = {}
        for artist in self.artist_list:
            if artist in artist_counts:
                artist_counts[artist] += 1
            else:
                artist_counts[artist] = 1

        top_artist, max_songs = None, 0
        for artist, count in artist_counts.items():
            if count > max_songs:
                top_artist, max_songs = artist, count
        return [top_artist, max_songs]


chart = MelonTop100()
top_artist, number_of_songs = chart.find_top_artist()
print(
    f"가장 많은 곡을 보유하고 있는 가수는 {top_artist}이며, 멜론 Top100에 등록된 노래는 총 {number_of_songs}곡 입니다."
)
