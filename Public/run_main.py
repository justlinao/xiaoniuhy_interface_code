# coding=UTF-8
from Public.readexcel import ReadExcel


class RunMain:
    def run_case(self):
        """

        :return:
        """
        rows = ReadExcel.get_rows()
        for i in range(rows):
            data = ReadExcel.get_row_value(i+2)  # i从0开始，case是从第二行写的
            print(data)


run = RunMain()
run.run_case()
