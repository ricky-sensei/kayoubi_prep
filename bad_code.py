import sys
import time
def hyouji_fruits(fruits):
    print("現在のフルーツリスト:")
    for fruit in fruits:
        print(fruit)
def add_fruits(fruits):
    fruit = input("追加するフルーツ：")
    if fruit in fruits:
        print(f"{fruit}はすでにリストに入っています。")
    else:
        fruits.append(fruit)
        print(fruit + "をリストに追加しました。")
def sakujyo_fruit(fruits):
    fruit = input("削除するフルーツ：")
    if fruit in fruits:
        fruits.remove(fruit)
        print(fruit + "をリストから削除しました。")
    else:
        print(fruit + "はリストにありません。")
def count_fruits(fruits):
    print("リストには" + str(len(fruits)) + "種類の果物があります。")
def main():
    fruits = ["apple", "banana", "cherry"]  
    hyouji_fruits(fruits)
    while True:
        setsumei = "コマンドを入力してください\n"\
                        "a:フルーツを追加\n"\
                        "r:フルーツを削除\n"\
                        "d:フルーツをリストを表示\n"\
                        "c:フルーツをリストの中の数を表示\n"\
                        "コマンド："
        command = input(setsumei)
        match command:
            case "a":
                add_fruits(fruits)
            case "r":
                sakujyo_fruit(fruits)
            case "d":
                hyouji_fruits(fruits)
            case "c":
                count_fruits(fruits)
            case "q":
                sys.exit()
            case _:
                print("コマンドが間違っています。")
        print("---------------------------")
        time.sleep(2.0)
if __name__ == "__main__":
    main()
