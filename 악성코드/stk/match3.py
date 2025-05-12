#
# write by SpeeDr00t
# 

find_hex_patterns = []
find_string_patterns = []

def SetFindHex(hex_string: str):
    """검색할 hex 패턴 등록 (공백 없는 16진수 문자열)"""
    try:
        b = bytes.fromhex(hex_string)
        find_hex_patterns.append((hex_string, b))
    except ValueError:
        print(f"❌ 잘못된 hex 문자열: {hex_string}")

def SetFindString(text: str):
    """검색할 일반 문자열 등록"""
    find_string_patterns.append(text.encode())

def SearchInELF(file_path: str, context_byte_count: int = 60):
    with open(file_path, "rb") as f:
        data = f.read()

    print(f"\n🔍 Searching in {file_path}...\n")

    # HEX 검색
    for hex_str, bpattern in find_hex_patterns:
        offsets = []
        offset = data.find(bpattern)
        while offset != -1:
            offsets.append(offset)
            offset = data.find(bpattern, offset + 1)

        if offsets:
            print(f"✅ Found HEX [{hex_str}] at:")
            for off in offsets:
                print(f"  - Offset 0x{off:08x}")
                segment = data[off:off + context_byte_count]
                hex_dump = ' '.join(f"{b:02x}" for b in segment)
                ascii_view = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in segment)
                print(f"    ↳ Hex:   {hex_dump}")
                print(f"    ↳ ASCII: {ascii_view}")
        else:
            print(f"❌ HEX [{hex_str}] not found.")

    # STRING 검색
    for spattern in find_string_patterns:
        try:
            stext = spattern.decode()
        except:
            stext = str(spattern)
        offsets = []
        offset = data.find(spattern)
        while offset != -1:
            offsets.append(offset)
            offset = data.find(spattern, offset + 1)

        if offsets:
            print(f"✅ Found STRING ['{stext}'] at:")
            for off in offsets:
                print(f"  - Offset 0x{off:08x}")
                segment = data[off:off + context_byte_count]
                hex_dump = ' '.join(f"{b:02x}" for b in segment)
                ascii_view = ''.join(chr(b) if 32 <= b <= 126 else '.' for b in segment)
                print(f"    ↳ Hex:   {hex_dump}")
                print(f"    ↳ ASCII: {ascii_view}")
        else:
            print(f"❌ STRING ['{stext}'] not found.")

# ✅ 예시 사용
if __name__ == "__main__":

    SetFindHex("2f62696e2f726d202d66")
    SetFindString("/bin/rm -f")

    SetFindHex("2f6465762f73686d")
    SetFindString("/dev/shm")

    SetFindHex("2f62696e2f63686d6f6420373535")
    SetFindString("/bin/chmod 755")

    SetFindHex("2f62696e2f69707461626c6573")
    SetFindString("/bin/iptables")

    SetFindHex("2f7573722f6c6962657865632f706f73746669782f6d6173746572")
    SetFindString("/usr/libexec/postfix/master")

    SetFindHex("2f7362696e2f69707461626c6573202d74206e6174202d4120505245524f5554494e4720")
    SetFindString("/sbin/iptables -t nat -A PREROUTING ")

    SetFindHex("2f7362696e2f69707461626c6573202d74206e6174202d4420505245524f5554494e47202d7020746370")
    SetFindString("/sbin/iptables -t nat -D PREROUTING -p tcp")

    SetFindHex("2f7362696e2f69707461626c6573202d4920494e505554202d7020746370")
    SetFindString("/sbin/iptables -I INPUT -p tcp")

    SetFindHex("2f7362696e2f69707461626c6573202d4420494e505554")
    SetFindString("/sbin/iptables -D INPUT")


    SetFindHex("65786563")
    SetFindString("exec")


    SetFindHex("7368656c6c")
    SetFindString("shell")


    SetFindHex("73797374656d2822")
    SetFindString("system(\"")


    SetFindHex("716d6772202d6c202d74206669666f202d75")
    SetFindString("qmgr -l -t fifo -u")

    SetFindHex("484f4d453d2f746d70")
    SetFindString("HOME=/tmp")


    SetFindHex("5053313d5b5c755c40485c20575d5c5c2420")
    SetFindString("PS1=[\\u@\\h \\W]\\$ ")

    SetFindHex("4d5953514c5f4849535446494c453d2f6465762f6e756c6c")
    SetFindString("MYSQL_HISTFILE=/dev/null")

    SetFindHex("2f7362696e2f7564657664202d64")
    SetFindString("/sbin/udevd -d")


    SetFindHex("2f7362696e2f6d696e6765747479202f6465762f74747937")
    SetFindString("/sbin/mingetty /dev/tty7")

    SetFindHex("2f7573722f7362696e2f636f6e736f6c652d6b69742d6461656d6f6e202d2d6e6f2d6461656d6f6e22")
    SetFindString("/usr/sbin/console-kit-daemon --no-daemon\"")


    SetFindHex("68616c642d6164646f6e2d616370693a206c697374656e696e67206f6e2061637069206b65726e656c20696e74657266616365202f70726f632f616370692f6576656e74")
    SetFindString("hald-addon-acpi: listening on acpi kernel interface /proc/acpi/event")


    SetFindHex("646275732d6461656d6f6e202d2d73797374656d")
    SetFindString("dbus-daemon --system")


    SetFindHex("68616c642d72756e6e6572")
    SetFindString("hald-runner")


    SetFindHex("7069636b7570202d6c202d74206669666f202d75")
    SetFindString("pickup -l -t fifo -u")


    SetFindHex("61766168692d6461656d6f6e3a206368726f6f742068656c706572")
    SetFindString("avahi-daemon: chroot helper")


    SetFindHex("2f7362696e2f617564697464202d6e")
    SetFindString("/sbin/auditd -n")


    SetFindHex("2f7573722f6c69622f73797374656d642f73797374656d642d6a6f75726e616c64")
    SetFindString("/usr/lib/systemd/systemd-journald")


    SearchInELF("malware_file")



