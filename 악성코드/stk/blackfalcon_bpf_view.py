#!/usr/bin/env python3

#
# write by blackfalcon 
# 
# hacker@hacker:~/bpfdoorpoc$ sudo python3 blackfalcon_bpf_view.py 
# All for One , One for ALL
# Black Falcon
# Starting packet_recvmsg watcher (press Ctrl-C to stop)
#
# 2025-06-19 12:36:12
#
# root        3854    3853  0 12:25 pts/1    00:00:00 ./bpfdoorpoc
# root        4036    4035  0 12:36 pts/3    00:00:00 /bin/sh -c ps -ef | grep 3854
# root        4038    4036  0 12:36 pts/3    00:00:00 grep 3854
#

import glob
import subprocess
import time
import re

OUTPUT_FILE = "/tmp/find.txt"
PID_PATTERN = re.compile(r"/proc/(\d+)/stack")


def find_packet_recvmsg_pids():
    pids = set()
    for path in glob.glob('/proc/*/stack'):
        try:
            with open(path, 'r') as f:
                if 'packet_recvmsg' in f.read():
                    m = PID_PATTERN.search(path)
                    if m:
                        pids.add(m.group(1))
        except (IOError, PermissionError):
            continue
    return pids


def ps_grep(pid):
    # ps -ef | grep <pid>
    cmd = f"ps -ef | grep {pid}"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
    return result.stdout.strip().splitlines()


def main():
    # 데몬 시작 메시지 출력
    print("All for One , One for ALL")
    print("Black Falcon")
    print("Starting packet_recvmsg watcher (press Ctrl-C to stop)")

    while True:
        # 5초마다 시간 출력 (위아래 빈 줄 포함)
        print()
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print()

        pids = find_packet_recvmsg_pids()
        if pids:
            with open(OUTPUT_FILE, 'w') as out:
                for pid in sorted(pids):
                    lines = ps_grep(pid)
                    for line in lines:
                        print(line)
                        out.write(line + "\n")
        time.sleep(5)


if __name__ == "__main__":
    main()
