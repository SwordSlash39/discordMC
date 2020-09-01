import random, discord, math, time, loot_table, history, crafting, tags, portals, descriptions, tools, pets, ids


class word:
	def __init__(self, text):
		self.word = text
		self.enter = ""
		self.ans = ""
	
	def startswith(self, entered):
		self.enter = str(entered)
		for i in range(len(self.enter)):
			try:
				if self.enter[i] != self.word[i]:
					return False
			except:
				return False
		return True
	
	def clearfront(self, entered):
		self.ans = ""
		self.enter = int(entered)
		self.word = list(self.word)
		if len(self.word) >= self.enter + 1:
			for i in range(self.enter):
				self.word.pop(0)
			for i in range(len(self.word)):
				self.ans += self.word[i]
			self.word = self.ans
			return self.word
		else:
			pass

	def clearback(self, entered):
		self.ans = ""
		self.enter = int(entered)
		self.word = list(self.word)
		if len(self.word) >= self.enter + 1:
			for i in range(self.enter):
				self.word.pop(len(self.word) - 1)
			for i in range(len(self.word)):
				self.ans += self.word[i]
			self.word = self.ans
			return self.word
		else:
			pass

client = discord.Client()
token = '---'
default_call = history.default_call
txt = ''
msg = ''
auth = []
daytime = [True, 1595840752.1231422]
explore_delay = 10

# Special items
special_items = ["discord:dev_token", 'discord:national_flag_2020', 'discord:medal_of_contribution', "discord:first_5", "discord:wood_nerd", "discord:stone_nerd", "discord:netherrack_nerd"]

# Materials
mats = []
for n in range(len(ids.ids)):
	mats.append(str(n + 1))

acts = [['mining', 'time_mine'], ['hunting', 'time_hunt'], ['chopping', 'time_chop'], ['explore', 'time_explore']]
icon = "https://lh3.googleusercontent.com/-Th4UBxDTJQI/Xy4gVrirvBI/AAAAAAAAA10/og_TMT0sJ6wo0wdBJcn9iQvYOxUD2uZUQCK8BGAsYHg/s0/download.jpeg"

players = [['603569154171207701', {'times': {'time_chop': 1597056692.981584, 'time_mine': 1597373925.6324725, 'time_hunt': 1597374312.9973466, 'time_explore': 1597497625.8576834}, 'actions': {'chopping': False, 'mining': False, 'hunting': True, 'explore': False}, 'material': {'discord:wood': 25, 'discord:wood_planks': 122, 'discord:crafting_table': 1, 'discord:stick': 3, 'discord:stone': 511082, 'discord:iron': 18419, 'discord:diamond': 1115, 'discord:obsidian': 2251, 'discord:meat': 757986006.8, 'discord:lava': 127, 'discord:rotten_flesh': 24, 'discord:bone': 23, 'discord:arrow': 0, 'discord:tnt': 35, 'discord:gunpowder': 2, 'discord:string': 0, 'discord:spider_eye': 0, 'discord:portal_table': 1, 'discord:netherite_scrap': 37, 'discord:netherite_ingot': 22, 'discord:magma_block': 22095, 'discord:blaze_rod': 2, 'discord:gold': 7, 'discord:nether_quartz': 55247, 'discord:netherrack': 2210170, 'discord:nether_portal': 1, 'discord:blaze_powder': 4, 'discord:eye_of_ender': 0, 'discord:ender_pearl': 0, 'discord:emerald': 5, 'discord:first_5': 1, 'discord:national_flag_2020': 1, 'discord:medal_of_contribution': 1, 'discord:end_portal': 0, 'discord:gold_nugget': 16, 'discord:wool': 0, 'discord:bed': 0, 'discord:chorus_fruit': 0, 'discord:end_stone': 0, 'discord:chorus_seed': 0, 'discord_magma_cream': 0, 'discord:magma_cream': 11, 'discord:stone_nerd': 1, 'discord:wood_nerd': 0, 'discord:netherrack_nerd': 0, 'discord:dev_token': 0, 'discord:leather': 4, 'discord:apple': 0, 'discord:enchanted_stick': 0}, 'tools': {'chop': 25, 'mine': 50, 'hunt': 85, 'shoot': 30}, 'armor': {'shield': 25, 'body': 50}, 'dimension': 'discord:nether', 'wardrobe': {'1': 'discord:obsidian_armor', '2': 'discord:netherite_armor', '3': 'discord:obsidian_armor'}, 'pets': []}], ['611513933710229504', {'times': {'time_chop': 1597579707.008055, 'time_mine': 1598183916.0656385, 'time_hunt': 1597579707.0080562, 'time_explore': 1598183982.656798}, 'actions': {'chopping': False, 'mining': True, 'hunting': False, 'explore': False}, 'material': {'1': 7024, '2': 199, '3': 1, '4': 16, '5': 599853, '6': 20045, '7': 1814, '8': 250712, '14': 66880.8, '9': 163, '10': 46, '11': 35, '12': 8, '13': 17, '15': 0, '16': 1314, '17': 0, '18': 1, '19': 22, '22': 0, '23': 13470, '24': 22, '25': 184, '26': 33690, '27': 347860, '28': 1, '29': 4, '30': 6, '31': 44, '32': 1, '45': 1, '44': 1, '43': 1, '35': 1, '38': 36, '40': 1661571, '41': 21, '33': 195, '34': 0, '37': 1, '36': 20, '46': 0, '47': 1, '48': 1, '39': 0, '42': 6580, '20': 0, '21': 0, '49': 15, '50': 0, '51': 0, '52': 0}, 'tools': {'chop': 25, 'mine': 50, 'hunt': 85, 'shoot': 30}, 'armor': {'shield': 25, 'body': 50}, 'dimension': 'discord:the_end', 'wardrobe': {'1': 'discord:obsidian_armor', '2': 'discord:netherite_armor', '3': None}, 'pets': [['wolf', 'tiger']]}], ['697013961698181161', {'times': {'time_chop': 1595321866.4887702, 'time_mine': 1595321601.6574612}, 'actions': {'chopping': True, 'mining': False}, 'material': {'discord:wood': 23, 'discord:wood_planks': 4, 'discord:crafting_table': 0, 'discord:stick': 0, 'discord:stone': 0, 'discord:iron': 0, 'discord:diamond': 0, 'discord:obsidian': 0}, 'tools': {'chop': 1, 'mine': 0, 'hunt': 1}}], ['730338865583358073', {'times': {'time_chop': 1595407267.4630358, 'time_mine': 1595839923.155249, 'time_hunt': 1595839672.5558612}, 'actions': {'chopping': False, 'mining': True, 'hunting': False}, 'material': {'discord:wood': 0, 'discord:wood_planks': 33, 'discord:crafting_table': 1, 'discord:stick': 2, 'discord:stone': 63, 'discord:iron': 0, 'discord:diamond': 0, 'discord:obsidian': 0, 'discord:meat': 160.4, 'discord:lava': 0, 'discord:rotten_flesh': 0, 'discord:bone': 0, 'discord:arrow': 0, 'discord:tnt': 0, 'discord:gunpowder': 0, 'discord:string': 0, 'discord:spider_eye': 0, 'discord:portal_table': 0, 'discord:netherite_scrap': 0, 'discord:netherite_ingot': 0, 'discord:magma_block': 0, 'discord:blaze_rod': 0, 'discord:gold': 0, 'discord:nether_quartz': 0, 'discord:netherrack': 0, 'discord:nether_portal': 0, 'discord:blaze_powder': 0, 'discord:eye_of_ender': 0, 'discord:ender_pearl': 0, 'discord:emerald': 0, 'discord:first_5': 1, 'discord:national_flag_2020': 1}, 'tools': {'chop': 1, 'mine': 2, 'hunt': 1, 'shoot': 0}, 'armor': {'shield': 0, 'body': 0}, 'dimension': 'discord:overworld'}], ['584019276315230211', {'times': {'time_chop': 1595421603.8348112, 'time_mine': 1595421603.8348114, 'time_hunt': 1595421603.8348117}, 'actions': {'chopping': False, 'mining': False, 'hunting': False}, 'material': {'discord:wood': 0, 'discord:wood_planks': 0, 'discord:crafting_table': 0, 'discord:stick': 0, 'discord:stone': 0, 'discord:iron': 0, 'discord:diamond': 0, 'discord:obsidian': 0, 'discord:meat': 10.0, 'discord:lava': 0, 'discord:rotten_flesh': 0, 'discord:bone': 0, 'discord:arrow': 0, 'discord:tnt': 0, 'discord:gunpowder': 0, 'discord:string': 0, 'discord:spider_eye': 0, 'discord:portal_table': 0, 'discord:netherite_scrap': 0, 'discord:netherite_ingot': 0, 'discord:magma_block': 0, 'discord:blaze_rod': 0, 'discord:gold': 0, 'discord:nether_quartz': 0, 'discord:netherrack': 0, 'discord:nether_portal': 0, 'discord:blaze_powder': 0, 'discord:eye_of_ender': 0, 'discord:ender_pearl': 0, 'discord:emerald': 0, 'discord:gold_nugget': 0, 'discord:wool': 0, 'discord:end_portal': 0, 'discord:magma_cream': 0, 'discord:bed': 0, 'discord:chorus_fruit': 0, 'discord:dev_token': 0, 'discord:end_stone': 0, 'discord:chorus_seed': 0, 'discord:medal_of_contribution': 0, 'discord:national_flag_2020': 0, 'discord:first_5': 0, 'discord:wood_nerd': 0, 'discord:stone_nerd': 0, 'discord:netherrack_nerd': 0}, 'tools': {'chop': 1, 'mine': 0, 'hunt': 1, 'shoot': 0}, 'armor': {'body': None, 'shield': None}, 'dimension': 'discord:overworld'}], ['620070372452204551', {'times': {'time_chop': 1597374513.0533295, 'time_mine': 1597374513.0533307, 'time_hunt': 1597374513.0533311}, 'actions': {'chopping': False, 'mining': True, 'hunting': False}, 'material': {'discord:meat': 19523.1, 'discord:crafting_table': 1, 'discord:stone': 318052, 'discord:iron': 3940, 'discord:diamond': 379, 'discord:obsidian': 107, 'discord:lava': 5, 'discord:rotten_flesh': 0, 'discord:bone': 0, 'discord:arrow': 0, 'discord:tnt': 0, 'discord:gunpowder': 0, 'discord:string': 389, 'discord:spider_eye': 0, 'discord:portal_table': 1, 'discord:netherite_scrap': 0, 'discord:netherite_ingot': 3, 'discord:magma_block': 1276, 'discord:blaze_rod': 0, 'discord:gold': 16, 'discord:nether_quartz': 3190, 'discord:netherrack': 127693, 'discord:nether_portal': 1, 'discord:blaze_powder': 0, 'discord:eye_of_ender': 7, 'discord:ender_pearl': 1, 'discord:emerald': 0, 'discord:wood': 93, 'discord:wood_planks': 291, 'discord:stick': 11, 'discord:national_flag_2020': 1, 'discord:end_portal': 1, 'discord:medal_of_contribution': 0, 'discord:end_stone': 0, 'discord:chorus_seed': 0, 'discord:chorus_fruit': 0, 'discord:gold_nugget': 63, 'discord:wool': 0, 'discord:bed': 0, 'discord:magma_cream': 1, 'discord:first_5': 0, 'discord:wood_nerd': 0, 'discord:stone_nerd': 0, 'discord:netherrack_nerd': 0, 'discord:dev_token': 0, 'discord:leather': 1952}, 'tools': {'chop': 25, 'mine': 25, 'hunt': 25, 'shoot': 0}, 'armor': {'body': 35, 'shield': 25}, 'dimension': 'discord:the_end', 'wardrobe': {'1': '', '2': 'discord:iron_armor', '3': 'discord:obsidian_armor'}}], ['526745153143177216', {'times': {'time_chop': 1597061711.568761, 'time_mine': 1597373942.7027369, 'time_hunt': 1597062118.3680727}, 'actions': {'chopping': False, 'mining': True, 'hunting': False}, 'material': {'discord:meat': 17.6, 'discord:crafting_table': 1, 'discord:stone': 0, 'discord:iron': 0, 'discord:diamond': 0, 'discord:obsidian': 0, 'discord:lava': 0, 'discord:rotten_flesh': 0, 'discord:bone': 0, 'discord:arrow': 0, 'discord:tnt': 0, 'discord:gunpowder': 0, 'discord:string': 0, 'discord:spider_eye': 0, 'discord:portal_table': 0, 'discord:netherite_scrap': 0, 'discord:netherite_ingot': 0, 'discord:magma_block': 0, 'discord:blaze_rod': 0, 'discord:gold': 0, 'discord:nether_quartz': 0, 'discord:netherrack': 0, 'discord:nether_portal': 0, 'discord:blaze_powder': 0, 'discord:eye_of_ender': 0, 'discord:ender_pearl': 0, 'discord:emerald': 0, 'discord:gold_nugget': 0, 'discord:wood': 3672, 'discord:wood_planks': 2, 'discord:stick': 2, 'discord:end_portal': 0, 'discord:chorus_fruit': 0, 'discord:end_stone': 0, 'discord:chorus_seed': 0, 'discord:medal_of_contribution': 0, 'discord:national_flag_2020': 0, 'discord:wool': 0, 'discord:magma_cream': 0, 'discord:bed': 0, 'discord:first_5': 0, 'discord:wood_nerd': 0, 'discord:stone_nerd': 0, 'discord:netherrack_nerd': 0, 'discord:dev_token': 0, 'discord:leather': 0}, 'tools': {'chop': 1, 'mine': 0, 'hunt': 1, 'shoot': 0}, 'armor': {'body': None, 'shield': None}, 'dimension': 'discord:overworld', 'wardrobe': {'1': '', '2': None, '3': None}}], ['720259123639222286', {'times': {'time_chop': 1597147878.1576347, 'time_mine': 1597239283.1593993, 'time_hunt': 1597239224.8454516}, 'actions': {'chopping': False, 'mining': True, 'hunting': False}, 'material': {'discord:meat': 9.4, 'discord:crafting_table': 0, 'discord:stone': 0, 'discord:iron': 0, 'discord:diamond': 0, 'discord:obsidian': 0, 'discord:lava': 0, 'discord:rotten_flesh': 0, 'discord:bone': 0, 'discord:arrow': 0, 'discord:tnt': 0, 'discord:gunpowder': 0, 'discord:string': 0, 'discord:spider_eye': 0, 'discord:portal_table': 0, 'discord:netherite_scrap': 0, 'discord:netherite_ingot': 0, 'discord:magma_block': 0, 'discord:blaze_rod': 0, 'discord:gold': 0, 'discord:nether_quartz': 0, 'discord:netherrack': 0, 'discord:nether_portal': 0, 'discord:blaze_powder': 0, 'discord:eye_of_ender': 0, 'discord:ender_pearl': 0, 'discord:emerald': 0, 'discord:gold_nugget': 0, 'discord:wood': 0, 'discord:wood_planks': 0, 'discord:wool': 0, 'discord:stick': 0, 'discord:end_portal': 0, 'discord:magma_cream': 0, 'discord:bed': 0, 'discord:chorus_fruit': 0, 'discord:dev_token': 0, 'discord:end_stone': 0, 'discord:chorus_seed': 0, 'discord:medal_of_contribution': 0, 'discord:national_flag_2020': 0, 'discord:first_5': 0, 'discord:wood_nerd': 0, 'discord:stone_nerd': 0, 'discord:netherrack_nerd': 0}, 'tools': {'chop': 1, 'mine': 0, 'hunt': 1, 'shoot': 0}, 'armor': {'body': None, 'shield': None}, 'wardrobe': {'1': None, '2': None, '3': None}, 'dimension': 'discord:overworld'}], ['720421826139783188', {'times': {'time_chop': 1597369158.4184127, 'time_mine': 1597657876.2753992, 'time_hunt': 1597658021.0818105, 'time_explore': 1597657907.9175024}, 'actions': {'chopping': False, 'mining': False, 'hunting': True, 'explore': False}, 'material': {'discord:meat': 27024.3, 'discord:crafting_table': 1, 'discord:stick': 2, 'discord:stone': 493457, 'discord:iron': 6252, 'discord:diamond': 520, 'discord:obsidian': 1588, 'discord:lava': 21, 'discord:rotten_flesh': 43, 'discord:bone': 686, 'discord:arrow': 0, 'discord:tnt': 34, 'discord:gunpowder': 22, 'discord:string': 3, 'discord:spider_eye': 2, 'discord:portal_table': 1, 'discord:netherite_scrap': 158, 'discord:netherite_ingot': 5, 'discord:magma_block': 15937, 'discord:blaze_rod': 2, 'discord:gold': 71, 'discord:nether_quartz': 39848, 'discord:netherrack': 1594053, 'discord:nether_portal': 1, 'discord:blaze_powder': 0, 'discord:eye_of_ender': 9, 'discord:ender_pearl': 5, 'discord:emerald': 7, 'discord:wood': 0, 'discord:wood_planks': 72, 'discord:national_flag_2020': 1, 'discord:medal_of_contribution': 0, 'discord:end_portal': 0, 'discord:chorus_fruit': 0, 'discord:end_stone': 0, 'discord:chorus_seed': 0, 'discord:gold_nugget': 920, 'discord:wool': 0, 'discord:bed': 0, 'discord_magma_cream': 0, 'discord:first_5': 0, 'discord:magma_cream': 11, 'discord:wood_nerd': 0, 'discord:stone_nerd': 0, 'discord:netherrack_nerd': 0, 'discord:dev_token': 0, 'discord:leather': 2702, 'discord:apple': 0, 'discord:enchanted_stick': 0}, 'tools': {'chop': 50, 'mine': 50, 'hunt': 85, 'shoot': 30}, 'armor': {'body': 35, 'shield': 25}, 'dimension': 'discord:nether', 'wardrobe': {'1': 'discord:diamond_armor', '2': 'discord:obsidian_armor', '3': None}, 'pets': [['wolf', 'tiger']]}], ['652849205454569493', {'times': {'time_chop': 1597238907.0808995, 'time_mine': 1597281620.448202, 'time_hunt': 1597282422.7821376}, 'actions': {'chopping': False, 'mining': False, 'hunting': True}, 'material': {'discord:wood': 9519, 'discord:wood_planks': 43, 'discord:crafting_table': 1, 'discord:stick': 22, 'discord:stone': 531196, 'discord:iron': 6632, 'discord:diamond': 650, 'discord:obsidian': 87, 'discord:meat': 2097.9, 'discord:lava': 9, 'discord:rotten_flesh': 0, 'discord:bone': 0, 'discord:arrow': 0, 'discord:tnt': 0, 'discord:gunpowder': 0, 'discord:string': 2, 'discord:spider_eye': 0, 'discord:portal_table': 1, 'discord:netherite_scrap': 10, 'discord:netherite_ingot': 0, 'discord:magma_block': 1180, 'discord:blaze_rod': 0, 'discord:gold': 4, 'discord:nether_quartz': 2953, 'discord:netherrack': 118160, 'discord:nether_portal': 1, 'discord:blaze_powder': 0, 'discord:eye_of_ender': 0, 'discord:ender_pearl': 0, 'discord:emerald': 0, 'discord:first_5': 1, 'discord:national_flag_2020': 1, 'discord:medal_of_contribution': 1, 'discord:end_portal': 0, 'discord:end_stone': 0, 'discord:chorus_seed': 0, 'discord:chorus_fruit': 0, 'discord:gold_nugget': 53, 'discord:wool': 0, 'discord:bed': 0, 'discord:magma_cream': 1, 'discord:wood_nerd': 0, 'discord:stone_nerd': 0, 'discord:netherrack_nerd': 0, 'discord:dev_token': 0, 'discord:leather': 14}, 'tools': {'chop': 25, 'mine': 25, 'hunt': 25, 'shoot': 0}, 'armor': {'body': 35, 'shield': 25}, 'dimension': 'discord:nether', 'wardrobe': {'1': '', '2': 'discord:obsidian_armor', '3': 'discord:obsidian_armor'}}], ['702011697589911633', {'times': {'time_chop': 1597373942.0304701, 'time_mine': 1597371997.921528, 'time_hunt': 1597371997.9215283}, 'actions': {'chopping': True, 'mining': False, 'hunting': False}, 'material': {'discord:meat': 7.3, 'discord:crafting_table': 0, 'discord:stone': 0, 'discord:iron': 8, 'discord:diamond': 2, 'discord:obsidian': 0, 'discord:lava': 0, 'discord:rotten_flesh': 0, 'discord:bone': 0, 'discord:arrow': 0, 'discord:tnt': 2, 'discord:gunpowder': 0, 'discord:string': 0, 'discord:spider_eye': 0, 'discord:portal_table': 0, 'discord:netherite_scrap': 0, 'discord:netherite_ingot': 0, 'discord:magma_block': 0, 'discord:blaze_rod': 0, 'discord:gold': 0, 'discord:nether_quartz': 0, 'discord:netherrack': 0, 'discord:nether_portal': 0, 'discord:blaze_powder': 0, 'discord:eye_of_ender': 0, 'discord:ender_pearl': 0, 'discord:emerald': 0, 'discord:gold_nugget': 0, 'discord:wood': 192, 'discord:wood_planks': 0, 'discord:wool': 0, 'discord:stick': 0, 'discord:end_portal': 0, 'discord:magma_cream': 0, 'discord:bed': 0, 'discord:chorus_fruit': 0, 'discord:dev_token': 0, 'discord:end_stone': 0, 'discord:chorus_seed': 0, 'discord:leather': 0, 'discord:medal_of_contribution': 0, 'discord:national_flag_2020': 0, 'discord:first_5': 0, 'discord:wood_nerd': 0, 'discord:stone_nerd': 0, 'discord:netherrack_nerd': 0}, 'tools': {'chop': 1, 'mine': 0, 'hunt': 1, 'shoot': 0}, 'armor': {'body': None, 'shield': None}, 'wardrobe': {'1': None, '2': None, '3': None}, 'dimension': 'discord:overworld'}], ['711439467386241035', {'times': {'time_chop': 1596955782.6546967, 'time_mine': 1597573218.9613633, 'time_hunt': 1597373753.1717467, 'time_explore': 1597573511.7302575}, 'actions': {'chopping': False, 'mining': True, 'hunting': False, 'explore': False}, 'material': {'discord:wood': 17627, 'discord:wood_planks': 399, 'discord:crafting_table': 1, 'discord:stick': 12, 'discord:stone': 232579, 'discord:iron': 2996, 'discord:diamond': 219, 'discord:obsidian': 16, 'discord:meat': 39688.1, 'discord:lava': 0, 'discord:rotten_flesh': 26, 'discord:bone': 997, 'discord:arrow': 0, 'discord:tnt': 32, 'discord:gunpowder': 7, 'discord:string': 2, 'discord:spider_eye': 0, 'discord:portal_table': 0, 'discord:netherite_scrap': 1, 'discord:netherite_ingot': 0, 'discord:magma_block': 0, 'discord:blaze_rod': 0, 'discord:gold': 0, 'discord:nether_quartz': 0, 'discord:netherrack': 0, 'discord:nether_portal': 0, 'discord:blaze_powder': 0, 'discord:eye_of_ender': 0, 'discord:ender_pearl': 0, 'discord:emerald': 11, 'discord:national_flag_2020': 1, 'discord:medal_of_contribution': 0, 'discord:gold_nugget': 0, 'discord:wool': 0, 'discord:end_portal': 0, 'discord:magma_cream': 0, 'discord:bed': 0, 'discord:chorus_fruit': 0, 'discord:dev_token': 0, 'discord:end_stone': 0, 'discord:chorus_seed': 0, 'discord:leather': 3967, 'discord:first_5': 0, 'discord:wood_nerd': 0, 'discord:stone_nerd': 0, 'discord:netherrack_nerd': 0, 'discord:apple': 0, 'discord:enchanted_stick': 0}, 'tools': {'chop': 1, 'mine': 25, 'hunt': 25, 'shoot': 30}, 'armor': {'body': 15, 'shield': 25}, 'dimension': 'discord:overworld', 'wardrobe': {'1': '', '2': 'discord:iron_armor', '3': 'discord:diamond_armor'}, 'pets': []}]]


def findPlayer(player):
	for i in range(len(players)):
		if str(players[i][0]) == str(player):
			return i
	return "nil"

def addPlayer(name: str):
	global players
	players.append(
		[name, {
		'times': {}, 
		'actions': {}, 
		'material': {'14': 10}, 
		'tools': {'chop': 1, 'mine': 0, 'hunt': 1, 'shoot': 0},
		'armor': {'body': None, 'shield': None},
		'wardrobe': {'1': None, '2': None, '3': None},
		'dimension': 'discord:overworld',
		'pets': []
		}])


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
	global txt, msg, players, daytime


	if message.author == client.user or message.author.bot:
		return
	else:
		msg = word(message.content)
	
	if findPlayer(str(message.author.id)) != 'nil':
		entity = players[findPlayer(str(message.author.id))]

		# Auto update systems:

		if 'discord:wood' in entity[1]['material'].keys():
			entity[1]['materials_save'] = {}
			for material, count in entity[1]['material'].items():
				n = ''
				i = 1
				while n != material:
					n = ids.ids[str(i)]
					i += 1
				entity[1]['materials_save'][str(i - 1)] = count
			entity[1]['material'] = entity[1]['materials_save']
			entity[1].pop('materials_save')

		for material in mats:
			try:
				entity[1]['material'][material] += 0
			except KeyError:
				entity[1]['material'][material] = 0

		try:
			entity[1]['tools']['chop'] += 0
		except KeyError:
			entity[1]['tools'] = {'chop': 1, 'mine': 0, 'hunt': 1}
		
		try:
			entity[1]['tools']['shoot'] += 0
		except KeyError:
			entity[1]['tools']['shoot'] = 0
		
		try:
			entity[1]['pets']
		except KeyError:
			entity[1]['pets'] = []
		
		try:
			entity[1]['armor']
		except KeyError:
			entity[1]['armor'] = {'shield': 0, 'body': 0}
		
		try:
			entity[1]['wardrobe']
		except KeyError:
			entity[1]['wardrobe'] = {'1': None, '2': None, '3': None}
			if entity[1]['armor']['body'] != 0:
				armor = ""
				for armor_name, multiplier in loot_table.armor_multiplier.items():
					if entity[1]['armor']['body'] == multiplier:
						armor = armor_name
						break
				entity[1]['wardrobe']['1'] = armor
				
		
		try:
			entity[1]['dimension'] = entity[1]['dimension']
		except KeyError:
			entity[1]['dimension'] = 'discord:overworld'
		
		for action in acts:
			try:
				entity[1]['actions'][action[0]] = entity[1]['actions'][action[0]]
			except KeyError:
				entity[1]['actions'][action[0]] = False
				entity[1]['times'][action[1]] = time.time()


		# Game mechanics
		if daytime[1] - time.time() >= 3600:
			daytime[0] = not daytime[0]
		entity[1]['material']['14'] -= 0.1
		entity[1]['material']['14'] = round(entity[1]['material']['14'] * 10) / 10
		tf_boo = True


		if msg.word.lower() == str(default_call) + 'wardrobe':
			txt = 'Wardrobe:\n'
			for slot, armor in entity[1]['wardrobe'].items():
				if armor is None:
					txt += "\nSlot " + slot + ": Empty"
				else:
					txt += "\nSlot " + slot + ": " + armor
			ebd = discord.Embed(title="Wardrobe", description=txt, color=discord.Color.blue())
			ebd.set_author(name='DiscordMC')
			ebd.set_thumbnail(url=icon)
			ebd.set_footer(text='Do ' + default_call + 'equip <slot> to equip armor!')
			await message.channel.send(embed=ebd)
		
		if msg.word.lower().startswith(str(default_call) + "equip"):
			msg.clearfront(6 + len(default_call))
			try:
				armor = entity[1]['wardrobe'][msg.word]
				if armor is None:
					ebd = discord.Embed(title='Error 109', description='You don\'t have armor in slot ' + msg.word, color=discord.Color.red())
					ebd.set_author(name='DiscordMC')
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
				else:
					entity[1]['armor']['body'] = loot_table.armor_multiplier[entity[1]['wardrobe'][msg.word]]
					ebd = discord.Embed(title='Success!', description='You equipped a suit!', color=discord.Color.green())
					ebd.set_author(name='DiscordMC')
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
			except KeyError:
				ebd = discord.Embed(title='Error 108', description='Invalid wardrobe slot!', color=discord.Color.red())
				ebd.set_author(name='DiscordMC')
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)

		if msg.word.lower() == str(default_call) + "chop":
			if not entity[1]['actions']['chopping']:
				for i in entity[1]['actions']:
					entity[1]['actions'][str(i)] = False
				entity[1]['actions']['chopping'] = True
				entity[1]['times']['time_chop'] = time.time()
				ebd = discord.Embed(title="Actions", description="You started chopping wood!", color=discord.Color.blue())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			else:
				ebd = discord.Embed(title="Actions", description="You are already chopping wood!", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
		
		elif msg.word.lower() == str(default_call) + "mine":
			if not entity[1]['actions']['mining']:
				for i in entity[1]['actions']:
					entity[1]['actions'][str(i)] = False
				entity[1]['actions']['mining'] = True
				entity[1]['times']['time_mine'] = time.time()
				ebd = discord.Embed(title="Actions", description="You started mining!", color=discord.Color.blue())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			else:
				ebd = discord.Embed(title="Actions", description="You are already mining!", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
		
		elif msg.word.lower() == str(default_call) + "hunt":
			if not entity[1]['actions']['hunting']:
				for i in entity[1]['actions']:
					entity[1]['actions'][str(i)] = False
				entity[1]['actions']['hunting'] = True
				entity[1]['times']['time_hunt'] = time.time()
				ebd = discord.Embed(title="Actions", description="You started hunting!", color=discord.Color.blue())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			else:
				ebd = discord.Embed(title="Actions", description="You are already hunting!", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
		
		elif msg.word.lower() == str(default_call) + "collect_wood":
			if entity[1]['actions']['chopping']:
				txt = round((time.time() - entity[1]['times']['time_chop']) / 10)
				entity[1]['times']['time_chop'] = time.time()
				entity[1]['material']['1'] += round(txt * entity[1]['tools']['chop'])
				ebd = discord.Embed(title="Collect Wood", description="You chopped " + str(txt) + " wood!", color=discord.Color.blue())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			else:
				ebd = discord.Embed(title="Error 100-0", description="You are not chopping wood!", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)

		elif msg.word.lower() == str(default_call) + "collect_hunting":
			if entity[1]['actions']['hunting']:
				delay = round((time.time() - entity[1]['times']['time_hunt']) / 25)
				if 'Direct Message' not in str(message.channel):
					if message.guild.id == 735427369287811082:
						delay *= 1.1
				txt = "Result from your hunting session:"
				for item, multiplier in loot_table.hunting_loot[entity[1]['dimension']].items():
					entity[1]['material'][item] += math.floor(multiplier * delay)
					if math.floor(multiplier * delay) > 0:
						txt += "\nYou got {} {}!".format(math.floor(multiplier * delay), ids.ids[item])
				if 'Direct Message' not in str(message.channel):
					if message.guild.id == 735427369287811082:
						txt += "\n\nYou got 10% more items from collecting in our official server!"
				entity[1]['times']['time_hunt'] = time.time()
				ebd = discord.Embed(title="Collect Hunting", description=txt, color=discord.Color.blue())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			else:
				ebd = discord.Embed(title="Error 100-2", description="You are not hunting!", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
		
		elif msg.word.lower().startswith(str(default_call) + 'warp'):
			msg.clearfront(5 + len(default_call))
			if msg.word in portals.warps.keys():
				info = portals.warps[msg.word]
				if entity[1]['material'][info[0]] < 1:
					ebd = discord.Embed(title="Error 105", description="You don't have this portal!", color=discord.Color.red())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
				else:
					if entity[1]['dimension'] == info[1]:
						ebd = discord.Embed(title="Warning 203", description="You are already in this dimension!", color=discord.Color.orange())
						ebd.set_author(name="DiscordMC")
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
					else:
						if random.randint(1, 20) != 1:
							for timer in entity[1]['times'].keys():
								entity[1]['times'][timer] = time.time()
							entity[1]['dimension'] = info[1]
							ebd = discord.Embed(title="Success!", description="Warped to " + info[1] + "!", color=discord.Color.green())
							ebd.set_author(name="DiscordMC")
							ebd.set_thumbnail(url=icon)
							await message.channel.send(embed=ebd)
						else:
							entity[1]['material'][info[0]] -= 1
							if entity[1]['material'][info[0]] < 1:
								ebd = discord.Embed(title='Oh no!', description="Your portal broke!", color=discord.Color.orange())
								ebd.set_author(name='DiscordMC')
								ebd.set_thumbnail(name=icon)
								await message.channel.send(embed=ebd)
							else:
								for timer in entity[1]['times'].keys():
									entity[1]['times'][timer] = time.time()
								entity[1]['dimension'] = info[1]
								ebd = discord.Embed(title="Success!", description="Your portal broke so you used another of your portal to warp to " + info[1] + "!", color=discord.Color.green())
								ebd.set_author(name="DiscordMC")
								ebd.set_thumbnail(url=icon)
								await message.channel.send(embed=ebd)
			else:
				if msg.word == 'overworld':
					if entity[1]['dimension'] == 'discord:overworld':
						ebd = discord.Embed(title="Warning 203", description="You are already in this dimension!", color=discord.Color.orange())
						ebd.set_author(name="DiscordMC")
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
					else:
						entity[1]['dimension'] = 'discord:overworld'
						ebd = discord.Embed(title="Success!", description="Warped to discord:overworld!", color=discord.Color.green())
						ebd.set_author(name="DiscordMC")
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
				else:
					ebd = discord.Embed(title="Error 106", description="Invalid dimension!", color=discord.Color.red())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)

		elif msg.word.lower() == str(default_call) + 'dimension':
			txt = 'Current Dimension: ' + entity[1]['dimension']
			extraPortals = False
			for portal in tags.Requires_portal_table:
				if entity[1]['material'][portal] > 0:
					if not extraPortals:
						txt += '\n\nPortals:'
						extraPortals = True
					txt += '\n' + portal
			if not extraPortals:
				txt += '\n\nYou don\'t have any portals!'
			ebd = discord.Embed(title='Portals and Dimensions', description=txt, color=discord.Color.gold())
			ebd.set_author(name='DiscordMC')
			ebd.set_thumbnail(url=icon)
			ebd.set_footer(text='Use ' + default_call + 'warp <dimension> to warp!')
			await message.channel.send(embed=ebd)

		elif msg.word.lower() == str(default_call) + "collect_mining":
			if entity[1]['actions']['mining']:
				txt = "Results from your mining session:\n"
				mining_delay = round(time.time() - entity[1]['times']['time_mine'])
				if'Direct Message' not in str(message.channel):
					if message.guild.id == 735427369287811082:
						mining_delay = mining_delay * 1.1
				for mineral, info in loot_table.mining_loot[entity[1]['dimension']].items():
					count = math.floor(mining_delay * entity[1]['tools']['mine'] * info[0] / 100)
					if entity[1]['tools']['mine'] >= info[1] and count > 0:
						entity[1]['material'][mineral] += count
						txt += '\nYou collected ' + str(count) + " " + ids.ids[mineral] + '!'
				entity[1]['times']['time_mine'] = time.time()
				
				for name, info in loot_table.mining_rare_drop[entity[1]['dimension']].items():
					c = 0
					if entity[1]['tools']['mine'] >= info[2]:
						if mining_delay >= info[1]:
							for n in range(round(mining_delay // info[1])):
								if random.randint(1, loot_table.getChance(info[0])) == 1:
									c += 1
							if c >= 1:
								txt += "\nRARE DROP! You got " + str(c) + " " + ids.ids[name] + "!"
								entity[1]['material'][name] += c

				if entity[1]['tools']['mine'] < loot_table.pickaxe_multiplier['discord:wooden_pickaxe']:
					ebd = discord.Embed(title="Error 102-0", description="You don't have a pickaxe!", color=discord.Color.red())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
				else:
					if message.guild.id == 735427369287811082:
						txt += '\n\nYou get 10% more items because you collected in our official server!'
					ebd = discord.Embed(title="Collect Mining", description=txt, color=discord.Color.blue())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
			else:
				ebd = discord.Embed(title="Error 100-1", description="You are not mining!", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
		
		elif str(msg.word.lower()).startswith(str(default_call) + "info"):
			msg.clearfront(5 + len(default_call))
			if 'discord:' + msg.word.lower() not in descriptions.descriptions.keys():
				ebd = discord.Embed(title="Error 107", description="Description not found!", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			else:
				ebd = discord.Embed(title="Info for " + msg.word, description=descriptions.descriptions['discord:' + msg.word], color=discord.Color.blue())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				ebd.set_footer(text="If you are looking for the recipe of the item, you can use " + default_call + "viewrecipe <recipe>.")
				await message.channel.send(embed=ebd)

		elif str(msg.word.lower()).startswith(str(default_call) + "viewrecipe"):
			msg.clearfront(11 + len(default_call))
			if msg.word.lower() not in crafting.crafts.keys():
				ebd = discord.Embed(title="Error 104-0", description="Invalid Crafting Recipe!", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
				return
			else:
				recipe = crafting.crafts[msg.word.lower()]
				txt = ''
				for n in range(len(recipe) - 1):
					txt += '\n' + str(recipe[n][1]) + ' ' + str(recipe[n][0])
				if type(recipe[-1]) is not str:
					txt += '\n\n**Output:**\n' + str(recipe[-1][1]) + ' ' + str(recipe[-1][0])
				else:
					txt += '\n\n**Output:**\n' + msg.word.lower()
				ebd = discord.Embed(title='Recipe for ' + msg.word.lower(), description=txt, color=discord.Color.gold())
				ebd.set_author(name='DiscordMC')
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)

		elif msg.word.lower() == str(default_call) + "hotbar":
			txt = ""
			for name, multiplier in loot_table.foraging_multiplier.items():
				if entity[1]['tools']['chop'] == multiplier:
					txt += "Axe: **" + str(name) + "**"
			for name, multiplier in loot_table.pickaxe_multiplier.items():
				if entity[1]['tools']['mine'] == multiplier:
					if txt != '':
						txt += ',\n'
					txt += "Pickaxe: **" + str(name) + "**"
			for name, multiplier in loot_table.sword_multiplier.items():
				if entity[1]['tools']['hunt'] == multiplier:
					if txt != '':
						txt += ',\n'
					txt += "Sword: **" + str(name) + "**"
			for name, multiplier in loot_table.armor_multiplier.items():
				if entity[1]['armor']['body'] == multiplier:
					if txt != '':
						txt += ',\n'
					txt += "Armor: **" + str(name) + "**"
			for name, multiplier in loot_table.shield_multiplier.items():
				if entity[1]['armor']['shield'] == multiplier:
					if txt != '':
						txt += ',\n'
					txt += "Shield: **" + str(name) + "**"
			for name, multiplier in loot_table.bow_multiplier.items():
				if entity[1]['tools']['shoot'] == multiplier:
					if txt != '':
						txt += ',\n'
					txt += "Bow: **" + str(name) + "**"

			if txt != "":
				ebd = discord.Embed(title="Hotbar", description=("Name: {}\n\n{}".format(str(message.author.mention), str(txt))), color=discord.Color.blue())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			else:
				ebd = discord.Embed(title="Hotbar", description="Name: {}\n\n{}".format("<@!" + str(msg.word) + ">", "You have no items in your hand currently!"), color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
		
		elif msg.word.startswith(str(default_call) + "hotbar "):
			txt = ""
			msg.clearfront(7 + len(default_call))
			if findPlayer(str(msg.word)) != 'nil':
				entity = players[findPlayer(str(msg.word))]
				for name, multiplier in loot_table.foraging_multiplier.items():
					if entity[1]['tools']['chop'] == multiplier:
						txt += "Axe: **" + str(name) + "**"
				for name, multiplier in loot_table.pickaxe_multiplier.items():
					if entity[1]['tools']['mine'] == multiplier:
						if txt != '':
							txt += ',\n'
						txt += "Pickaxe: **" + str(name) + "**"
				for name, multiplier in loot_table.sword_multiplier.items():
					if entity[1]['tools']['hunt'] == multiplier:
						if txt != '':
							txt += ',\n'
						txt += "Sword: **" + str(name) + "**"
				for name, multiplier in loot_table.armor_multiplier.items():
					if entity[1]['armor']['body'] == multiplier:
						if txt != '':
							txt += ',\n'
						txt += "Armor: **" + str(name) + "**"
				for name, multiplier in loot_table.shield_multiplier.items():
					if entity[1]['armor']['shield'] == multiplier:
						if txt != '':
							txt += ',\n'
						txt += "Shield: **" + str(name) + "**"
				for name, multiplier in loot_table.bow_multiplier.items():
					if entity[1]['tools']['shoot'] == multiplier:
						if txt != '':
							txt += ',\n'
						txt += "Bow: **" + str(name) + "**"

				if txt != "":
					ebd = discord.Embed(title="Hotbar", description="Name: {}\n\n{}".format("<@!" + str(msg.word) + ">", str(txt)), color=discord.Color.blue())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
				else:
					ebd = discord.Embed(title="Hotbar", description="Name: {}\n{}".format("<@!" + str(msg.word) + ">", "You have no items ni your hand currently!"), color=discord.Color.red())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
			else:
				ebd = discord.Embed(title="Error 101", description="That person does not play DiscordMC! Go invite them to play DiscordMC!", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			return

		elif msg.word.lower() == str(default_call) + "inv":
			msg.clearfront(4 + len(default_call))
			txt = "**Name**: " + str(message.author.mention) + "\n\nMaterials:"
			c = 0
			special = []
			for x, y in entity[1]['material'].items():
				if y > 0:
					if x not in special_items:
						if c < 10:
							txt += "\n" + ids.ids[x] + " **[ID: " + x + "]** => " + str(y)
						c += 1
					else:
						special.append(ids.ids[x] + " **[Special]**")
			if len(special) != 0:
				txt += "\n\n"
				for special_item in special:
					txt += "\n" + special_item
			ebd = discord.Embed(title="Inventory", description=str(txt), color=discord.Color.blue())
			ebd.set_author(name="DiscordMC")
			ebd.set_thumbnail(url=icon)
			if c > 10:
				ebd.set_footer(text = "Page 1 of {}".format(str(math.ceil(c / 10))))
			await message.channel.send(embed=ebd)
		
		elif msg.word.startswith(str(default_call) + "inv "):
			msg.clearfront(4 + len(default_call))
			if findPlayer(msg.word) != 'nil':
				txt =	"**Name:** <@!" + str(msg.word) + ">\n\nMaterials:"
				special = []
				for x, y in players[findPlayer(msg.word)][1]['material'].items():
					if y > 0:
						if x not in special_items:
							txt += "\n" + ids.ids[x] + " **[ID: " + x + "]** => " + str(y)
						else:
							special.append(ids.ids[x] + " **[Special]**")
				if len(special) != 0:
					txt += "\n\n"
					for special_item in special:
						txt += "\n" + special_item
				ebd = discord.Embed(title="Inventory", description=str(txt), color=discord.Color.blue())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			else:
				if int(msg.word) < 10 ** 18:
					txt =	"**Name:** " + str(message.author.mention) + "\n\nMaterials:"
					special = []
					c = 0
					for x, y in entity[1]['material'].items():
						if y > 0:
							if x not in special_items:
								if int(msg.word) * 10 > c > int(msg.word) * 10 - 11:
									txt += "\n" + ids.ids[x] + " **[ID: " + x + "]** => " + str(y)
								c += 1
							else:
								special.append(ids.ids[x] + " **[Special]**")
					if len(special) != 0:
						txt += "\n\n"
						for special_item in special:
							txt += "\n" + special_item
					if int(msg.word) > math.ceil(c / 10):
						ebd = discord.Embed(title="Error 110", description="Invalid page! There is only {} pages!".format(str(math.ceil(c / 10))), color=discord.Color.red())
						ebd.set_author(name="DiscordMC")
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
					elif int(msg.word) < 1:
						ebd = discord.Embed(title="Error 110", description="Invalid page!".format(str(math.ceil(c / 10))), color=discord.Color.red())
						ebd.set_author(name="DiscordMC")
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
					else:
						ebd = discord.Embed(title="Inventory Page {}".format(msg.word), description=str(txt), color=discord.Color.blue())
						ebd.set_author(name="DiscordMC")
						ebd.set_thumbnail(url=icon)
						ebd.set_footer(text = "Page {} of {}".format(msg.word, str(math.ceil(c / 10))))
						await message.channel.send(embed=ebd)
				else:
					ebd = discord.Embed(title="Error 101", description="That person does not play DiscordMC! Go invite them to play DiscordMC!", color=discord.Color.red())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
		
		elif msg.startswith(str(default_call) + "modKick "):
			if str(message.author.id) in auth:
				msg.clearfront(8 + len(default_call))
				try:
					players.pop(findPlayer(msg.word))
					ebd = discord.Embed(title="ModKick", description="You modKicked " + str(msg.word), color=discord.Color.green())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
				except:
					ebd = discord.Embed(title="Error 101", description="Who is that??", color=discord.Color.red())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
				
				with open('players.txt', 'w') as data:
					data.write(str(players))
				return
			else:
				ebd = discord.Embed(title="Error 103", description="Not Authorised", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
		
		elif msg.startswith(str(default_call) + "craft "):
			msg.clearfront(6 + len(default_call))
			try:
				toCraft, count = msg.word.split(", ", 2)
				recipe = crafting.getRecipe(toCraft)
				recipeOutput = recipe[-1]
				if type(recipeOutput) is not str:
					try:
						if not (int(count) / recipeOutput[1]).is_integer():
							raise TypeError
						if int(count) <= 0:
							raise TypeError
					except TypeError:
						ebd = discord.Embed(title="Error 104-3", description="Please enter a valid amount!", color=discord.Color.red())
						ebd.set_author(name="DiscordMC")
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
						return
				if recipe == 'nil':
					ebd = discord.Embed(title="Error 104-0", description="Invalid Crafting Recipe!", color=discord.Color.red())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
					return
				if 'discord:' + toCraft in tags.Requires_crafting_table:
					if entity[1]['material']['3'] < 1:
						ebd = discord.Embed(title="Error 104-2a", description="You need a Crafting Table to craft this Recipe!", color=discord.Color.red())
						ebd.set_author(name="DiscordMC")
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
						return
				elif 'discord:' + toCraft in tags.Requires_portal_table:
					if entity[1]['material']['18'] < 1:
						ebd = discord.Embed(title="Error 104-2b", description="You need a Portal Table to craft this Recipe!", color=discord.Color.red())
						ebd.set_author(name="DiscordMC")
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
						return
				if not crafting.checkItem(entity, recipe, count):
					ebd = discord.Embed(title="Error 104-2", description="Not Enough Items!", color=discord.Color.red())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
					return

				for item in recipe:
					if len(recipe) - recipe.index(item) == 1:
						if not type(crafting.crafts[toCraft][-1]) is str:
							entity[1]['material'][crafting.getItem(recipeOutput[0])] += int(int(count) * recipeOutput[1] / crafting.crafts[toCraft][-1][1])
						else:
							output = word(recipeOutput)
							if output.startswith("pm"):
								output.clearfront(2)
								if entity[1]['tools']['mine'] < int(output.word):
									entity[1]['tools']['mine'] = int(output.word)
								else:
									ebd = discord.Embed(title="Bruh.", description="You already have a pickaxe of that tier or higher, so you yeeted the new one into the river.", color=discord.Color.orange())
									ebd.set_author(name="DiscordMC")
									ebd.set_thumbnail(url=icon)
									await message.channel.send(embed=ebd)

							elif output.startswith("am"):
								output.clearfront(2)
								if entity[1]['tools']['chop'] < int(output.word):
									entity[1]['tools']['chop'] = int(output.word)
								else:
									ebd = discord.Embed(title="Bruh.", description="You already have a axe of that tier or higher, so you yeeted the new one into the river.", color=discord.Color.orange())
									ebd.set_author(name="DiscordMC")
									ebd.set_thumbnail(url=icon)
									await message.channel.send(embed=ebd)

							elif output.startswith("sm"):
								output.clearfront(2)
								if entity[1]['tools']['hunt'] < int(output.word):
									entity[1]['tools']['hunt'] = int(output.word)
								else:
									ebd = discord.Embed(title="Bruh.", description="You already have a sword of that tier or higher, so you yeeted the new one into the river.", color=discord.Color.orange())
									ebd.set_author(name="DiscordMC")
									ebd.set_thumbnail(url=icon)
									await message.channel.send(embed=ebd)		 

							elif output.startswith("armor"):
								output.clearfront(5)
								found = False
								for n in range(int(count)):
									for slot in entity[1]['wardrobe'].keys():
										if entity[1]['wardrobe'][slot] is None:
											entity[1]['wardrobe'][slot] = 'discord:' + toCraft
											found = True
											break
									if not found:
										entity[1]['wardrobe']['1'] = 'discord:' + toCraft
										ebd = discord.Embed(title='Bruh.', description="You do not have a free slot in your wardrobe, so the armor in your first slot got yeeted into the river.", color=discord.Color.orange())
										ebd.set_author(name='DiscordMC')
										ebd.set_thumbnail(url=icon)
										await message.channel.send(embed=ebd)

							elif output.startswith("shield"):
								output.clearfront(6)
								if entity[1]['armor']['shield'] is not None:
									if entity[1]['armor']['shield'] < int(output.word):
										entity[1]['armor']['shield'] = int(output.word)
									else:
										ebd = discord.Embed(title="Bruh.", description="You already have a shield of that tier or higher, so you yeeted the new one into the river.", color=discord.Color.orange())
										ebd.set_author(name="DiscordMC")
										ebd.set_thumbnail(url=icon)
										await message.channel.send(embed=ebd)
								else:
									entity[1]['armor']['shield'] = int(output.word)

							elif output.startswith("bow"):
								output.clearfront(3)
								if entity[1]['tools']['shoot'] < int(output.word):
									entity[1]['tools']['shoot'] = int(output.word)
								else:
									ebd = discord.Embed(title="Bruh.", description="You already have a bow of that tier or higher, so you yeeted the new one into the river.", color=discord.Color.orange())
									ebd.set_author(name="DiscordMC")
									ebd.set_thumbnail(url=icon)
									await message.channel.send(embed=ebd)
					else:
						print(crafting.crafts[toCraft])
						if not type(crafting.crafts[toCraft][-1]) is str:
							entity[1]['material'][crafting.getItem(item[0])] -= int(item[1] * int(count) / crafting.crafts[toCraft][-1][1])
						else:
							entity[1]['material'][crafting.getItem(item[0])] -= int(item[1] * int(count))
				
				ebd = discord.Embed(title="Success!", description="Crafted " + str(count) + " " + toCraft + "!", color=discord.Color.green())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)

			except ValueError:
				ebd = discord.Embed(title="Error 104-3", description="Please enter a valid amount!", color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			

		elif msg.word.lower() == str(default_call) + "leave":
			players.pop(findPlayer(str(message.author.id)))
			ebd = discord.Embed(title="Aww...", description="You left discordMC. Guess people will start calling you a coward from now on then >:)", color=discord.Color.orange)
			ebd.set_author(name="DiscordMC")
			ebd.set_thumbnail(url=icon)
			await message.channel.send(embed=ebd)
			
			with open('players.txt', 'w') as data:
				data.write(str(players))
			return

		elif msg.word.lower() == str(default_call) + "help":
			await message.delete()
			await message.channel.send(history.commands)
		
		elif msg.word.lower() == str(default_call) + "versions":
			try:
				await message.delete()
			except discord.errors.Forbidden:
				pass
			for version in history.versions:
				await message.channel.send(version)
		
		elif msg.word.lower().startswith(str(default_call) + "give"):
			if str(message.author.id) not in auth:
				ebd = discord.Embed(title='Error 103', description='Not Authorised!', color=discord.Color.red())
				ebd.set_author(name='DiscordMC')
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			else:
				msg.clearfront(5 + len(default_call))
				try:
					person, item, count = msg.word.split(', ', 3)
					try:
						count = int(count)
					except TypeError:
						ebd = discord.Embed(title="Error 300", description="Invalid syntax!", color=discord.Color.red())
						ebd.set_author(name='DiscordMC')
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
						return
					if findPlayer(person) != 'nil':
						person_entity = players[findPlayer(person)]
						for material in mats:
							try:
								person_entity[1]['material'][material] += 0
							except KeyError:
								person_entity[1]['material'][material] = 0

						try:
							person_entity[1]['tools']['chop'] += 0
						except KeyError:
							person_entity[1]['tools'] = {'chop': 1, 'mine': 0, 'hunt': 1}
						
						try:
							person_entity[1]['tools']['shoot'] += 0
						except KeyError:
							person_entity[1]['tools']['shoot'] = 0
						
						try:
							person_entity[1]['armor']
						except KeyError:
							person_entity[1]['armor'] = {'shield': 0, 'body': 0}
						
						try:
							person_entity[1]['dimension'] = entity[1]['dimension']
						except KeyError:
							person_entity[1]['dimension'] = 'discord:overworld'
						
						for action in acts:
							try:
								person_entity[1]['actions'][action[0]] = entity[1]['actions'][action[0]]
							except KeyError:
								person_entity[1]['actions'][action[0]] = False
								person_entity[1]['times'][action[1]] = time.time()
						try:
							person_entity[1]['material']['discord:' + item] += count
							ebd = discord.Embed(title='Success!', description='Successfully gave <@!' + person + '> ' + str(count) + ' ' + item, color=discord.Color.green())
							ebd.set_author(name='DiscordMC')
							ebd.set_thumbnail(url=icon)
							await message.channel.send(embed=ebd)
						except KeyError:
							try:
								person_entity[1]['tools'][item] = count
								ebd = discord.Embed(title='Success!', description='Successfully gave <@!' + person + '> ' + item + ' multiplier of ' + str(count), color=discord.Color.green())
								ebd.set_author(name='DiscordMC')
								ebd.set_thumbnail(url=icon)
								await message.channel.send(embed=ebd)
							except KeyError:
								try:
									person_entity[1]['armor'][item] = count
									ebd = discord.Embed(title='Success!', description='Successfully gave ' + person + ' ' + item + ' multiplier of ' + str(count), color=discord.Color.green())
									ebd.set_author(name='DiscordMC')
									ebd.set_thumbnail(url=icon)
									await message.channel.send(embed=ebd)
								except KeyError:
									ebd = discord.Embed(title='Error 301', description='Invalid Item!', color=discord.Color.red())
									ebd.set_author(name='DiscordMC')
									ebd.set_thumbnail(url=icon)
									await message.channel.send(embed=ebd)
					else:
						ebd = discord.Embed(title='Error 101', description='Player does not play DiscordMC.', color=discord.Color.red())
						ebd.set_author(name='DiscordMC')
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
				except ValueError:
					ebd = discord.Embed(title="Error 300", description="Invalid syntax!", color=discord.Color.red())
					ebd.set_author(name='DiscordMC')
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)

		elif msg.word.lower().startswith(str(default_call) + "convert_to_roman"):
			msg.clearfront(17 + len(default_call))
			await message.channel.send('```' + tools.convert_to_roman(int(msg.word)) + '```')

		elif msg.word.lower().startswith(str(default_call) + "convert_to_integer"):
			msg.clearfront(19 + len(default_call))
			await message.channel.send('```' + str(tools.convert_to_integer(msg.word)) + '```')

		elif msg.word.lower() == str(default_call) + "explore":
			base = 10000000000000
			if time.time() - entity[1]['times']['time_explore'] < explore_delay:
				ebd = discord.Embed(title="Please try again later.", description="There is a {} second cooldown!".format(explore_delay), color=discord.Color.red())
				ebd.set_author(name='DiscordMC')
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
				return
			entity[1]['times']['time_explore'] = time.time()
			structure_found = float(random.randint(1, base) / (base / 100))
			structure = None
			chance_covered = 0
			for structure_lt, chance in loot_table.structure_chance[entity[1]['dimension']].items():
				chance_covered += chance
				if structure_found <= chance_covered:
					structure = structure_lt
					break
			if structure is not None:
				defense = 1
				if entity[1]['armor']['body'] is not None:
					defense = entity[1]['armor']['body']
				if random.randint(1, 100 * defense) <= loot_table.structure_deaths[structure][0]:
					ebd = discord.Embed(title="Oh No!", description=str(message.author.mention) + ", you " + loot_table.structure_deaths[structure][1])
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
					players.pop(findPlayer(str(message.author.id)))
					addPlayer(str(message.author.id))
				else:
					text = ""
					for item in loot_table.structure_loot[structure]:
						count = random.randint(item[2], item[3])
						if item[0] == "discord:crossbow":
							if entity[1]['tools']['shoot'] >= loot_table.bow_multiplier['discord:crossbow']:
								ebd = discord.Embed(title="Aww man", description="You already have a bow of this tier or higher, so you yeeted the new one into the river.", color=discord.Color.orange())
								ebd.set_author(name="DiscordMC")
								ebd.set_thumbnail(url=icon)
								await message.channel.send(embed=ebd)
							else:
								entity[1]['tools']['shoot'] = loot_table.bow_multiplier['discord:crossbow']
						else:
							entity[1]['material'][crafting.getItem(item[0])] += count
						text += str(message.author.mention) + ", you found " + str(count) + " " + item[0] + "!\n"
					if text != "":
						ebd = discord.Embed(title="Loot", description=text, color=discord.Color.blue())
						ebd.set_author(name="DiscordMC")
						ebd.set_thumbnail(url=icon)
						await message.channel.send(embed=ebd)
			else:
				for pet in pets.chances:
					if random.randint(1, base) / (base / 100) <= pet[1]:
						entity[1]["pets"].append(pets.pets[str(pet[0])])
				ebd = discord.Embed(title="Please try again later.", description=str(message.author.mention) + ", you didn\'t find a structure or a pet!", color=discord.Color.orange())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)

		else:
			tf_boo = False
			entity[1]['material']['14'] += 0.1
			entity[1]['material']['14'] = round(entity[1]['material']['14'] * 10) / 10
		
		if entity[1]['material']['14'] < 3 and tf_boo:
			ebd = discord.Embed(title="Warning 200-0", description="You are running low on food!", color=discord.Color.orange())
			ebd.set_author(name="DiscordMC")
			ebd.set_thumbnail(url=icon)
			await message.channel.send(embed=ebd)
		elif entity[1]['material']['14'] < 1 and tf_boo:
			ebd = discord.Embed(title="Warning 200-0", description="You are running extremely low on food!", color=discord.Color.orange())
			ebd.set_author(name="DiscordMC")
			ebd.set_thumbnail(url=icon)
			await message.channel.send(embed=ebd)
		elif entity[1]['material']['14'] <= 0:
			players.pop(findPlayer(str(message.author.id)))
			addPlayer(str(message.author.id))
			with open('players.txt', 'w') as data:
					data.write(str(players))
			ebd = discord.Embed(title="Uh Oh!", description="You ran out of food and died!", color=discord.Color.red())
			ebd.set_author(name="DiscordMC")
			ebd.set_thumbnail(url=icon)
			await message.channel.send(embed=ebd)
			return

		if entity[1]['tools']['hunt'] >= int(min(loot_table.sword_multiplier.values())):
			if entity[1]['armor']['body'] is not None:
				player_strength = entity[1]['tools']['hunt'] * entity[1]['armor']['body']
			else:
				player_strength = entity[1]['tools']['hunt']
			if entity[1]['tools']['shoot'] >= int(min(loot_table.bow_multiplier.values())):
				player_strength *= (entity[1]['tools']['shoot'])
			monster_strength = 0
			mobs = {}
			txt = ""
			for monster, info in loot_table.combat_loot[entity[1]['dimension']].items():
				if monster != 'discord:magma_cube':
					stat = loot_table.mob_stats[monster]
				else:
					stat = random.choice(loot_table.magma_cube)
					
				if random.randint(1, 1000) <= stat[0]:
					mob_strength = random.randint(stat[1], stat[2]) * round(math.sqrt(player_strength))
					if monster in tags.Undead and entity[1]['tools']['hunt'] == loot_table.sword_multiplier['discord:undead_sword']:
						mob_strength /= 2.5
					if monster in tags.Undead and entity[1]['tools']['shoot'] == loot_table.bow_multiplier['discord:undead_bow']:
						mob_strength /= 1.5
					monster_strength += mob_strength
					if monster not in mobs.keys():
						mobs[monster] = 1
					else:
						mobs[monster] += 1
			for monster, count in mobs.items():
				txt += "```" + monster + ": " + str(count) + "```"
			if txt != "":
				ebd = discord.Embed(title="Uh Oh!", description=str(message.author.mention) + ", you found: " + txt, color=discord.Color.orange())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
				if player_strength >= mob_strength:
					ebd = discord.Embed(title="Monster Hunter!", description="You defeated the monsters!", color=discord.Color.green())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
					for monster, count in mobs.items():
						drops = loot_table.combat_loot[entity[1]['dimension']][monster]
						for n in range(count):
							for drop_name, drop_info in drops.items():
								if random.randint(1, 100) <= drop_info[2]:
									if drop_name != "discord:bow":
										entity[1]['material'][drop_name] += random.randint(drop_info[0], drop_info[1])
									else:
										if entity[1]['tools']['shoot'] >= loot_table.bow_multiplier['discord:bow']:
											ebd = discord.Embed(title="Aww man", description="You already have a bow of this tier or higher, so you yeeted the new one into the river.", color=discord.Color.orange())
											ebd.set_author(name="DiscordMC")
											ebd.set_thumbnail(url=icon)
											await message.channel.send(embed=ebd)
										else:
											entity[1]['tools']['shoot'] = loot_table.bow_multiplier['discord:bow']
											ebd = discord.Embed(title="RARE DROP", description="Bow! (" + str(loot_table.combat_loot['discord:skeleton']['discord:bow'][2]) + "% Chance)", color=discord.Color.green())
											ebd.set_author(name="DiscordMC")
											ebd.set_thumbnail(url=icon)
											await message.channel.send(embed=ebd)
				else:
					ebd = discord.Embed(title="R.I.P.", description="You were killed by monsters!", color=discord.Color.blurple())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					with open("players.txt", 'w') as data:
						data.write(str(players))
					data.close()
					with open("timecycle.txt", 'w') as data2:
						data2.write(str(daytime))
					data2.close()
					players.pop(findPlayer(str(message.author.id)))
					addPlayer(str(message.author.id))
					await message.channel.send(embed=ebd)
					
		
		if str(message.content) == str(default_call) + "sleep":
			if entity[1]['material']['37'] > 0:
				if entity[1]['dimension'] not in tags.Bed_explode_dimensions:
					await message.channel.send("📢**ANNOUNCEMENT EVERYONE!!! {} IS GOING TO SLEEP 😴! LETS ALL** *`KEEP VERY QUIET`*".format(str(message.author.mention)))
				else:
					ebd = discord.Embed(title="BOOM", description="You were killed by [Intentional Game Design]", color=discord.Color.blurple())
					ebd.set_author(name="DiscordMC")
					ebd.set_thumbnail(url=icon)
					await message.channel.send(embed=ebd)
					players.pop(findPlayer(str(message.author.id)))
					addPlayer(str(message.author.id))
			else:
				ebd = discord.Embed(title="Error", description="{}, you cannot sleep on the floor!".format(str(message.author.mention)), color=discord.Color.red())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)

		players[findPlayer(str(message.author.id))] = entity
	else:
		if msg.word.lower() == str(default_call) + "start":
			if findPlayer(str(message.author.id)) == 'nil':
				addPlayer(str(message.author.id))
				ebd = discord.Embed(title="Welcome!", description="You successfully created your account, " + str(message.author.mention) + "!", color=discord.Color.green())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			else:
				ebd = discord.Embed(title="Bruh.", description=str(message.author.mention) + ", you already have an account.", color=discord.Color.orange())
				ebd.set_author(name="DiscordMC")
				ebd.set_thumbnail(url=icon)
				await message.channel.send(embed=ebd)
			return
		return
	
	with open("players.txt", 'w') as data:
		data.write(str(players))
	data.close()
	with open("timecycle.txt", 'w') as data2:
		data2.write(str(daytime))
	data2.close()

client.run(token)

txt.close() 
