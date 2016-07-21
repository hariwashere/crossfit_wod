from lxml import html
import requests


def get_exercise_text(exercise_dom):
    exercise_string = unicode(exercise_dom.text_content()).encode('utf-8')
    return exercise_string[:exercise_string.find("Post")]


BASE_URL = 'https://www.crossfit.com/workout'
page = requests.get(BASE_URL)
tree = html.fromstring(page.content)
exercise_doms = tree.find_class('col-sm-6')

# Weed out matches for the entire exercise section
exercise_doms = filter(lambda exercise: len(exercise.classes) == 1, exercise_doms)

exercise_text = map(get_exercise_text, exercise_doms)

with open('exercises', 'w') as op_file:
    op_file.writelines(exercise_text)
