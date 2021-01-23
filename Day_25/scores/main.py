import pandas

data_dict = {
    "students": ["Amy", "James", "Kris"],
    "score": [78, 43, 67]
}

data = pandas.DataFrame(data_dict)
data.to_csv("scores.csv")
