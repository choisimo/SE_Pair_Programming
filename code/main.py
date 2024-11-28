todo_list = []

def load_todo_list():
    if len(todo_list) == 0:
        print("To-Do List 파일이 존재하지 않습니다.")


def add_task():
    """
    새로운 할 일을 입력받아 To-Do List에 추가하고 저장하느 함수
    """

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
