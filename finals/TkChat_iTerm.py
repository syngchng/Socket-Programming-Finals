#!/usr/bin/python
# -*- coding: UTF-8 -*-

import _socket as soc
import threading
import tkinter


# print("\n ----------------------------------------------------------- \n")
# print("\t\t WELCOME TO UDP CHAT FOR iTerm \n")
# print("\t\t\t iTerm 을 위한 UDP 채팅 \n")
# print("\n ----------------------------------------------------------- \n")

# IP 및 포트 번호 지정
iterm_ip = "127.0.0.1"
iterm_port = 1234
inal_ip = "127.0.0.1"
inal_port = 2222

# 소켓 생성 및 IP, 포트 번호 바인딩
ms = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)
ms.bind((iterm_ip, iterm_port))

# 메세지를 받아오고 상대가 q 혹은 Q 입력 시 오프라인으로 전환했다는 메세지를,
# 그렇지 않을 시 상대가 전송해온 메세지 내용을 출력하는 메소드
def receive():
    flag = 1
    while flag:
        # 메세지 받아오기
        msg_rec = ms.recvfrom(1024)
        msg_dec = msg_rec[0].decode()
        # 받은 메세지 출력
        msg_inal = "\n\t FROM Terminal : " + msg_dec
        # 메세지가 q/Q일 떄
        if msg_dec == "q" or msg_dec == "Q":
            msg_inal = "\n\t Terminal WENT OFFLINE"
            flag = 0
        return msg_inal


# 보낼 메세지를 입력받고 전송하는 메소드
def send():
    flag = True
    while flag:
        # 메세지 입력받기
        # raw_input을 쓴 이유는 그냥 input 사용 시 NameError가 뜨기 때문
        msg_send = entry_msgsend.get()
        # 메세지 전송
        ms.sendto(msg_send.encode(), (inal_ip, inal_port))
        # 메세지가 q/Q인지 점검, 맞을 시 종료
        if msg_send == "q" or msg_send == "Q":
            flag = False
            break


# 메세지를 보내기 위한 스레드 선언
t1 = threading.Thread(target=send)

# 메세지를 받아오기 위한 스레드 선언
t2 = threading.Thread(target=receive)

# 스레드 구동
t1.start()
t2.start()

w = tkinter.Tk()
w.title("iTerm 을 위한 UDP 채팅")

lbl_inal = tkinter.Label(w, text=receive())
lbl_send = tkinter.Label(w, text="YOUR MESSAGE (Q TO QUIT) : ")

entry_msgsend = tkinter.Entry(w)

btn_send = tkinter.Button(w, text="SEND", command=receive and send)


lbl_inal.grid(row=0, column=0, columnspan=2)
lbl_send.grid(row=1, column=0)
entry_msgsend.grid(row=1, column=1)
btn_send.grid(row=2, column=0, columnspan=2, sticky='nswe')

w.mainloop()
