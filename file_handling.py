
import json




def speech_reader(speaker: str, file_name: str):
    with open (file_name) as f:
        content = f.read()

    speech_words = content.split()
    speech_lines = content.splitlines()   

    print(f'{speaker}\'s Total number of words: {len(speech_words)}')   
    print(f'{speaker}\'s Total number of lines: {len(speech_lines)}\n')  

# Read obama_speech.txt file and count number of lines and words
speech_reader('Obama','C:/Users/austi/Documents/GitHub/30daysofPython/files/obama_speech.txt')

# Read michelle_obama_speech.txt file and count number of lines and words
speech_reader('Michelle','C:/Users/austi/Documents/GitHub/30daysofPython/files/michelle_obama_speech.txt')

# Read donald_speech.txt file and count number of lines and words
speech_reader('Trump','C:/Users/austi/Documents/GitHub/30daysofPython/files/donald_speech.txt')

# Read melina_trump_speech.txt file and count number of lines and words
speech_reader('Melina', 'C:/Users/austi/Documents/GitHub/30daysofPython/files/melina_trump_speech.txt')


   
# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_language_json(file: str, country_num: int):
    language_list  = {} 

    with open(file, 'r', encoding='utf-8') as f:
        country_content = json.load(f)

    for country in country_content:
        languages = country.get('languages', [])

        for lang in languages:
            if lang in language_list:
                language_list[lang] += 1
            else:
                language_list[lang] = 1

    sorted_languages = sorted(language_list.items(), key=lambda x: x[1], reverse=True)
    
    for lang, count in sorted_languages[:country_num]:
        print(f'{lang}: {count}' )


# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
def most_populated_countries_json(file: str, country_num: int):
    population_list = []

    with open(file, 'r', encoding='utf-8') as f:
        country_content = json.load(f)

    for country in country_content:
        country_name  = country.get('name')
        population_size = country.get('population')

        population_list.append((country_name, population_size))


    sorted_population =  sorted(population_list, key=lambda x: x[1], reverse=True)    

    print('')
    for country, pop in sorted_population[:country_num]:
        print(f'Country: {country} , Population: {pop}' )

most_spoken_language_json('C:/Users/austi/Documents/GitHub/30daysofPython/files/countries_data.json', 10)    
most_populated_countries_json('C:/Users/austi/Documents/GitHub/30daysofPython/files/countries_data.json', 10)
