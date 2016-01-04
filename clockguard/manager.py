import time
from datetime import datetime

class TimeManager(object):
	def __init__(self, start_time=None, end_time=None):
		self.start_time = start_time
		self.end_time = end_time

	def check(self):
		raise NotImplementedError('subclasses of TimeManager must provide a check() method')

class ParticularTimePeriod(TimeManager):
	def __init__(self, start_time, end_time):
		super(ParticularTimePeriod, self).__init__(start_time, end_time)

	def check(self):
		current_datetime = datetime.now()
		if current_datetime < self.start_time and current_datetime > self.end_time:
			return True
		else:
			return False

class EveryDayManager(TimeManager):
	def __init__(self, start_time, end_time):
		super(EveryDayManager, self).__init__(start_time, end_time)

	def check(self):
		current_time = datetime.now().time()
		if current_time < self.start_time and current_time > self.end_time:
			return True
		else:
			return False

class EveryWeekManager(TimeManager):
	def __init__(self, start_time, end_time, day):
		super()

	def check(self):
		return True

class EveryMonthManager(TimeManager):
	def __init__(self, start_time, end_time, date):
		super()

	def check(self):
		return True

class EveryYearManager(TimeManager):
	def __init__(self, start_time, end_time, date):
		super()

	def check(self):
		return True