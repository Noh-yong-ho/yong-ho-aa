import tkinter as tk
from tkinter import messagebox

def evaluate_score():
    try:
        score = int(entry.get())

        if score < 1 or score > 100:
            messagebox.showwarning("입력 오류", "1부터 100 사이 숫자를 입력하세요.")
            return

        if score < 30:
            messagebox.showinfo("응답", "그 점수는 니얼굴! 용호 외모로 다시 입력요망")
        elif score < 60:
            messagebox.showinfo("응답", "잘못 입력했다.")
        elif score < 80:
            messagebox.showinfo("응답", "용호 사진 보고 다시 한번 잘 생각해봐")
        elif score < 90:
            messagebox.showinfo("응답", "정말 다시 한번 잘 생각해봐")
        else:
            messagebox.showinfo("정답!", "역시 넌 나밖에 몰라 ❤️")
            root.destroy()  # 프로그램 종료

        entry.delete(0, tk.END)  # 입력창 초기화

    except ValueError:
        messagebox.showerror("오류", "숫자만 입력하세요.")

# GUI 창 생성
root = tk.Tk()
root.title("용호의 외모점수는?")

# 라벨
label = tk.Label(root, text="용호의 외모점수는? (1~100):", font=("Arial", 14))
label.pack(pady=10)

# 입력창
entry = tk.Entry(root, font=("Arial", 14), justify='center')
entry.pack(pady=5)

# 버튼
button = tk.Button(root, text="입력", command=evaluate_score, font=("Arial", 12))
button.pack(pady=10)

# 창 실행
root.mainloop()
