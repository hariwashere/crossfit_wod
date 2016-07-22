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


def main():
    page = requests.get(BASE_URL)
    tree = html.fromstring(page.content)
    exercise_doms = tree.find_class('col-sm-6')

    # Weed out matches for the entire exercise section
    exercise_doms = filter(lambda exercise: len(exercise.classes) == 1, exercise_doms)
    exercise_text = map(get_exercise_text, exercise_doms)
    exercise_text = filter(is_wod_significant, exercise_text)

    wod_to_equipment = []

    for wod in exercise_text:
        equipment = get_equipments_for_wod(wod)
        wod_to_equipment.append({'wod': wod, 'equipment': equipment})

    with open('exercises', 'w') as op_file:
        op_file.writelines(
            [repr(line) for line in wod_to_equipment]
        )
    return


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


if __name__ == "__main__":
    main()
