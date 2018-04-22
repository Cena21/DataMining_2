# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv('Building_Permits.csv', low_memory=False)

rule = ['Permit Type','Street Number','Estimated Cost', 'Proposed Use', 'Existing Construction Type']

rule_label = []

for column in rule:
    column =  column.replace(' ','_')
    rule_label.append(column)
data = df[rule]
trans_dict = {}
record_num = data.index.__len__()
for column in rule:
    new_line = [""]*record_num
    for index in data.index:
        item = data[column][index]
        try:
            if np.isnan(item):
                new_line[index] = ""
            else:
                new_line[index] = rule_label[rule.index(column)] + ":"+ str(item).replace(' ','_')
        except BaseException as e:
            new_line[index] = rule_label[rule.index(column)] + ":" + str(item).replace(' ','_')
    trans_dict[column] = new_line

csv_write = pd.DataFrame(trans_dict)
csv_write.to_csv('Pre_data.csv', index=False, header=False)