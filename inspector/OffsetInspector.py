from inspector import Code
from inspector.DBConnect import DBConnect
from inspector.SentenceGroup import SentenceGroup
from inspector.ExcelWriter import ExcelWriter


class OffsetInspector:
    def __init__(self):
        self.sample_id = 0
        self.sample_type = ''
        self.sample_type_code = 0
        self.annotation_data = None
        self.error_groups = []
        self.did_it_work = True

    def inspect_and_get_error_groups(self):
        self.get_data_from_db()
        self.inspect_by_type()
        return self.error_groups

    def get_data_from_db(self):
        self.sample_id = input(">> 표본 번호 = ")
        db = DBConnect(self.sample_id)
        self.sample_type = db.get_sample_type()
        self.annotation_data = db.get_annotations_data()
        if self.sample_type == '문어':
            print(">> 문어는 아직 못 만들었습니다.")
            self.did_it_work = False
            return
        elif self.sample_type == '구어':
            self.sample_type_code = Code.SPEECH_TYPE
        print("{} 타입의 샘플 {}을 검사합니다.".format(self.sample_type, self.sample_id))

    def inspect_by_type(self):
        data_list = self.get_data_by_type(self.sample_type_code)
        sentence_groups = self.get_sentence_groups(data_list)
        for group in sentence_groups:
            group.inspect_sentence()
            group.inspect_words()
            if len(group.error_words) >= 1:
                self.error_groups.append(group)

    def get_data_by_type(self, a_type):
        data_list = []
        for data in self.annotation_data:
            if data[Code.A_TYPE_INDEX] == a_type:
                data_list.append(data)
        return data_list

    # noinspection PyMethodMayBeStatic
    def get_sentence_groups(self, data_list):
        sentence_groups = []
        sentence_group = SentenceGroup()
        previous_data = None
        for data in data_list:
            if self.is_the_end_of_the_sentence_group(previous_data, data):
                sentence_groups.append(sentence_group)
                sentence_group = SentenceGroup()
            sentence_group.set_data(data)
            previous_data = data
        return sentence_groups

    # noinspection PyMethodMayBeStatic
    def is_the_end_of_the_sentence_group(self, previous_data, data):
        if previous_data is None:
            return False
        elif previous_data[Code.T_VALUE_INDEX] not in Code.START_SENTENCE_GROUP and data[Code.T_VALUE_INDEX] in Code.START_SENTENCE_GROUP:
            return True
        else:
            return False
