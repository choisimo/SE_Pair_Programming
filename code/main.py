todo_list = []

def load_todo_list():
    if len(todo_list) == 0:
        print("To-Do List 파일이 존재하지 않습니다.")
    else:
        count=0
        print("현재 To-Do List:")
        for task in todo_list:
            count += 1
            print(f"{count}. {task}")


def add_task():
    new_task = str(input("새로운 할 일을 입력하세요: "))
    todo_list.append(new_task)


def main():
    print("1. To-Do List 불러오기")
    print("2. 새로운 할 일 추가하기")
    choice = int(input("선택하세요 (1 또는 2): "))
    if choice == 1:
        load_todo_list()
    elif choice == 2:
        add_task()
    else:
        print("1 또는 2 중에서 선택하세요.")

if __name__ == "__main__":
    main()
