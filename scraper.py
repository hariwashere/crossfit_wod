from lxml import html
import requests
import re
import M2E


BASE_URL = 'https://www.crossfit.com/workout'

def test():
    import ipdb; ipdb.set_trace()
    wods = master()

    for i in range(3):
        wod_entity = wods[i]

        db_wod = WOD(
            wod=wod_entity['wod']
        )

        for equipment in wod_entity.equipment:
            if equipment == 'GHD machine':
                db_wod.ghd = True


def master():
    page = requests.get(BASE_URL)
    tree = html.fromstring(page.content)
    exercise_doms = tree.find_class('col-sm-6')
    
    # Weed out matches for the entire exercise section
    exercise_doms = filter(lambda exercise: len(exercise.classes) == 1, exercise_doms)
    exercise_text = map(get_exercise_text, exercise_doms)

    with open('exercises', 'w') as op_file:
        op_file.writelines(exercise_text)

    wod_to_equipment = []

    for wod in exercise_text:
        if len(wod) < 10 or wod.startswith('Rest Day'):
            continue
        else:
            equipment = convert_wod_to_equipment(wod)

        wod_to_equipment.append({'wod': wod, 'equipment': equipment})

    return wod_to_equipment


def convert_wod_to_equipment(wod):
    movements = get_movements_with_equipment(wod)
    movements = [m.lower() for m in movements]

    equipment = []

    for key, value in M2E.MOVEMENT_TO_EQUIPMENT.iteritems():
        if key.lower() in movements:
            if value != "none":
                equipment.append(value)

    return list(set(equipment))


def get_movements_with_equipment(exercise_text):
    matched_movements = []
    for movement, movement_regex in M2E.MOVEMENT_TO_REGEX.iteritems():
        if re.search(movement_regex, exercise_text.lower()):
            matched_movements.append(movement)

    return matched_movements


def get_exercise_text(exercise_dom):
    exercise_string = unicode(exercise_dom.text_content()).encode('utf-8')
    return exercise_string[:exercise_string.find("Post")]

