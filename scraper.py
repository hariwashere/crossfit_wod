from lxml import html
import requests

BASE_URL = 'https://www.crossfit.com/workout'
page = requests.get(BASE_URL)
tree = html.fromstring(page.content)
exercise_doms = tree.find_class('col-sm-6')

with open('exercises', 'w') as op_file:
    for exercise in exercise_doms:
        # Weed out matches for the entire exercise section
        if len(exercise.classes) == 1:
            op_file.write(
                unicode(exercise.text_content()).encode('utf-8')
            )
