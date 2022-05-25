from inspector.OffsetInspector import OffsetInspector
from inspector.ExcelWriter import ExcelWriter
from concat.DataMaker import DataMaker
from concat.DBConnect import DBConnect

if __name__ == "__main__":
    while True:
        switch = input(">> 오프셋을 검사하려면 1, 끝내려면 2를 입력하세요. = ")
        if switch == '1':
            offset_inspector = OffsetInspector()
            error_groups = offset_inspector.inspect_and_get_error_groups()
        else:
            print(">> 종료합니다.")
            break

        if offset_inspector.did_it_work:
            excel_writer = ExcelWriter(offset_inspector.sample_id)
            excel_writer.get_offset_inspect_result(error_groups)
