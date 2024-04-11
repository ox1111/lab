#
# write by kyoung chip ,jang
# ida 8.3
#
import sys
import idaapi
import idc
import idautils

def get_function_info():
    function_info = []
    
    # 모든 세그먼트 반복
    for seg_ea in idautils.Segments():
        # 세그먼트 내의 모든 함수 반복
        for func_ea in idautils.Functions(seg_ea, idc.get_segm_end(seg_ea)):
            func_name = idc.get_func_name(func_ea)
            func_offset = func_ea - idaapi.get_imagebase()
            
            function_info.append((func_name, func_offset))
    
    return function_info

def main():
    print("Function Name\tRelative Address")
    print("------------------------------------")
    
    for func_name, func_offset in get_function_info():
        print(f"{func_name}\t0x{func_offset:X}")

if __name__ == "__main__":
    main()
    
    for func_name, func_offset in get_function_info():
        print(f"{func_name}\t0x{func_offset:X}")

if __name__ == "__main__":
    main()
