% UFTRACE-RECV(1) Uftrace User Manuals
% Namhyung Kim <namhyung@gmail.com>
% Sep, 2018

이름
====
uftrace-recv - 네트워크를 통해 추적 데이터를 수신하고 파일로 저장한다.


사용법
========
uftrace recv [*옵션*]


설명
===========
uftrace recv 명령어는 네트워크를 통해 추적 데이터를 수신하고 파일로 저장한다.
추적 데이터는 `uftrace-record` 명령어와 -H/\--host 옵션을 사용하여 전송된다.


옵션
=======
-d *DATA*, \--data=*DATA*
:   수신된 추적 데이터를 저장할 디렉터리 이름을 지정한다.

\--port=*PORT*
:   기본 포트(8090) 대신 사용할 포트 번호를 지정한다.

\--run-cmd=*COMMAND*
:   추적 데이터를 수신한 다음 즉시 실행할 명령어(쉘)를 설정한다. 예를들어,
    수신된 추적 데이터에 대해 `uftrace replay` 명령어를 실행할 수 있다.


예제
=======
uftrace recv 명령은 `uftrace-record` 명령어로 데이터를 전송하기 전에 먼저 실행되어야 한다.

    # 호스트 
    $ uftrace recv -d recv_data --port 1234

위의 명령어는 지정된 포트 `1234`를 사용하여 추적 데이터를 수신할 준비를 마치고, 원격 클라이언트에서 
데이터를 수신하기 위해 한다.

    # 클라이언트 :
    $ uftrace record -H localhost -d example_data --port 1234 example

위의 명령어는 `example` 프로그램을 실행을 `-d` 옵션을 사용하여 `example_data` 디렉터리 이름을 지정한 다음
-H 옵션을 사용하여 추적 데이터를 수신할 호스트를 설정하고 추적 데이터를 전송한다. 
최종적으로, 위의 명령어의 호스트는 `localhost`이고 포트번호는 `1234`이며,
클라이언트에서 호스트로 전송될 추적 데이터의 디렉터리는 `example_data`이 된다.

    # HOST : Check received data
    $ uftrace replay -d recv_data/example_data
    # DURATION    TID     FUNCTION
                [17308] | main() {
                [17308] |   a() {
                [17308] |     b() {
                [17308] |       c() {
       1.058 us [17308] |         getpid();
       4.356 us [17308] |       } /* c */
       4.664 us [17308] |     } /* b */
       4.845 us [17308] |   } /* a */
       5.076 us [17308] | } /* main */

호스트에서 지정한 `recv_data` 디렉터리의 하위 디렉터리에서 `example_data` 추적 데이터를 찾을 수 있다.
추적데이터가 정상적으로 수신되었는지 호스트에서 확인해야한다.


추가정보
========
`uftrace`(1), `uftrace-record`(1)


번역자
========
김관영 <gy741.kim@gmail.com>
