from lxml import html
import requests
import re

MOVEMENT_TO_REGEX = {
    'dead lift': 'dead[ -]?lifts?'
}


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


def get_movements_with_equipment(exercise_text):
    matched_movements = []
    for movement, movement_regex in MOVEMENT_TO_REGEX.iteritems():
        if re.search(movement_regex, exercise_text):
            matched_movements.append(movement)
    return matched_movements
