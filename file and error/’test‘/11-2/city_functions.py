#对city_functions.py的函数进行小型改进

def get_title_county(county,city,population = ''):
    if population:
        total_name = f"{city}，{county} - {population} 5000"
        return total_name.title()
    else:
        total_name = f"{city}，{county} - 5000"
        return total_name.title()