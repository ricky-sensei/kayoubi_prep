import sys
import time


def display_fruits(fruits):
    for fruit in fruits:
        print("好きな果物は" + fruit + "です。")


def add_fruits(fruits, fruit):
    fruits.append(fruit)
    print(fruit + "をリストに追加しました。")


def remove_fruit(fruits, fruit):
    if fruit in fruits:
        fruits.remove(fruit)
        print(fruit + "をリストから削除しました。")
    else:
        print(fruit + "はリストにありません。")


def count_fruits(fruits):
    print("リストには" + str(len(fruits)) + "種類の果物があります。")


def main():
    fruits = ["apple", "banana", "cherry"]
    display_fruits(fruits)
    
    while True:
        command = input("コマンドを入力してください\na:フルーツを追加\nr:フルーツを削除\nd:フルーツをリストを表示\nc:フルーツをリストの中の数を表示\nq:プログラムを終了\n")
        
        match command:
            case "a":
                fruit = input("追加するフルーツ：")
                add_fruits(fruits, fruit)

            case "r":
                fruit = input("追加するフルーツ：")
                remove_fruit(fruits, fruit)

            case "d":
                display_fruits(fruits)

            case "c":
                count_fruits(fruits)

            case "q":
                sys.exit()
        print("---------------------------")
        time.sleep(2.0)
                

if __name__ == "__main__":
    main()
