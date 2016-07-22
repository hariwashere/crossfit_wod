import re
import requests
import simplejson

from lxml import html
import M2E


BASE_URL = 'https://www.crossfit.com/workout'

def test():
    wods = master()

    for i in range(3):
        wod_entity = wods[i]

        db_wod = WOD(
            wod=wod_entity['wod']
        )

        for equipment in wod_entity.equipment:
            if equipment == 'GHD machine':
                db_wod.ghd = True


def main():
    exercise_text = []
    for page_number in range(1, 11):
        print "Getting page " + str(page_number)
        url = BASE_URL + 'page={page}'.format(page=page_number)
        exercise_text.extend(
            get_wods_for_url(url)
        )
    wod_to_equipment = []

    for wod in exercise_text:
        equipment = list(set(get_equipments_for_wod(wod)))
        wod_to_equipment.append({'wod': wod, 'equipment': equipment})

    with open('exercises', 'w') as op_file:
        op_file.write(simplejson.dumps(wod_to_equipment))


def get_wods_for_url(url):
    page = requests.get(BASE_URL)
    tree = html.fromstring(page.content)
    exercise_doms = tree.find_class('col-sm-6')

    # Weed out matches for the entire exercise section
    exercise_doms = filter(lambda exercise: len(exercise.classes) == 1, exercise_doms)
    exercise_text = map(get_exercise_text, exercise_doms)
    return filter(is_wod_significant, exercise_text)

def get_equipments_for_wod(exercise_text):
    equipments_needed = []
    for movement, movement_regex in M2E.MOVEMENT_TO_REGEX.iteritems():
        if re.search(movement_regex, exercise_text.lower()):
            if (M2E.MOVEMENT_TO_EQUIPMENT.get(movement)):
                equipments_needed.append(
                    M2E.MOVEMENT_TO_EQUIPMENT.get(movement)
                )
    return equipments_needed


def get_exercise_text(exercise_dom):
    exercise_string = unicode(exercise_dom.text_content()).encode('utf-8')
    return exercise_string[:exercise_string.find("Post")]


def is_wod_significant(wod):
    return not(len(wod) < 10 or wod.startswith('Rest Day'))


def load_wod_from_file():
    with open('exercises', 'r') as wod_file:
        return simplejson.loads(wod_file.read())


def get_wod_for_equipments(equipments):
    wod_dict = load_wod_from_file()
    equipments_had = set(equipments)
    selected_wods = []
    for wod in wod_dict:
        equipments_needed = set(wod['equipment'])
        if equipments_needed <= equipments_had:
            selected_wods.append(wod['wod'])
        if len(selected_wods) == 3:
            return selected_wods
    return selected_wods


if __name__ == "__main__":
    # main()
    print get_wod_for_equipments(['barbell', 'wall ball', 'jump rope', 'box', 'pull up bar', 'running space'])
