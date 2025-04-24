# 導入必要的模組
import random  # 用於隨機選擇帳戶
from game_data import data  # 導入遊戲數據，包含名人資訊
from art import logo, vs  # 導入遊戲的圖形藝術元素

# 隨機從數據中選擇一個名人帳戶
def get_random_account():
    """從數據列表中隨機返回一個名人帳戶"""
    return random.choice(data)

# 格式化名人資訊以便顯示
def format_data(account):
    """將帳戶資訊格式化為可讀字串"""
    name = account["name"]  # 獲取名人姓名
    description = account["description"]  # 獲取名人描述
    country = account["country"]  # 獲取名人國家
    return f"{name}, a {description}, from {country}."  # 返回格式化的字串

# 檢查玩家的猜測是否正確
def check_answer(guess, a_followers, b_followers):
    """比較粉絲數量並檢查玩家猜測是否正確"""
    if a_followers > b_followers:  # 如果A的粉絲數量大於B
        return guess == "a"  # 如果玩家猜A，返回True
    else:  # 如果B的粉絲數量大於或等於A
        return guess == "b"  # 如果玩家猜B，返回True

# 主遊戲函數
def game():
    """執行高低猜測遊戲的主要邏輯"""
    print(logo)  # 顯示遊戲標誌
    score = 0  # 初始化分數為0
    game_should_continue = True  # 設置遊戲繼續的標誌
    
    # 選擇初始的兩個帳戶
    account_a = get_random_account()  # 隨機選擇帳戶A
    account_b = get_random_account()  # 隨機選擇帳戶B
    
    # 確保A和B是不同的帳戶
    while account_a == account_b:
        account_b = get_random_account()
    
    # 主遊戲循環
    while game_should_continue:
        # 顯示比較資訊
        print(f"Compare A: {format_data(account_a)}")  # 顯示A的資訊
        print(vs)  # 顯示VS圖形
        print(f"Against B: {format_data(account_b)}")  # 顯示B的資訊
        
        # 獲取玩家猜測
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()  # 轉換為小寫
        
        # 驗證輸入有效性
        while guess not in ['a', 'b']:
            print("無效輸入！請輸入 'A' 或 'B'")  # 提示無效輸入
            guess = input("Who has more followers? Type 'A' or 'B': ").lower()  # 重新獲取輸入
        
        # 獲取粉絲數量
        a_followers = account_a["follower_count"]  # A的粉絲數
        b_followers = account_b["follower_count"]  # B的粉絲數
        
        # 檢查答案是否正確
        is_correct = check_answer(guess, a_followers, b_followers)
        
        # 顯示兩個帳戶的粉絲數量
        print(f"A: {account_a['name']} 有 {a_followers} 個粉絲")
        print(f"B: {account_b['name']} 有 {b_followers} 個粉絲")
        
        # 處理猜測結果
        if is_correct:
            score += 1  # 增加分數
            print(f"You're right! Current score: {score}.")  # 顯示當前分數
            
            # 將B移到A的位置，然後為B選擇一個新帳戶
            account_a = account_b  # B成為新的A
            account_b = get_random_account()  # 選擇新的B
            
            # 確保新的B與A不同
            while account_a == account_b:
                account_b = get_random_account()
        else:
            game_should_continue = False  # 結束遊戲
            print(f"Sorry, that's wrong. Final score: {score}")  # 顯示最終分數
            
            # 詢問是否再玩一次
            play_again = input("想再玩一次嗎？(y/n): ").lower()
            if play_again == 'y':
                game()  # 重新開始遊戲

# 啟動遊戲
game()
