MOVEMENT_TO_REGEX = {
    'deadlift': 'dead[ -]?lifts?',
    'GHD sit-up': 'GHD[ -]?sit[ -]?ups?',
    'double-under': 'double[ -]?unders?',
    'rope climb': 'rope[ -]?climbs?',
    'wall-ball shot': 'wall[ -]?ball[ ]?shots?',
    'box jump': 'box[ -]?jumps?',
    'triple-under': 'triple[ -]?unders?',
    'power clean': 'power[ -]?cleans?',
    'squat clean and jerk': 'squat[ -]?clean[ -]?and[ -]?jerks?',
    'medicine ball clean ': 'medicine[ -]?ball[ -]?cleans?',
    'handstand walking': 'handstand[ -]?walk(ing)?s?',
    'sit-up': 'sit[ -]?ups?',
    'row': 'rows?',
    'knees-to-elbow ': 'knees[ -]?to[ -]?elbows?',
    'handstand walk ': 'handstand[ -]?walks?',
    'barbell turkish get-up': 'barbell[ -]?(T|t)urkish[ -]?get[ -]?ups?',
    'pull-up': 'pull[ -]?ups?',
    'hang power clean': 'hang[ -]?power[ -]?cleans?',
    'bike': 'bikes?',
    'squat clean': 'squat[ -]?cleans?',
    'step-up': 'step[ -]?ups?',
    'hang squat snatch': 'hang[ -]?squat[ -]?snatch(es)?',
    'swim': 'swims?',
    'thruster': 'thursters?',
    'hip extension': 'hip[ -]?extensions?',
    'snatch': 'snatch("es")?',
    'farmers carry': 'farmers carrys?',
    'kettlebell snatch': 'kettlebell[ -]?snatch(es)?',
    'handstand push-up': 'handstand[ -]?push[ -]?ups?',
    'hang squat clean ': 'hang[ -]?squat[ -]?cleans?',
    'turkish get-up': '(T|t)urkish[ -]?get[ -]?ups?',
    'burpee': 'burpees?',
    'toes-to-bar': 'toes[ -]?to[ -]?bars?',
    'weighted lunge': 'weighted[ -]?lunges?',
    'dumbbell squat clean': 'dumbbell[ -]?squat[ -]?cleans?',
    'push jerk': 'push[ -]?jerks?',
    'muscle-up': 'muscle[ -]?ups?',
    'sumo deadlift high pull': 'sumo[ -]?deadlift[ -]?high[ -]?pulls?',
    'power snatch': 'power[ -]?snatch(es)?',
    'sprint': 'sprints?',
    'squat': 'squats?',
    'legless rope climb': 'legless[ -]?rope[ -]?climbs?',
    'shoulder press': 'shoulder[ -]?press(es)?',
    'chest-to-bar pull-up': 'chest[ -]?to[ -]?bar[ -]?pull[ -]?ups?',
    'strict pull-up': 'strict[ -]?pull[ -]?ups?',
    'run': 'runs?',
    'burpee box jump over': 'burpee[ -]?box[ -]?jump[ -]?overs?',
    'clean and jerk': 'clean[ -]?and[ -]?jerks?',
    'one-legged squat': 'one[ -]?legged[ -]?squats?',
    'push-up': 'push[ -]?ups?',
    'back squat': 'back[ -]?squats?',
    'single-arm dumbbell overhead lunge ': 'single[ -]?arm[ -]?dumbell[ -]?overhead[ -]?lunges?',
    'kettlebell swing': 'kettlebell[ -]?swings?',
    'ring dip': 'ring[ -]?dips?',
    'burpee bar muscle-up': 'burpee[ -]?bar[ -]?muscle[ -]?ups?',
    'front squat': 'front[ -]?squats?',
    'L pull-up': '(L|l)[ -]?pull[ -]?ups?',
    'bench press': 'bench[ -]?press(es)?',
    'push press': 'push[ -]?press(es)?',
    'cleans': 'cleans?',
    'dumbbell squat snatch': 'dumbbell[ -]?squat[ -]?snatch(es)?',
    'overhead squat': 'overhead[ -]?squats?'
}





MOVEMENT_TO_EQUIPMENT = {
    'ghd sit-up': 'GHD machine',
    'l pull-up': 'pull up bar',
    'turkish get-up': 'kettlebell',
    'back squat': 'barbell',
    'barbell turkish get-up': 'barbell',
    'bench press': 'barbell',
    'bike': 'bike',
    'box jump': 'box',
    'burpee': 'none',
    'burpee bar muscle-up': 'barbell',
    'burpee box jump over': 'box',
    'chest-to-bar pull-up': 'pull up bar',
    'clean and jerk': 'barbell',
    'cleans': 'barbell',
    'deadlift ': 'barbell',
    'double-under': 'jump rope',
    'dumbbell squat clean': 'dumbbell',
    'dumbbell squat snatche': 'barbell',
    'farmers carry': 'kettlebell',
    'front squat': 'barbell',
    'handstand push-up': 'wall',
    'handstand walk ': 'running space',
    'handstand walking': 'running space',
    'hang power clean': 'barbell',
    'hang squat clean ': 'barbell',
    'hang squat snatch': 'barbell',
    'hip extension': 'GHD machine',
    'kettlebell snatch': 'kettlebell',
    'kettlebell swing': 'kettlebell',
    'knees-to-elbow ': 'pull up bar',
    'legless rope climb': 'climbing rope',
    'medicine ball clean ': 'medicine ball',
    'muscle-up': 'rings',
    'one-leged squat': 'none',
    'overhead squat': 'barbell',
    'power clean': 'barbell',
    'power snatch': 'barbell',
    'pull-up': 'pull up bar',
    'push jerk': 'barbell',
    'push press': 'barbell',
    'push-up': 'none',
    'ring dip': 'rings',
    'rope climb': 'climbing rope',
    'row': 'rowing machine',
    'run': 'running space',
    'shoulder press': 'barbell',
    'single-arm dumbbell overhead lunge ': 'dumbbell',
    'sit-up': 'none',
    'snatch': 'barbell',
    'sprint': 'running space',
    'squat': 'none',
    'squat clean': 'barbell',
    'squat clean and jerk': 'barbell',
    'step-up': 'box',
    'strict pull-up': 'pull up bar',
    'sumo deadlift high pull': 'barbell',
    'swim': 'pool',
    'thruster': 'barbell',
    'toes-to-bar': 'pull up bar',
    'triple-under': 'jump rope',
    'wall-ball shot': 'wall ball',
    'weighted lunge': 'barbell'
}

CANON_EQUIP_TO_DB_EQUIP = [
    {
        canon: 'GHD machine',
        db: 'ghd'
    },
    {
        canon: 'pull up bar',
        db: 'pull_up_bar'
    },
    {
        canon: 'kettlebell',
        db: 'kettlebell'
    },
    {
        canon: 'barbell',
        db: 'barbell'
    },
    {
        canon: 'GHD machine',
        db: 'ghd'
    },{
        canon: 'GHD machine',
        db: 'ghd'
    },{
        canon: 'GHD machine',
        db: 'ghd'
    },{
        canon: 'GHD machine',
        db: 'ghd'
    },
    {
        canon: 'GHD machine',
        db: 'ghd'
    },
    {
        canon: 'GHD machine',
        db: 'ghd'
    },
    {
        canon: 'GHD machine',
        db: 'ghd'
    },{
        canon: 'GHD machine',
        db: 'ghd'
    },
    {
        canon: 'GHD machine',
        db: 'ghd'
    },
    {
        canon: 'GHD machine',
        db: 'ghd'
    },
    {
        canon: 'GHD machine',
        db: 'ghd'
    },






]