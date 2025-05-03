import sys
import time


# フルーツリストの中身を表示
def display_fruits(fruits):
    print("現在のフルーツリスト:")
    for fruit in fruits:
        print(fruit)


# フルーツリストに新たなフルーツを追加
def add_fruits(fruits):
    fruit = input("追加するフルーツ：")
    if fruit in fruits:
        print(f"{fruit}はすでにリストに入っています。")
    else:
        fruits.append(fruit)
        print(fruit + "をリストに追加しました。")


# フルーツリストから指定のフルーツを削除
def remove_fruit(fruits):
    fruit = input("削除するフルーツ：")
    if fruit in fruits:
        fruits.remove(fruit)
        print(fruit + "をリストから削除しました。")
    else:
        print(fruit + "はリストにありません。")


# フルーツリストの中のアイテムを数える
def count_fruits(fruits):
    print("リストには" + str(len(fruits)) + "種類の果物があります。")


# メインプログラム
def main():
    fruits = ["apple", "banana", "cherry"]  # フルーツリストの初期値
    display_fruits(fruits)
    
    while True:
        """
        アルファベット1文字のコマンドで、それぞれに対応した機能を実行
        a:追加
        r:削除
        d:表示
        c:カウント
        """

        # 各コマンドの機能の説明を表示
        setsumei = "コマンドを入力してください\n"\
                        "a:フルーツを追加\n"\
                        "r:フルーツを削除\n"\
                        "d:フルーツをリストを表示\n"\
                        "c:フルーツをリストの中の数を表示\n"\
                        "コマンド："
        command = input(setsumei)
        
        # それぞれのコマンドに対応した関数を実行
        match command:
            case "a":
                add_fruits(fruits)

            case "r":
                remove_fruit(fruits)

            case "d":
                display_fruits(fruits)

            case "c":
                count_fruits(fruits)

            case "q":
                sys.exit()

            case _:
                print("コマンドが間違っています。")

        # 区切り線を表示
        print("---------------------------")

        # 次のコマンド入力まで2秒待つ
        time.sleep(2.0)


if __name__ == "__main__":
    main()
