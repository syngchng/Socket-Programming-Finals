#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _socket as soc
import threading
import tkinter

# 소켓 생성
sc = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)

# 메세지를 받아오고 상대가 q 혹은 Q 입력 시 오프라인으로 전환했다는 메세지를,
# 그렇지 않을 시 상대가 전송해온 메세지 내용을 출력하는 메소드
def receive():
    flag = True
    while flag:
        # 메세지 받아오기
        msg_rec = sc.recvfrom(1024)
        msg_dec = msg_rec[0].decode()
        # 받은 메세지 출력
        their_msg = "\t FROM Terminal : " + msg_dec
        # 메세지가 q/Q일 떄
        if msg_dec == "q" or msg_dec == "Q":
            their_msg = "\t Terminal WENT OFFLINE"
            flag = False
        return msg_list.insert(tkinter.END, their_msg)


# 보낼 메세지를 입력받고 전송하는 메소드
def send():
    flag = True
    while flag:
        # 메세지 입력받기
        msg_send = my_msg.get()
        my_msg.set("")
        # 메세지 전송
        sc.sendto(msg_send.encode(), (inal_ip, inal_port))
        # 메세지가 q/Q인지 점검, 맞을 시 종료
        if msg_send == "q" or msg_send == "Q":
            flag = False
            break


# 닫을 때 실행될 메소드
def close():
    my_msg.set("{quit}")
    send()


# 메세지를 보내기 위한 스레드 선언
t1 = threading.Thread(target=send)

# 메세지를 받아오기 위한 스레드 선언
t2 = threading.Thread(target=receive)

# 스레드 구동
t1.start()
t2.start()

# tkinter 창 생성
w = tkinter.Tk()
w.title("iTerm 을 위한 UDP 채팅")
frame = tkinter.Frame(w)

# 보낼 메세지 변수 선언
my_msg = tkinter.StringVar()
my_msg.set("Your message")

# 지난 메세지 스크롤바
scrlbar = tkinter.Scrollbar(frame)

# 지난 메세지 칸
msg_list = tkinter.Listbox(frame, height=15, width=50, yscrollcommand=scrlbar.set)

# 사용을 위한 pack
scrlbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
frame.pack()

# 입력 칸
entry_msg = tkinter.Entry(w, textvariable=my_msg)
entry_msg.setvar("")
entry_msg.bind("<Return>", send)
entry_msg.pack()

# 전송 버튼
btn_send = tkinter.Button(w, text="Send", command=send)
btn_send.pack()

# 창 닫을 시 실행될 메소드 지정
w.protocol("WM_DELETE_WINDOW", close)

#--------------------------------------
# IP 및 포트 번호 지정
iterm_ip = "127.0.0.1"
iterm_port = 1234
inal_ip = "127.0.0.1"
inal_port = 2222

# IP, 포트 번호 바인딩
sc.bind((iterm_ip, iterm_port))


# GUI 실행되게 함
w.mainloop()
