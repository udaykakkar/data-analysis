import pandas as pd

csv_file = pd.DataFrame(pd.read_csv("noc-cnp.csv", sep = ",", header = 0, index_col = False))
print()	
csv_file.to_json("noc1.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)