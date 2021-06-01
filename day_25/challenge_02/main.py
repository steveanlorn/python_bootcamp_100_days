# Create new data frame contains:
# Fur Color, Count

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# primary_fur_color = data.groupby('Primary Fur Color')['Primary Fur Color'].count()
# primary_fur_color = data['Primary Fur Color'].value_counts()
primary_fur_color = data.groupby('Primary Fur Color').size()

# fur = []
# count = []
# for item in primary_fur_color.iteritems():
#     fur.append(item[0])
#     count.append(item[1])
#
# new_data_frame = {
#     "fur": fur,
#     "count": count,
# }

new_data_frame = {
    "fur": primary_fur_color.index.tolist(),
    "count": primary_fur_color.tolist(),
}

primary_fur_color_df = pandas.DataFrame(new_data_frame)
primary_fur_color_df.to_csv("primary_fur_color.csv")
