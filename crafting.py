import loot_table, ids


def getRecipe(recipeName: str):
  if recipeName in crafts.keys():
    return crafts[recipeName]
  else:
    return 'nil'


def getItem(item: str):
	n = 1
	while ids.ids[str(n)] != item:
		n += 1
	return str(n)


def checkItem(entity, recipe, count):
  print(recipe)
  for n in range(len(recipe) - 1):
    if type(recipe[-1]) is not str:
      if int(entity[1]['material'][getItem(recipe[n][0])]) < int(recipe[n][1] * int(count) / recipe[-1][1]):
        return False
    else:
      if type(recipe[n]) is not str:
        if int(entity[1]['material'][getItem(recipe[n][0])]) < int(recipe[n][1]):
          return False
  return True

crafts = {
  "wooden_pickaxe": [
    ["discord:wood_planks", 3],
    ["discord:stick", 2],
    "pm" + str(loot_table.pickaxe_multiplier['discord:wooden_pickaxe'])
  ],
  "stone_pickaxe": [
    ["discord:stone", 3],
    ["discord:stick", 2],
    "pm" + str(loot_table.pickaxe_multiplier['discord:stone_pickaxe'])
  ],
  "iron_pickaxe": [
    ["discord:iron", 3],
    ["discord:stick", 2],
    "pm" + str(loot_table.pickaxe_multiplier['discord:iron_pickaxe'])
  ],
  "diamond_pickaxe": [
    ["discord:diamond", 3],
    ["discord:stick", 2],
    "pm" + str(loot_table.pickaxe_multiplier['discord:diamond_pickaxe'])
  ],
  "obsidian_pickaxe": [
    ["discord:obsidian", 3],
    ["discord:stick", 2],
    "pm" + str(loot_table.pickaxe_multiplier['discord:obsidian_pickaxe'])
  ],
  "netherite_pickaxe": [
    ['discord:netherite_ingot', 3],
    ['discord:stick', 2],
    "pm" + str(loot_table.pickaxe_multiplier['discord:netherite_pickaxe'])
  ],
  "wooden_axe": [
    ["discord:wood_planks", 3],
    ["discord:stick", 2],
    "am" + str(loot_table.foraging_multiplier['discord:wooden_axe'])
  ],
  "stone_axe": [
    ["discord:stone", 3],
    ["discord:stick", 2],
    "am" + str(loot_table.foraging_multiplier['discord:stone_axe'])
  ],
  "iron_axe": [
    ["discord:iron", 3],
    ["discord:stick", 2],
    "am" + str(loot_table.foraging_multiplier['discord:iron_axe'])
  ],
  "diamond_axe": [
    ["discord:diamond", 3],
    ["discord:stick", 2],
    "am" + str(loot_table.foraging_multiplier['discord:diamond_axe'])
  ], 

  "obsidian_axe": [
    ["discord:obsidian", 3],
    ["discord:stick", 2],
    "am" + str(loot_table.foraging_multiplier['discord:obsidian_axe'])
  ],
  "netherite_axe": [
    ['discord:netherite_ingot', 3],
    ['discord:stick', 2],
    "am" + str(loot_table.foraging_multiplier['discord:netherite_axe'])
  ], 
  
  "wooden_sword": [
    ["discord:wood_planks", 2],
    ["discord:stick", 1],
    "sm" + str(loot_table.sword_multiplier['discord:wooden_sword'])
  ],

  "stone_sword": [
    ["discord:stone", 2],
    ["discord:stick", 1],
    "sm" + str(loot_table.sword_multiplier['discord:stone_sword'])
  ],

  "iron_sword": [
    ["discord:iron", 2],
    ["discord:stick", 1],
    "sm" + str(loot_table.sword_multiplier['discord:iron_sword'])
  ],

  "diamond_sword": [
    ["discord:diamond", 2],
    ["discord:stick", 1],
    "sm" + str(loot_table.sword_multiplier['discord:diamond_sword'])
  ],
  "obsidian_sword": [
    ["discord:obsidian", 2],
    ["discord:stick", 1],
    "sm" + str(loot_table.sword_multiplier['discord:obsidian_sword'])
  ],
  "undead_sword": [
    ["discord:rotten_flesh", 512],
    ["discord:bone", 256],
    "sm" + str(loot_table.sword_multiplier['discord:undead_sword'])
  ],
  "netherite_sword": [
    ['discord:netherite_ingot', 2],
    ['discord:stick', 1],
    "sm" + str(loot_table.sword_multiplier['discord:netherite_sword'])
  ],
  "wood_planks": [
    ["discord:wood", 1],
    ['discord:wood_planks', 4]
  ],
  "stick": [
    ["discord:wood_planks", 2],
    ["discord:stick", 4]
  ],
  "crafting_table": [
    ["discord:wood_planks", 4],
    ["discord:crafting_table", 1]
  ],
  "stone_nerd": [
    ["discord:stone", 1000000], 
    ["discord:stone_nerd", 1]
  ], 
  "wood_nerd": [
    ["discord:wood", 1000000], 
    ["discord:wood_nerd", 1]
  ], 
  "netherrack_nerd": [
    ["discord:netherrack", 1000000], 
    ["discord:netherrack_nerd", 1]
  ], 
	"enchanted_stick": [
		["discord:stick", 1000], 
		["discord:enchanted_stick", 1]
	], 
  "iron_armor": [
    ["discord:iron", 24],
    "armor" + str(loot_table.armor_multiplier['discord:iron_armor'])
  ],
  "diamond_armor": [
    ["discord:diamond", 24],
    "armor" + str(loot_table.armor_multiplier['discord:diamond_armor'])
  ],
  "obsidian_armor": [
    ["discord:obsidian", 24],
    "armor" + str(loot_table.armor_multiplier['discord:obsidian_armor'])
  ],
  "netherite_armor": [
    ["discord:netherite_ingot", 24],
    "armor" + str(loot_table.armor_multiplier['discord:netherite_armor'])
  ],
  "iron_shield": [
    ["discord:wood_planks", 6],
    ["discord:iron", 1],
    "shield" + str(loot_table.shield_multiplier['discord:iron_shield'])
  ],
  "diamond_shield": [
    ["discord:wood_planks", 6],
    ["discord:diamond", 1],
    "shield" + str(loot_table.shield_multiplier['discord:diamond_shield'])
  ],
  "obsidian_shield": [
    ["discord:wood_planks", 6],
    ["discord:obsidian", 1],
    "shield" + str(loot_table.shield_multiplier['discord:obsidian_shield'])
  ],
  "bow": [
    ["discord:string", 3],
    ["discord:stick", 3],
    "bow" + str(loot_table.bow_multiplier['discord:bow'])
  ],
  "explosive_bow": [
    ["discord:gunpowder", 192],
    ["discord:stick", 3],
    "bow" + str(loot_table.bow_multiplier['discord:explosive_bow'])
  ],
  "undead_bow": [
    ["discord:rotten_flesh", 128],
    ["discord:bone", 64],
    ["discord:stick", 3],
    "bow" + str(loot_table.bow_multiplier['discord:undead_bow'])
  ],
  "portal_table": [
    ["discord:obsidian", 8],
    ["discord:diamond", 1],
    ["discord:portal_table", 1]
  ],
  "nether_portal": [
    ['discord:obsidian', 14],
    ['discord:wood_planks', 1],
    ['discord:lava', 1],
    ['discord:nether_portal', 1]
  ],
  "end_portal": [
    ['discord:eye_of_ender', 15],
    ['discord:netherite_scrap', 20],
    ['discord:end_portal', 1]
  ],
  "netherite_ingot": [
    ['discord:netherite_scrap', 4],
    ['discord:gold', 4],
    ["discord:diamond", 16], 
    ['discord:netherite_ingot', 1]
  ],
  "blaze_powder": [
    ['discord:blaze_rod', 1],
    ['discord:blaze_powder', 2]
  ],
  "chorus_fruit": [
    ['discord:chorus_seed', 4],
    ['discord:chorus_fruit', 1]
  ],
  "eye_of_ender": [
    ['discord:blaze_powder', 1],
    ['discord:ender_pearl', 1],
    ['discord:eye_of_ender', 1]
  ], 
  "gold": [
    ['discord:gold_nugget', 9],
    ['discord:gold', 1]
  ], 
  "wool": [
    ['discord:string', 4],
    ['discord:wool', 1]
  ], 
  "bed": [
    ['discord:wool', 3],
    ["discord:wood_planks", 3], 
    ['discord:bed', 1]
  ],
}