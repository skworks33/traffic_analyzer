import os 
import googlemaps
import csv
from datetime import datetime

# スクリプトのあるディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# カレントディレクトリを変更
os.chdir(script_dir)

# 環境変数からAPIキーと地点情報を取得
gmap_api_key = os.environ["GMAP_API_KEY"]
origin = os.environ["ORIGIN"]
destination = os.environ["DESTINATION"]

# APIキーをセット
gmaps = googlemaps.Client(key=gmap_api_key)

# CSVファイルをオープン
with open('travel_time.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # 現在の時間
    now = datetime.now()

    # 所要時間を取得
    directions_result = gmaps.directions(origin,
                                         destination,
                                         mode="driving", # 車の場合の所要時間
                                         departure_time=now, # 現在時刻から出発
                                         avoid="tolls|highways|ferries", # 有料・高速・フェリーを避ける
                                        )

    # 所要時間を取得
    duration = directions_result[0]['legs'][0]['duration']['text']
    
    # CSVファイルに時間と所要時間を書き込む
    writer.writerow([now, duration])

    print(f"所要時間: {duration} がCSVファイルに保存されたよ！")

