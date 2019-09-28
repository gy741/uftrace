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
:   Specify directory name to save received data.

\--port=*PORT*
:   Use given port instead of the default (8090).

\--run-cmd=*COMMAND*
:   Run given (shell) command as soon as receive data.  For example, one can
    run `uftrace replay` for received data.


예제
=======
The uftrace recv command should be run before sending data by record command.

    # HOST 
    $ uftrace recv -d recv_data --port 1234

Above command starts a server with port by given (default `8090`) to receive
data from remote client.

    # CLIENT :
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
