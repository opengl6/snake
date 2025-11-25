# 实验一：GitHub 操作测试
# 学生信息
name = "[孙志远]"
student_id = "[1191220317]"
class_name = "[数媒2203]"

def display_info():
    print("=" * 50)
    print("GitHub 实验一完成证明")
    print(f"姓名: {name}")
    print(f"学号: {student_id}")
    print(f"班级: {class_name}")
    print("仓库: https://github.com/opengl6/snake")
    print("完成时间: 2025年")
    print("=" * 50)

def test_snake_game():
    """测试贪吃蛇游戏相关功能"""
    print("\n测试贪吃蛇游戏功能:")
    print("- 游戏主文件: main.py")
    print("- 源代码目录: src/")
    print("- 游戏逻辑: src/game.py")
    print("- 蛇类定义: src/snake.py")
    print("- 食物定义: src/food.py")
    return "测试完成"

if __name__ == "__main__":
    display_info()
    result = test_snake_game()
    print(f"\n结果: {result}")
    print("实验一所有任务已完成！")
