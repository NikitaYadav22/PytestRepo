import json
import pandas


excel_data_df = pandas.read_excel('tes_excel.xlsx', sheet_name='Sheet1')
mylist = excel_data_df['PLU'].tolist()
print(mylist)
# json_str = excel_data_df.to_json()
# json_str = json.loads(json_str)
# print('Excel Sheet to JSON:\n', json_str)
# file_data={}
# for str in json_str["PLU"]:
#     file_data[json_str["PLU"][str]]=False
# print('Excel Sheet to JSON:\n', file_data)

# with open('file.json', 'w') as f:
#     f.write(json.dumps(file_data))