# Ver 2
import pandas as pd

def get_top100(filename, header):
    df = pd.read_csv(filename, header=None)
    df = df.rename(columns=header)
    return df

def find_top_artists(artist_list):
    return [artist_list["가수"].value_counts().idxmax(), 
            artist_list["가수"].value_counts().max()]

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
    header = {0: "곡번호", 1: "노래제목", 2: "앨범제목", 3: "가수"}        
    top100 = get_top100("20240502_melon_top100.csv", header=header)
    top_artists = find_top_artists(top100)
    print(top_artists)
    # topk_artists = find_top5_artists(top100)
    # print(topk_artists)
