import mysql.connector
import yaml


def database_insert(host='localhost', user='root', password='Hunter55!', database='dnd5e', vals=[]):

    my_database = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    mycursor = my_database.cursor()

    sql = 'INSERT INTO items_weaponweaponproperty ' \
          '(property_id_id, weapon_id_id)' \
          'VALUES (%s, %s)'

    val = vals

    mycursor.executemany(sql, val)

    my_database.commit()

    print(mycursor.rowcount, 'was inserted.')


def get_db_values(file_path, keys=[]):

    inserts = []

    with open(file_path, 'r') as infile:
        records = yaml.full_load(infile) or []

    types = {'Simple Melee': 1, 'Simple Ranged': 2, 'Martial Melee': 3, 'Martial Ranged': 4}
    damage_type = {'Acid': 1, 'Bludgeoning': 2, 'Cold': 3, 'Fire': 4, 'Force': 5, 'Lightning': 6, 'Necrotic': 7,
                   'Piercing': 8, 'Poison': 9, 'Psychic': 10, 'Radiant': 11, 'Slashing': 12, 'Thunder': 13}
    p = {
        'Ammunition': 1,
        'Finesse': 2,
        'Heavy': 3,
        'Light': 4,
        'Loading': 5,
        'Monk': 6,
        'Reach': 7,
        'Special': 8,
        'Thrown': 9,
        'Two-Handed': 10,
        'Versatile': 11
    }

    for record in records:
        entry = []

        for keys, values in record.items():
            if values['equipment_category']['index']:
                if values['equipment_category']['index'] == 'weapon':

                    name = keys
                    properties = []

                    for property in values['properties']:
                        properties.append(property['name'])

                    que = {name: properties}
                    entry.append(que)

                    inserts.append(entry[0])

    # print(inserts)

    num = []

    for obj in enumerate(inserts, start=24):
        num.append(obj)

    # print(num)

    db_entries = []

    for i in num:
        dic = i[1]
        for v in dic.values():
            for value in v:
                db_entries.append([p[value], i[0]])

    print(db_entries)








                    # # Cost
                    # cost = values['cost']['quantity']
                    # unit = values['cost']['unit']
                    # if unit == 'gp':
                    #     cost = cost * 100
                    # elif unit == 'sp':
                    #     cost = cost * 10
                    # entry[1] = cost
                    #
                    # # Name
                    # entry[0] = keys
                    #
                    # # damage
                    # if entry[0] == 'Net':
                    #     entry[2], entry[3] = None, 14
                    #     entry[4] = '4'
                    # elif values['damage']:
                    #     entry[2] = values['damage']['damage_dice']
                    #     # damage type
                    #     entry[3] = damage_type[values['damage']['damage_type']['name']]
                    #
                    # # weapon type
                    # entry[4] = types[values['category_range']]
                    #
                    # # weight
                    # entry[5] = values['weight']
                    #
                    # inserts.append(entry)

    return db_entries


# vals = get_db_values('/home/graham/VSCode/webscraper/dndequipment.yaml', ['property_id_id', 'weapon_id_id'])

# database_insert(vals=vals)
