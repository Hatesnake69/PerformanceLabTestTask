import json


def report_maker(report_dict: dict, values_dict: dict):
    if 'id' in report_dict:
        for id_dict in values_dict['values']:
            if id_dict['id'] == report_dict['id']:
                report_dict['value'] = id_dict['value']
                values_dict['values'].remove(id_dict)
    for key, value in report_dict.items():
        if isinstance(value, list):
            for i_dict in value:
                report_maker(i_dict, values_dict)


with open('report.json', 'w+') as report_file:
    with open('tests.json', 'r') as test_file:
        data_test = json.load(test_file)
        with open('values.json', 'r') as values_file:
            data_values = json.load(values_file)
            report_maker(data_test, data_values)
    json.dump(data_test, report_file, indent=6, ensure_ascii=False)