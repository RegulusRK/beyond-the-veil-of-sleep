class entity:
    def __init__(self, name, life, weapon, damage):
        self.name = name
        self.life = life
        self.weapon = weapon
        self.damage = damage

def player_info():
    print('\n' * 130)
    entity.life = 20
    entity.weapon = 'Mãos nuas'
    entity.damage = 1
    print('Esse é você: \n')
    print('====================')
    print(f'    Nome: ', entity.name)
    print('====================')
    print(f'Life: ', entity.life)
    print(f'Vida:', entity.life,'/',entity.life)
    print(f'Arma: ', entity.weapon)
    print(f'Dano: ', entity.damage)

def create_entity_obj(class_ent, name, life, weapon, damage):
    new_entity = class_ent(name, life, weapon, damage)
    return (new_entity)

def create_player():
    print('Sob a lâmina prateada da lua, onde a névoa espessa se agarra aos ossos retorcidos dos esquecidos, o ar pesa com o fedor de sangue pisado e ferro velho. Entre os cadáveres ainda mornos e as carcaças secas que adornam')
    print('...A razão humana tropeça. Uma dúvida lancinante brota nas sombras da mente, persistente como a praga, sussurrando entre os ecos de perguntas que nunca encontrarão resposta. Dentre elas, a mais simples dentre elas irrompe:')
    entity.name = input('Como você se chama?\n')

player1 = create_entity_obj(entity, "Regulus", 20, "Sword", 2)
player2 = create_entity_obj(entity, "Edward", 30, "Axe", 7)

print(player1)
print(player2)

