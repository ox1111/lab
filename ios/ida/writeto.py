#
# write by kyoung chip ,jang
# ida 8.3
#
'''
funcaddr.txt
_get_thread_identifier_info,0x50C0
_get_proc_threadinfo,0x5110
-[X61WYG_IRD7 sessionId],0x5148
-[X61WYG_IRD7 sessionToken],0x5150
-[X61WYG_IRD7 getCachedSystemIdentifier],0x51A0
_vm_region_recurse_64,0x1C920
_vsscanf,0x1C92C
_write,0x1C938

addr.txt
const funcInfo = [
    { name: "_get_thread_identifier_info", offset: 0x50C0 },
    { name: "_get_proc_threadinfo", offset: 0x5110 },
    { name: "-[X61WYG_IRD7 sessionId]", offset: 0x5148 },
    { name: "-[X61WYG_IRD7 sessionToken]", offset: 0x5150 },
    { name: "-[X61WYG_IRD7 getCachedSystemIdentifier]", offset: 0x51A0 },
    { name: "_vm_region_recurse_64", offset: 0x1C920 },
    { name: "_vsscanf", offset: 0x1C92C },
    { name: "_write", offset: 0x1C938 },
];


# 파일 이름
input_filename = "funaddr.txt"
output_filename = "addr.txt"

# 입력 파일 읽기
with open(input_filename, "r") as f:
    lines = f.readlines()

# 함수 정보 파싱
parsed_info = []
for line in lines:
    # 콤마로 분리하여 함수 이름과 오프셋 추출
    name, offset = line.strip().split(",")
    # 함수 이름과 오프셋을 JavaScript 객체 형식으로 변환하여 추가
    parsed_info.append(f'{{ name: "{name.strip()}", offset: {offset.strip()} }}')

# 출력 파일 작성
with open(output_filename, "w") as f:
    # JavaScript 배열 형식으로 출력
    f.write("const funcInfo = [\n")
    for info in parsed_info:
        f.write("    " + info + ",\n")
    f.write("];\n")

print(f"Parsing completed. Result saved in {output_filename}")

