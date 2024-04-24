import json
import os.path
from collections import defaultdict

import pandas as pd
from docx import Document

from params import all_fields


class TableExtractor:

    def __init__(self):
        self.data_format = json.load(open("config.json", "r"))
        self.all_fields = all_fields.split(',')

    def get_keys(self):
        return self.all_fields

    def convert_dict(self, input_dic: dict):
        converted_dict = defaultdict(lambda: "N/A")
        for _key, _value in input_dic.items():
            converted_dict[_key] = _value

        # Full name
        # full_name = input_dic["Name"]
        # name_split = full_name.split()
        # if len(name_split) >= 4:
        #     converted_dict["Title"] = name_split[0]
        #     converted_dict["First Name"] = name_split[1]
        #     converted_dict["Middle Name"] = " ".join(name_split[2:-1])
        #     converted_dict["Last Name"] = name_split[-1]
        # if len(name_split) == 3:
        #     converted_dict["First Name"] = name_split[0]
        #     converted_dict["Middle Name"] = name_split[1]
        #     converted_dict["Last Name"] = name_split[2]
        # elif len(name_split) == 2:
        #     converted_dict["First Name"] = name_split[0]
        #     converted_dict["Last Name"] = name_split[1]
        # elif len(name_split) == 1:
        #     converted_dict["First Name"] = name_split[0]

        converted_dict["Casual Name"] = input_dic["First Name"]
        converted_dict["Name"] = input_dic["First Name"] + " " + input_dic["Last Name"]
        # Account Numbers
        converted_dict["EFT BSB Number"] = input_dic["bsb"]
        converted_dict["EFT Account Name"] = input_dic["account_name"]
        converted_dict["EFT Account Number"] = input_dic["account_number"]
        converted_dict["Industry Code"] = input_dic["business_type"]

        return converted_dict

    def get_table_info(self, filename):
        doc = Document(filename)
        tables = []
        for table in doc.tables:
            table_data = []
            for row in table.rows:
                row_data = []
                for cell in row.cells:
                    row_data.append(cell.text)
                table_data.append(row_data)
            tables.append(table_data)
        return tables

    def extract_data_from_table(self, table_info_list: list):
        data = defaultdict(lambda: "N/A")
        table_id = 0
        for _key, _value in self.data_format.items():
            if not len(table_info_list) > 0:
                return {}
            for row in table_info_list[table_id]:
                _content = "N/A"
                try:
                    if _value[0] in row[_value[1]]:
                        _content = row[_value[2]]
                        if _value[1] == _value[2]:
                            _content = _content.split(_value[0])[1].strip()
                        break
                finally:
                    data[_key] = _content
        return data

    def convert_to_csv(self, file_path):
        table_info = self.get_table_info(file_path)
        data = self.extract_data_from_table(table_info)
        df = pd.DataFrame(list(data.items()), columns=["Item", "Value"])
        new_filepath = file_path.replace("docx", "csv")
        df.to_csv(new_filepath)
        return os.path.basename(new_filepath)

    def get_dict(self, file_path):
        table_info = self.get_table_info(file_path)
        data = self.extract_data_from_table(table_info)
        return data


def main():
    tb = TableExtractor()
    table_info = tb.get_table_info('app_uploaded_files/IndividualTaxReturn-FactFind-2022-dulanj.docx')
    data = tb.extract_data_from_table(table_info)
    df = pd.DataFrame(list(data.items()), columns=["Item", "Value"])
    print(df.head(10))


def content_main():
    tb = TableExtractor()
    _file_path = '/home/dulanj/SB/test_docs/IndividualTaxReturn-FactFind-2022-dulanj.docx'
    content = open(_file_path, "rb")
    table_info = tb.get_table_info(content)
    data = tb.extract_data_from_table(table_info)
    new_data = {k: [v] for k, v in data.items()}
    df = pd.DataFrame(new_data)
    for row in df.iterrows():
        print(row)
    print(df.head(10))


if __name__ == '__main__':
    content_main()
