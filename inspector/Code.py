# tbl_annotations_data 테이블 컬럼 인덱스
OFFSET_START_INDEX = 2
OFFSET_END_INDEX = 3
A_TYPE_INDEX = 5
S_VALUE_INDEX = 8
T_VALUE_INDEX = 9

# 엑셀 파일에 출력할 시트 명
SHEET_ERROR = "오프셋 오류가 있는 문장 및 어절"
# 엑셀 파일에 출력할 컬럼 명
EXCEL_COLUMN_SPEECH = ["T_VALUE", "S_VALUE", "OFFSET_START", "OFFSET_END", "S_VALUE_WITH_OFFSET"]

# a_Type 코드
SPEECH_TYPE = 2
WRITE_TYPE = 1

# 코드에 사용할 컬럼 이름을 상수화
PERSON_ID = "PERSON_ID"
SENTENCE = "SENTENCE"
SPEECH_TIME = "SPEECH_TIME"
START_SENTENCE_GROUP = ["PERSON_ID", "SENTENCE", "SPEECH_TIME"]

# 원문 형태소를 그대로 s_value에 가져오지 않는 t_value ()
NOT_WORD = ("ERROR_CERTAINTY", "PAUSE_SHORT", "VOCAL", "PAUSE_LONG", "FOREIGN_LANG_DIFF", "UNCERTAIN_COUNT",
            "ERROR_RULES", "ERROR_UNCERTAINTY", "PERSON_ID", "SPEECH_TIME", "PRONOUNCE_VARIATION", "EVENT")

OFFSET_ADD_FOR_SPEECH_SENTENCE = 2