def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    # ユーザーから入力を受け取る（カンマ区切り）
    input_str = input("数字をカンマで区切って入力してください: ")
    try:
        number_list = [float(num.strip()) for num in input_str.split(",")]
        avg = calculate_average(number_list)
        print(f"平均は: {avg}")
    except ValueError:
        print("無効な入力です。数字をカンマで区切ってください。")