


import os
import operator

class  EntityTag(object):
	
	def __init__(self, tag=None, start=None, end=None, content=None):
		super( EntityTag, self).__init__()
		self.tag = tag
		self.start = start
		self.end = end
		self.content = content

	def __repr__(self):
		return str((self.tag, self.start, self.end))
	def __str__(self):
		return str((self.tag, self.start, self.end))


class Relation(object):
	
	def __init__(self, unit=None, ingredient=None, amount=None):
		super(Relation, self).__init__()
		self.unit = unit
		self.ingredient = ingredient
		self.amount = amount

	def __repr__(self):
		tmp = ""
""	""	""i""f"" ""s""e""l""f"".""a""m""o""u""n""t"":""
""	""	""	""t""m""p"" ""="" ""t""m""p"" ""+"" ""s""e""l""f"".""a""m""o""u""n""t""+