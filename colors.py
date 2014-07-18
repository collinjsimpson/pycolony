class bc:
	lgray = '\033[89m'
	dgray = '\033[90m'
	red = '\033[91m'
	green = '\033[92m'
	yellow = '\033[93m'
	blue = '\033[94m'
	pink = '\033[95m'
	cyan = '\033[96m'
	white = '\033[97m'

	endc = '\033[0m'

	@staticmethod
	def disable():
		bc.lgray = ''
		bc.dgray = ''
		bc.red = ''
		bc.green = ''
		bc.yellow = ''
		bc.blue = ''
		bc.pink = ''
		bc.cyan = ''
		bc.white = ''
		bc.endc = ''

	@staticmethod
	def enable():
		bc.lgray = '\033[89m'
		bc.dgray = '\033[90m'
		bc.red = '\033[91m'
		bc.green = '\033[92m'
		bc.yellow = '\033[93m'
		bc.blue = '\033[94m'
		bc.pink = '\033[95m'
		bc.cyan = '\033[96m'
		bc.white = '\033[97m'
		bc.endc = '\033[0m'

# background
class bg:

        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        yellow = '\033[43m'
        blue = '\033[44m'
        magenta = '\033[45m'
        cyan = '\033[46m'
        white = '\033[47m'
        endc = '\033[0m'

        @staticmethod
        def disable():
                bg.black = ''
                bg.red = ''
                bg.green = ''
                bg.yellow = ''
                bg.blue = ''
                bg.magenta = ''
                bg.cyan = ''
                bg.white = ''
                bg.endc = ''

        @staticmethod
        def enable():
                bg.black = '\033[40m'
                bg.red = '\033[41m'
                bg.green = '\033[42m'
                bg.yellow = '\033[43m'
                bg.blue = '\033[44m'
                bg.magenta = '\033[45m'
                bg.cyan = '\033[46m'
                bg.white = '\033[47m'
                bg.endc = '\033[0m'
