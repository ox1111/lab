
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

