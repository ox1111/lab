#
# write by kyoung chip ,jang
# ida 8.3
#
'''
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

'''
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
    print("\n\n\n\nFunction Name\tRelative Address")
    print("------------------------------------")
    
    for func_name, func_offset in get_function_info():
        print(f"{func_name},0x{func_offset:X}")

if __name__ == "__main__":
    main()
