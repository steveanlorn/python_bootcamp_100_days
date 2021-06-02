# Dictionary Comprehension
# {new_key:new_value for item in list}
# {new_key:new_value for (key,value) in dict.items()}
# {new_key:new_value for (key,value) in dict.items() if condition}

# Swapping value and key data
dic2 = {1: "Monday", 2: "Tuesday"}
new_dic2 = {value: key for (key, value) in dic2.items()}
print(new_dic2)

# Calculate number of letter in each word of a sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
list_of_words = sentence.split(" ")
dic_of_words = {word: len(word) for word in list_of_words}
print(dic_of_words)

# Convert weather from Celsius to Fahrenheit.
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def c_to_f(temp_c):
    return (temp_c * 9 / 5) + 32


weather_f = {day: c_to_f(temp) for (day, temp) in weather_c.items()}
print(weather_f)
