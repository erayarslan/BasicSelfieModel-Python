class Instagram(object):
	def __init__(self, gender):
		self.barzoCount = 50

		self.gender = gender
		self.areYouFamous = False
		self.like = 0

	def setAreYouFamous(self, areYouFamous):
		self.areYouFamous = areYouFamous

	def profile(self):
		return "sexy" if self.areYouFamous else "barzo"

class Selfie(Instagram):
	def __init__(self, gender):
		Instagram.__init__(self, gender)

		self.showBoobs = False

	def takePhoto(self, showBoobs):
		self.showBoobs = showBoobs

		if showBoobs:
			self.setAreYouFamous(True)

		if self.gender == "male" and self.areYouFamous != True:
			self.like = 7;
		elif self.gender == "male" and self.areYouFamous:
			self.like = 300 - self.barzoCount
		elif self.gender == "female":
			if self.areYouFamous != True:
				self.like = 20 # bff mode #on
			elif self.areYouFamous:
				self.like = 700

			while self.showBoobs and self.barzoCount < 150:
				self.like += self.barzoCount
				self.barzoCount = self.barzoCount + 1
		else:
			print "Go away fuckin faggot."
