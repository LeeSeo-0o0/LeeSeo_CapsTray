import sys
import win32api
import os
from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

# Caps Lock 상태 확인 함수
def check_caps_lock():
    return win32api.GetKeyState(0x14) & 0x0001  # Caps Lock 상태 확인

# 메인 프로그램
def main():
    app = QApplication(sys.argv)

    # 시스템 트레이 아이콘 생성
    tray_icon = QSystemTrayIcon()
    tray_icon.setIcon(QIcon("b.ico"))  # 초기 아이콘 설정 (소문자 상태)

    # 트레이 아이콘 메뉴 설정 (필요시)
    tray_menu = QMenu()
    quit_action = QAction("Quit", app)
    quit_action.triggered.connect(app.quit)
    tray_menu.addAction(quit_action)
    tray_icon.setContextMenu(tray_menu)

    # 트레이 아이콘 보이기
    tray_icon.setVisible(True)

    # Caps Lock 상태에 따라 아이콘 업데이트
    def update_icon():
        caps_lock_state = check_caps_lock()
        icon_path = "a.ico" if caps_lock_state else "b.ico"
        if os.path.exists(icon_path):
            tray_icon.setIcon(QIcon(icon_path))

    # 타이머를 이용해 1초마다 Caps Lock 상태를 확인하고 아이콘을 변경
    timer = QTimer()
    timer.timeout.connect(update_icon)
    timer.start(1000)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
