#编写一个函数，他接受两个形参：一个城市名和一个国家名。这个函数返回一个格式为City，County的字符串，如Santiago，Chile。
#将这个函数存储在在一个名为city_functions.py的模块中。

def get_title_county(county,city):
    total_name = f"{city} {county}"
    return total_name.title()