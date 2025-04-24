import random
from game_data import data  # 匯入包含帳號資料的模組
from art import vs, logo      # 匯入包含 logo 和 vs 圖案的模組


# 從 game_data 中隨機取得一筆帳號資料
def get_random_account():
    return random.choice(data)

# 格式化帳號資料成可讀取的字串
def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

# 檢查使用者的答案是否正確
def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# 主遊戲邏輯
def game():
    print(logo)  # 顯示遊戲標誌
    score = 0  # 初始分數
    game_should_continue = True  # 控制遊戲是否繼續
    account_a = get_random_account()
    account_b = get_random_account()

    # 如果一開始 A 跟 B 抽到的是同一筆帳號，重新抽 B
    while account_a == account_b:
        account_b = get_random_account()

    while game_should_continue:
        # 顯示帳號 A 的資訊
        print(f"Compare A: {format_data(account_a)}")
        print(vs)  # 顯示 vs 圖示
        # 顯示帳號 B 的資訊
        print(f"Against B: {format_data(account_b)}")

        # 讓使用者輸入猜測
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # 取得兩個帳號的粉絲數
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        # 判斷是否猜對
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        print(logo)  # 再次顯示 logo
        if is_correct:
            score += 1  # 答對加分
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False  # 猜錯就結束遊戲
            print(f"Sorry, that's wrong. Final score: {score}")


# 執行主程式
game()
