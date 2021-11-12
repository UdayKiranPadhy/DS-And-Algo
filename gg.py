import pandas as pd
import random
d = {}
for i in range(1, 67):
    question_no = set()
    while len(question_no) != 3:
        question_no.add(random.randint(1, 20))
    reg_num = "18B91A04" + str(i).rjust(2, "0")
    d[reg_num] = list(question_no)

df = pd.DataFrame(d)
df = df.transpose(copy=True)
df.reset_index(inplace=True)
df.columns = ["Reg Number", "Q1", "Q2", "Q3"]
writer = pd.ExcelWriter("GG.xlsx")
df.to_excel(writer, "Random Questions")
writer.save()