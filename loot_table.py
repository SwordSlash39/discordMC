import random, ids


def getChance(decimalChance):
  return 1 / decimalChance

def getID(material: str):
	for ID in ids.ids.keys():
		if str(ids.ids[ID]) == material:
			return str(ID)

pickaxe_multiplier = {
  'discord:wooden_pickaxe': 1, 
  'discord:stone_pickaxe': 2, 
  'discord:iron_pickaxe': 4,
  'discord:diamond_pickaxe': 10,
  'discord:obsidian_pickaxe': 25,
  'discord:netherite_pickaxe': 50
}

hunting_loot = {
  'discord:overworld': {
    getID('discord:meat'): 10,
    getID('discord:leather'): 1,
    getID('discord:bone'): 0.25, 
		getID('discord:apple'): 0.1
  },
  'discord:nether': {
    getID('discord:meat'): 5,
    getID('discord:leather'): 0.5,
    getID('discord:string'): 0.1,
    getID('discord:ender_pearl'): 0.005,
    getID('discord:blaze_rod'): 0.0025
  },
  'discord:end': {
    getID('discord:ender_pearl'): 0.01
  }
}

farming_loot = {
  'discord:overworld': {
    getID('discord:sugar_cane'): 0.1
  },
  'discord:nether': {
  },
  'discord:end': {
  }
}

mining_loot = {
  'discord:overworld': {
    getID('discord:stone'): [8, pickaxe_multiplier['discord:wooden_pickaxe']], 
    getID('discord:iron'): [0.1, pickaxe_multiplier['discord:stone_pickaxe']],
    getID('discord:diamond'): [0.01, pickaxe_multiplier['discord:iron_pickaxe']],
    getID('discord:obsidian'): [0.001, pickaxe_multiplier['discord:diamond_pickaxe']]
  },
  'discord:nether': {
    getID('discord:netherrack'): [10, pickaxe_multiplier['discord:wooden_pickaxe']],
    getID('discord:nether_quartz'): [0.25, pickaxe_multiplier['discord:wooden_pickaxe']],
    getID('discord:magma_block'): [0.1, pickaxe_multiplier['discord:wooden_pickaxe']],
    getID('discord:gold_nugget'): [0.005, pickaxe_multiplier['discord:wooden_pickaxe']],
    getID('discord:obsidian'): [0.01, pickaxe_multiplier['discord:diamond_pickaxe']],
    getID('discord:netherite_scrap'): [0.001, pickaxe_multiplier['discord:obsidian_pickaxe']]
  },
  'discord:the_end': {
    getID('discord:end_stone'): [5, pickaxe_multiplier['discord:stone_pickaxe']],
    getID('discord:obsidian'): [0.75, pickaxe_multiplier['discord:diamond_pickaxe']], 
    getID('discord:chorus_seed'): [0.0005, pickaxe_multiplier['discord:netherite_pickaxe']]
  }
}

mining_rare_drop = {
  'discord:overworld': {
    getID('discord:lava'): [0.5, 5000, pickaxe_multiplier['discord:obsidian_pickaxe']]
  },
  'discord:nether': {
    getID('discord:gold'): [0.2, 5000, pickaxe_multiplier['discord:wooden_pickaxe']]
  },
  'discord:the_end': {
    getID('discord:end_crystal'): [0.25, 10000, pickaxe_multiplier['discord:netherite_pickaxe']]
  }
}

foraging_multiplier = {
  'discord:wooden_axe': 2,
  'discord:stone_axe': 3,
  'discord:iron_axe': 5,
  'discord:diamond_axe': 11, 
  'discord:obsidian_axe': 25,
  'discord:netherite_axe': 50
}

armor_multiplier = {
  'discord:iron_armor': 5,
  'discord:diamond_armor': 15,
  'discord:obsidian_armor': 35,
  'discord:netherite_armor': 50
}

sword_multiplier = {
  'discord:wooden_sword': 2,
  'discord:stone_sword': 3,
  'discord:iron_sword': 6,
  'discord:diamond_sword': 12, 
  'discord:obsidian_sword': 25,
  'discord:undead_sword': 42,
  'discord:netherite_sword': 85
}

shield_multiplier = {
  'discord:iron_shield': 5,
  'discord:diamond_shield': 11,
  'discord:obsidian_shield': 25
}

bow_multiplier = {
  'discord:bow': 5,
  'discord:undead_bow': 18,
  'discord:explosive_bow': 20,
  'discord:crossbow': 30
}

# [Min, Max, Weight]
combat_loot = {
  'discord:overworld': { 
    'discord:zombie': {
      getID('discord:rotten_flesh'): [2, 4, 80],
      getID('discord:meat'): [1, 2, 15], 
      getID('discord:iron'): [1, 2, 4], 
      getID('discord:diamond'): [1, 1, 1]
    },
    'discord:skeleton': {
      getID('discord:bone'): [2, 4, 75],
      getID('discord:arrow'): [2, 4, 25],
      'discord:bow': [1, 1, 1]
    },
    'discord:creeper': {
      getID('discord:gunpowder'): [2, 4, 90],
      getID('discord:tnt'): [1, 1, 5]
    },
    'discord:spider': {
      getID('discord:string'): [1, 3, 70],
      getID('discord:spider_eye'): [1, 2, 10]
    },
    'discord:enderman': {
      getID('discord:ender_pearl'): [1, 2, 80]
    }
  },
  'discord:nether': {
    'discord:zombie_pigman': {
      getID('discord:rotten_flesh'): [1, 3, 42],
      getID('discord:gold_nugget'): [6, 9, 80]
    },
    'discord:blaze': {
      getID('discord:blaze_rod'): [1, 1, 50]
    }, 
    'discord:magma_cube': {
      getID('discord:magma_cream'): [1, 1, 75]
    }, 
    'discord:wither_skeleton': {
      getID('discord:bone'): [5, 8, 75], 
      getID('discord:wither_skull'): [1, 1, 5]
    }
  }, 
  'discord:the_end': {
    'discord:enderman': {
      getID('discord:ender_pearl'): [1, 2, 80],
      getID('discord:eye_of_ender'): [1, 1, 10]
    }
  }
}

# [Chance, strengthMin, strengthMax]

magma_cube = [[50, 3, 5], [30, 7, 10], [15, 13, 17], [5, 20, 25]]

mob_stats = { 
  'discord:zombie': [5, 3, 8],
  'discord:skeleton': [5, 5, 14],
  'discord:creeper': [5, 8, 22],
  'discord:spider': [10, 5, 15],
  'discord:enderman': [10, 12, 21],
  'discord:zombie_pigman': [25, 10, 17],
  'discord:blaze': [10, 10, 20], 
  'discord:wither_skeleton': [4, 15, 25]
}

structure_chance = {
  'discord:overworld': {
    'discord:buried_treasure': 1,
    'discord:village': 10,
    'discord:jungle_temple': 15, 
    'discord:desert_temple': 15,
    'discord:pillager_outpost': 5
  }, 
  'discord:nether': {
    'discord:nether_fortress': 9, 
    'discord:bastion_remnant': 12
  }, 
  'discord:the_end': {
    'discord:dev_house': 0.01
  }
}

# [Deathchance, Deathmessage]
structure_deaths = {
  'discord:buried_treasure': [20, 'suffocated'],
  'discord:village': [5, 'was slain by iron golem'],
  'discord:desert_temple': [10, 'was blown up by TNT'],
  'discord:jungle_temple': [20, 'stepped on traps and went off with a bang'],
  'discord:pillager_outpost': [15, 'was slain by Pillager'], 
  'discord:nether_fortress': [30, 'burnt to crisp'], 
  'discord:bastion_remnant': [40, 'was slain by piglin'], 
  'discord:dev_house': [75, 'was mistaken as a bug and got deleted']
}

# [Item, Weight, CountMin, Countmax]
structure_loot = {
  'discord:buried_treasure': [
    [getID('discord:diamond'), 100, 8, 14],
    [getID('discord:netherite_scrap'), 70, 1, 1], 
    [getID('discord:obsidian'), 90, 1, 3], 
    [getID('discord:iron'), 100, 15, 32],
    [getID('discord:rotten_flesh'), 100, 7, 15]
  ],
  'discord:village': [
    [getID('discord:emerald'), 5, 1, 2],
    [getID('discord:meat'), 25, 1, 10]
  ],
  'discord:desert_temple': [
    [getID('discord:tnt'), 100, 1, 9],
    [getID('discord:diamond'), 10, 1, 1],
    [getID('discord:iron'), 25, 1, 5]
  ],
  'discord:jungle_temple': [
    [getID('discord:iron'), 40, 3, 7],
    [getID('discord:diamond'), 5, 1, 2]
  ],
  'discord:pillager_outpost': [
    [getID('discord:iron'), 50, 2, 4],
    ['discord:crossbow', 1, 1, 1]
  ],
  'discord:nether_fortress': [
		[getID('discord:nether_wart'), 70, 4, 42],
    [getID('discord:diamond'), 25, 1, 2],
    [getID('discord:gold'), 25, 4, 6],
    [getID('discord:gold_nugget'), 50, 5, 8],
    [getID('discord:iron'), 75, 5, 15],
    [getID('discord:netherite_scrap'), 5, 1, 2]
  ],
  'discord:bastion_remnant': [
    [getID('discord:netherite_scrap'), 25, 2, 3],
    [getID('discord:gold'), 20, 5, 7],
    [getID('discord:netherite_ingot'), 10, 1, 2],
    [getID('discord:eye_of_ender'), 20, 1, 2]
  ], 
  'discord:dev_house': [
    [getID('discord:netherite_ingot'), 90, 10, 16],
    [getID('discord:dev_token'), 100, 1, 1]
  ]
}
