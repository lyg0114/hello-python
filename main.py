import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox

def submit_info():
    name = name_input.text()
    email = email_input.text()

    if not name or not email:
        QMessageBox.critical(main_window, "입력 오류", "이름과 이메일을 모두 입력하세요.")
    else:
        info_message = f"이름: {name}\n이메일: {email}"
        QMessageBox.information(main_window, "입력 완료", info_message)
        name_input.clear()
        email_input.clear()


# QApplication 초기화
app = QApplication(sys.argv)

# QMainWindow 생성
main_window = QMainWindow()
main_window.setWindowTitle("사용자 정보 입력")

# QLabel 추가
name_label = QLabel("이름:", main_window)
name_label.move(20, 20)

# QLineEdit (텍스트 입력 필드) 추가
name_input = QLineEdit(main_window)
name_input.move(100, 20)

# QLabel 추가
email_label = QLabel("이메일:", main_window)
email_label.move(20, 50)

# QLineEdit 추가
email_input = QLineEdit(main_window)
email_input.move(100, 50)

# QPushButton (제출 버튼) 추가
submit_button = QPushButton("제출", main_window)
submit_button.move(100, 80)
submit_button.clicked.connect(submit_info)

# 윈도우 표시
main_window.setGeometry(100, 100, 300, 150)
main_window.show()

# 이벤트 루프 시작
sys.exit(app.exec_())
