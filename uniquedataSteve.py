#  1. Create a new collection that contains the  unique color names in the list below

# 2. Create a new collection that stores the unique   color names AND how many times each one is in the list

eye_colors = [
    {
        "color": "brown"
    },
    {
        "color": "green"
    },
    {
        "color": "amber"
    },
    {
        "color": "blue"
    },
    {
        "color": "amber"
    },
    {
        "color": "amber"
    },
    {
        "color": "brown"
    },
    {
        "color": "amber"
    },
    {
        "color": "brown"
    },
    {
        "color": "brown"
    },
    {
        "color": "purple"
    },
    {
        "color": "purple"
    },
    {
        "color": "blue"
    },
    {
        "color": "blue"
    },
    {
        "color": "brown"
    },
    {
        "color": "amber"
    },
    {
        "color": "amber"
    },
    {
        "color": "green"
    },
    {
        "color": "green"
    },
    {
        "color": "green"
    },
    {
        "color": "brown"
    },
    {
        "color": "amber"
    },
    {
        "color": "brown"
    },
    {
        "color": "amber"
    },
    {
        "color": "blue"
    },
    {
        "color": "blue"
    },
    {
        "color": "green"
    },
    {
        "color": "green"
    }
]

#  1. Create a new collection that contains the  unique color names in the list above

# --Answers to Section 1 From Here----------
# unique_colors = set()

# for color_dict in eye_colors:
#     current_color = color_dict["color"]
#     unique_colors.add(current_color)

# print(unique_colors)
# --Answers to Section 1 To Here----------


# 2. Create a new collection that stores the unique   color names AND how many times each one is in the list

# --Answer to Section 2---->

color_table = {}

for each_color_dict in eye_colors:
    this_color = each_color_dict["color"]

    if this_color not in color_table:
        color_table[this_color] = 1
    else:
        color_table[this_color] += 1

print(color_table)
