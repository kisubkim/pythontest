import os

# 할 일 목록 관리자
# 작성자: 김기섭
# 작성일: 2025년 2월 12일
# 최종 수정일: 2025년 2월 12일


todo_list = ["파이썬 공부", "알고리즘 공부", "운동하기", "영어 공부"]

while True:
    print("")
    print("할 일 목록 관리자")
    print("1. 할 일 목록 보기")
    print("2. 할 일 추가")
    print("3. 할 일 수정")
    print("4. 할 일 삭제")
    print("5. 종료")

    choice = input("메뉴를 선택하세요: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if choice == "1":
        print("할 일 목록 보기를 선택하셨습니다.")
        print("할 일 목록")
        for i, todo in enumerate(todo_list):
            print(f"{i+1}. {todo}")
    elif choice == "2":
        print("할 일 추가를 선택하셨습니다.")
        todo = input("할 일을 입력하세요: ")
        todo_list.append(todo)
        print(f"{todo}이(가) 추가되었습니다.")
    elif choice == "3":
        print("할 일 수정을 선택하셨습니다.")
    elif choice == "4":
        print("할 일 삭제를 선택하셨습니다.")
        todo = input("삭제할 할 일을 입력하세요: ")
        if todo in todo_list:
            todo_list.remove(todo)
            print(f"{todo}이(가) 삭제되었습니다.")
        else:
            print("해당 할 일이 목록에 없습니다.")
    elif choice == "5":
        print("종료를 선택하셨습니다.")
        break
    else:
        print("잘못된 선택입니다.")

