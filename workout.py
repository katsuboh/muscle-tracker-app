import csv
import os
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

FILE_NAME = "workout_log.csv"

pd.set_option("display.unicode.east_asian_width", True)

def create_file_if_not_exists():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["date", "exercise", "weight", "reps"])

    else:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            first_line = file.readline().strip()

        if first_line != "date,exercise,weight,reps":
            print("ヘッダーを追加します")

            with open(FILE_NAME, "r", encoding="utf-8") as file:
                data = file.read()

            with open(FILE_NAME, "w", encoding="utf-8") as file:
                file.write("date,exercise,weight,reps\n")
                file.write(data)
       
                
def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def add_workout():
    exercise = input("種目名を入力してください: ")
    weight = input("重量(kg)を入力してください: ")
    reps = input("回数を入力してください: ")

    if not is_number(weight):
        print("重量は数字で入力してください。")
        return

    if not reps.isdigit():
        print("回数は整数で入力してください。")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, exercise, weight, reps])

    print("筋トレ記録を保存しました！")


# 一時的追加
print("CSV存在:", os.path.exists(FILE_NAME))
print("現在のフォルダ:", os.getcwd())

def show_workouts():
    if not os.path.exists(FILE_NAME):
        print("まだ記録がありません。")
        return

    df = pd.read_csv(FILE_NAME)

    print(df.columns)
    print(df)

    print(f"件数: {len(df)}")
   
print(os.path.abspath(FILE_NAME))
create_file_if_not_exists()

def show_graph():
    if not os.path.exists(FILE_NAME):
        print("まだ記録がありません。")
        return

    df = pd.read_csv(FILE_NAME)

    exercise_name = input("グラフ表示したい種目名を入力してください: ")

    filtered_df = df[df["exercise"] == exercise_name]

    if filtered_df.empty:
        print(f"{exercise_name} の記録がありません。")
        return

    plt.plot(filtered_df["date"], filtered_df["weight"], marker="o")

    plt.title(f"{exercise_name} weight progress")
    plt.xlabel("Date")
    plt.ylabel("Weight(kg)")
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
    
while True:
    print("\n1: 筋トレを記録する")
    print("2: 記録を見る")
    print("3: グラフを見る")
    print("4: 終了する")

    choice = input("番号を選んでください: ")

    if choice == "1":
        add_workout()
    elif choice == "2":
        show_workouts()    
    elif choice == "3":
        show_graph()
    elif choice == "4":
        print("アプリを終了します。お疲れさまでした！")
        break
    else:
        print("1〜4の番号を選んでください。")