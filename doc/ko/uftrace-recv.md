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

    # 서버 
    $ uftrace recv -d recv_data --port 1234

위의 명령어는 지정된 포트 `1234`를 사용하여 서버를 시작하고, 원격 클라이언트에서 
데이터를 수신한다.

    # 클라이언트 :
    $ uftrace record -H localhost -d example_data --port 1234 example

Above command sends the trace data to a remote server that pointed by given
-H option (`localhost` in this case) after running the example program.  And
as you see, you can choose save directory by using `-d` option (sending data
will save to `example_data` in this case).

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

You can find saved trace data of example from `recv_data`'s subdirectory
`example_data`.  Obviously, you should check at `HOST`.


추가정보
========
`uftrace`(1), `uftrace-record`(1)


번역자
========
김관영 <gy741.kim@gmail.com>
