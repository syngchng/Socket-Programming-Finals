import _socket as soc
import threading


print("\n --------------------------------------------------------------------- \n")
print("\t\t WELCOME TO UDP CHAT FOR Terminal \n")
print("\t\t    Terminal을 위한 UDP 채팅 \n")
print("\n --------------------------------------------------------------------- \n")

# IP 및 포트 번호 지정
inal_ip = "127.0.0.1"
inal_port = 2222
iterm_ip = "127.0.0.1"
iterm_port = 1234

# 소켓 생성 및 IP, 포트 번호 바인딩
ms = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)
ms.bind((inal_ip, inal_port))


# 메세지를 받아오고 상대가 q 혹은 Q 입력 시 오프라인으로 전환했다는 메세지를,
# 그렇지 않을 시 상대가 전송해온 메세지 내용을 출력드하는 메소드
def receive():
    while 1:
        # 메세지 받아오기
        msg_rec = ms.recvfrom(1024)
        msg_dec = msg_rec[0].decode()
        # 메세지가 q/Q인지 점검
        if msg_dec == "q" or msg_dec == "Q":
            print("\n\t iTerm WENT OFFLINE")
            exit(0)
        # 받은 메세지 출력
        print("\n\t FROM iTerm : " + msg_dec)


# 보낼 메세지를 입력받고 전송하는 메소드
def send():
    while 1:
        # 메세지 입력받기
        # raw_input을 쓴 이유는 그냥 input 사용 시 NameError가 뜨기 때문
        msg_send = input("YOUR MESSAGE (Q TO QUIT) : ")
        # 메세지 전송
        ms.sendto(msg_send.encode(), (iterm_ip, iterm_port))
        # 메세지가 q/Q인지 점검, 맞을 시 종료
        if msg_send == "q" or msg_send == "Q":
            exit(0)


# 메세지를 보내기 위한 스레드 선언
t1 = threading.Thread(target=send)

# 메세지를 받아오기 위한 스레드 선언
t2 = threading.Thread(target=receive)

# 스레드 구동
t1.start()
t2.start()
