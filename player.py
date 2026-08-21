class entity:
    def __init__(self, name, life, weapon, damage):
        self.name = name
        self.life = life
        self.weapon = weapon
        self.damage = damage

def create_entity_obj(class_ent, name, life, weapon, damage):
    new_entity = class_ent(name, life, weapon, damage)
    return (new_entity)

def player_name_error():
    print('Tente se lembrar, pelo menos o nome...')
    name = input('Então, qual seu nome?\n')
    name_len = len(name)
    if (name_len < 1):
        print('Não consegue se lembrar se quer disso...?')
        name = input('Talvez, seu nome seja...\n')
        name_len = len(name)
        if (name_len < 1):
            print('Você olha para todo os lados, e somente corpos e rios de sangue são vistos*\nTalvez, seu nome pudesse ser "Lethe"... naquele momento, sem saber ao certo o real\nmotivo, aquele nome fazia muito sentido.')
            name = 'Lethe'
    return (name)

def create_player():
    print('\n' * 130)
    print('Sob a lâmina prateada da lua, onde a névoa espessa se agarra aos ossos retorcidos dos esquecidos,\no ar pesa com o fedor de sangue pisado e ferro velho. Entre os cadáveres ainda mornos e as carcaças')
    print('secas que adornam. A razão humana tropeça. Uma dúvida lancinante brota nas sombras da mente,\npersistente como a praga, sussurrando entre os ecos de perguntas que nunca encontrarão resposta.\nDentre elas, a mais simples dentre elas irrompe:')
    name = input('Como você se chama?\n')
    name_len = len(name)
    if (name_len < 1):
        name = player_name_error()   
    player = create_entity_obj(entity, name, 20, 'Mãos nuas', 2)
    return (player)

def player_info(player):
    print('Esse é você: \n')
    print('====================')
    print(f'    Nome: ', player.name)
    print('====================')
    print(f'Life: ', player.life)
    print(f'Vida:', player.life,'/',player.life)
    print(f'Arma: ', player.weapon)
    print(f'Dano: ', player.damage)

