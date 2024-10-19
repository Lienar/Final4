from .models import *
from .Inventory import *


def create_location_blank(data):
    new_location_gen(data)
    Location_empty.objects.create(location_name=data['location_name'], description=data['description'])


def create_location_encaunter(data):
    new_location_gen(data)
    Location_enemy.objects.create(location_name=data['location_name'], description=data['description'],
                                  enemy_name=data['enemy_name'])


def create_location_trap(data):
    new_location_gen(data)
    Location_trap.objects.create(location_name=data['location_name'], description=data['description'],
                                 trap_description=data['trap_description'], trap_activation_chance=data['trap_activation_chance'],
                                 trap_damage_min=data['trap_damage_min'], trap_damage_max=data['trap_damage_max'],
                                 trap_exists=data['trap_exists'], trap_found=data['trap_found'])


def create_location_riddle(data):
    new_location_gen(data)
    Location_enemy.objects.create(location_name=data['location_name'], description=data['description'],
                                  riddle_answer=data['riddle_answer'], riddle_solved_text=data['riddle_solved_text'])

def create_class(data):
    Player_class.objects.create(class_id=data['class_id'], class_name=data['class_name'],
                                 class_description=data['class_description'], class_health=data['class_health'],
                                 class_inventory=data['class_inventory'])

def create_enemy(data):
    Enemy.objects.create(name=data['name'], enemy_class=data['enemy_class'], enemy_description=data['enemy_description'],
                         health=data['health'], enemy_skill1_id=data['enemy_skill1_id'], enemy_skill2_id=data['enemy_skill2_id'])


def create_enemy_skill(data):
    Enemy_skill.objects.create(skill_name = data['skill_name'], skill_id = data['skill_id'], skill_type = data['skill_type'],
                               skill_description = data['skill_description'], skill_effect_max = data['skill_effect_max'],
                               skill_effect_min = data['skill_effect_min'], skill_cooldown = data['skill_cooldown'])

def create_inventory(data):
    is_have_heal = False
    is_have_empty_slot = True
    item1 = find_item(data['item1'])
    item2 = find_item(data['item2'])
    item3 = find_item(data['item3'])
    item4 = find_item(data['item4'])
    item5 = find_item(data['item5'])
    item6 = find_item(data['item6'])
    items = [item1, item2, item3, item4, item5, item6]
    for item in items:
        if item.item_type == 'Heal' and is_have_heal == False:
            is_have_heal = True
        if item.item_name == 'Empty' and is_have_empty_slot == False:
                is_have_heal = True

    Class_inventory.objects.create(inventory_id = data['inventory_id'], item1=data['item1'], item2=data['item2'],
                                   item3=data['item3'], item4=data['item4'], item5=data['item5'], item6=data['item6'],
                                   is_have_heal=is_have_heal, is_have_empty_slot=is_have_empty_slot)

def create_item(data):
    Item_list.objects.create(item_id = data.item_id, item_type = data.item_type, item_name = data.item_name,
                             description = data.description, skill_description = data.skill_description,
                             skill_effect_max = data.skill_effect_max, skill_effect_min = data.skill_effect_min,
                             skill_cooldown = data.skill_cooldown)

def new_location_gen(data):
    last_location_id = len(Location.objects.all())
    Location.objects.create(id_number=last_location_id + 1, location_name=data['location_name'],
                            location_type=data['location_type'], is_it_tech=data['is_it_tech'])


