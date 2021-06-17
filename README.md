# Socket-Programming-Finals
TCP/IP Socket Programming final assignment

# 개요
UDP 소켓을 이용한 Mac OS Terminal - Mac iTerm2 간의 채팅 서버 기능을 구현하고자 하였다.<br><br>

# 목적
원래는 윈도우와 맥 터미널 간의 채팅 서버를 구현하고자 하였으나 두 OS 간의 차이점과 접근 권한, 버전 등 어려움이 너무 많았고,<br>
이에 따라 올려놓은 코드의 기능을 tKinter (파이썬 GUI) 창을 이용할 수 있도록 구현하고자 하였으나<br><br>

<img width="466" alt="Screenshot 2021-06-17 at 23 59 14" src="https://user-images.githubusercontent.com/74042902/122422518-2c629880-cfc8-11eb-989e-35764b72747e.png"><br>
<img width="470" alt="Screenshot 2021-06-17 at 23 59 28" src="https://user-images.githubusercontent.com/74042902/122422565-371d2d80-cfc8-11eb-9490-d5c16be63a1f.png"><br><br>
위와 같이 겉모습은 나오지만 <br>

아래와 같은 내용의 에러를 지속적으로 만났고<br><br>
<img width="609" alt="Screenshot 2021-06-17 at 23 59 34" src="https://user-images.githubusercontent.com/74042902/122422668-4a2ffd80-cfc8-11eb-9d06-744db5df459b.png"><br><br>
결국 해결하지 못한 관계로 성공한 코드에 대해서 먼저 설명드리도록 하겠습니다.<br><br>
위 사진에 보이는 코드는 TkChat_이라는 이름으로 첨부만 하였습니다.<br>

# 설계 및 기능
두 파이썬 파일을 동시에 터미널에서 실행시키면, 아래 실행 화면처럼 텍스트가 출력됩니다.<br><br>

이 때 어느 한 쪽에서 메세지를 치면 상대방 쪽에는<br>
<code>FROM ( 상대방 ) : < 메세지 ></code><br>
형식으로 뜹니다. <br><br>

이와 같은 방식으로 메세지를 주고받다가, 어느 한 쪽이 q나 Q를 입력하여 접속을 종료할 시에는 <br>
  상대방 쪽에 <code>( 상대방 ) WENT OFFLINE</code> 이라는 문구가 뜹니다.<br><br>


# 차이점
기존 수업에서 한 클라이언트 사용자의 메세지를 미러링하는 코드와는 달리<br>
해당 코드는 양 쪽에서 서로 메세지를 주고받는 것을 확인할 수 있다. <br><br>
<img width="1018" alt="Screenshot 2021-06-17 at 22 39 33" src="https://user-images.githubusercontent.com/74042902/122410485-ece37e80-cfbe-11eb-8cd2-8ab8deac4cf6.png"><br><br>

# 실행 화면
<br>
iTerm2
<br><br>
<img width="573" alt="Screenshot 2021-06-17 at 22 39 55" src="https://user-images.githubusercontent.com/74042902/122410517-f2d95f80-cfbe-11eb-8ee7-498f0551cff2.png"><br><br>

Terminal
<br><br>
<img width="659" alt="Screenshot 2021-06-17 at 22 40 26" src="https://user-images.githubusercontent.com/74042902/122410525-f53bb980-cfbe-11eb-8946-a58bc153a3af.png"><br>

