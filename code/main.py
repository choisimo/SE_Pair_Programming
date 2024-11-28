todo_list = []

def load_todo_list():
    if len(todo_list) == 0:
        print("To-Do List 파일이 존재하지 않습니다.")
    else:
        count=0
        print("현재 To-Do List:")
        for task in todo_list:
            count += 1
            print(f"{count}. {task} \n")


def add_task():
    new_task = str(input("새로운 할 일을 입력하세요: "))

    if new_task in todo_list:
        print("이미 To-Do List에 존재하는 할 일입니다. \n")
        return

    todo_list.append(new_task)
    print(f"새로운 할 일 '{new_task}'가 To-Do List에 추가되었습니다.\n")

def main():
    while True:
        print("\n-------------------------------\n")
        print("1. To-Do List 불러오기")
        print("2. 새로운 할 일 추가하기")
        print("3. 종료")
        print("-------------------------------\n")

        choice = int(input("선택하세요 (1, 2 또는 3): "))

        if choice == 1:
            load_todo_list()
        elif choice == 2:
            add_task()
        elif choice == 3:
            print("프로그램을 종료합니다.")
            break
        else:
            print("1, 2 또는 3 중에서 선택하세요.")


if __name__ == "__main__":
    main()
