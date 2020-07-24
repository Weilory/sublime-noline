import sublime
import sublime_plugin


class NolineCommand(sublime_plugin.TextCommand):
	@staticmethod
	def disline(contents):
		flag = True
		result = ''
		for letter in contents:
			if(letter == '\n'):
				if flag: 
					flag = False
				else: 
					flag = True
					result += letter
			else:
				flag = True
				result += letter
		return result

	def run(self, edit):
		contents = self.view.substr(sublime.Region(0, self.view.size()))
		self.view.erase(edit, sublime.Region(0, self.view.size()))
		self.view.insert(edit, 0, NolineCommand.disline(contents))

