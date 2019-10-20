#!/usr/bin/env python

from runtest import TestBase
import subprocess as sp

TDIR='xxx'

class TestCase(TestBase):
    def __init__(self):
        TestBase.__init__(self, 'sort', """
Total time,Self time,Calls,Function
 10.283 ms,109.645 us,1,main
 10.136 ms, 30.007 us,1,bar
 10.106 ms, 10.106 ms,1,usleep
 36.873 us,  1.770 us,2,foo
 35.103 us, 35.103 us,6,loop
  0.903 us,  0.903 us,1,__monstartup
  0.526 us,  0.526 us,1,__cxa_atexit
""")

    def pre(self):
        record_cmd = '%s record -d %s %s' % (TestBase.uftrace_cmd, TDIR, 't-' + self.name)
        sp.call(record_cmd.split())
        return TestBase.TEST_SUCCESS

    def runcmd(self):
        return '%s report --format csv -d %s' % (TestBase.uftrace_cmd, TDIR)

    def post(self, ret):
        sp.call(['rm', '-rf', TDIR])
        return ret

    def sort(self, output):
        """ This function post-processes output of the test to be compared .
            It ignores blank and comment (#) lines and remaining functions.  """
        result = []
        for ln in output.split('\n'):
            if ln.strip() == '':
                continue
            line = ln.split()
            if line[0] == 'Total':
                continue
            if line[0].startswith('='):
                continue
            # A report line consists of following data
            # [0]         [1]   [2]        [3]   [4]     [5]
            # total_time  unit  self_time  unit  called  function
            try:
                if line[5].startswith('__'):
                    continue
            except:
                pass
            result.append('%s %s' % (line[4], line[5]))

        return '\n'.join(result)
