import os
import gtk
from subprocess import call

class SevenZip():

	def __init__(self, main_window)	:
		self.main_window = main_window
		self.archive_mimes = ('application/zip', 'application/x-tar', 'application/x-compressed-tar')
		self.menu_mimes = ('application/octet-stream', 'inode/directory', 'text/directory', 'folder')
		self.menu_item = (
			{
				'label': 'Extract here',
				'data': False,
				'callback': self.archive_extract,
			},
            {
            	'label': 'Extract to folder',
            	'data': True,
            	'callback': self.archive_extract,
            },
			{
				'label': 'Create .7z archive',
				'callback': self.archive_create_7z,
			},

		)

		self.menu = gtk.Menu()
		for item in self.menu_item:
			self.menu.append(self.main_window.menu_manager.create_menu_item(item))

		self.sevenzip_menu = self.main_window.menu_manager.create_menu_item(
			{
				'label': '7zip',
				'submenu': ''
			}
		)
		self.sevenzip_menu.connect("activate", self.expand_menu)

	def expand_menu(self, data):
		#TODO do not show Extract options for non-archives
		self.sevenzip_menu.set_submenu(self.menu)

	def get_selection(self):
		selections = self.main_window.get_active_object()._get_selection()
		return selections

	def archive_extract(self, widget, to_folder):
		filepath = self.get_selection()
		path = os.path.dirname(filepath)

		if to_folder:
			path = os.path.splitext(filepath)[0]
			try:
				call(["mkdir", path])
			except Exception, e:
				print e

		try:
			#TODO supress 7z output?
			call(["7za", "x", "-o"+path, filepath])
		except Exception, e:
			print e

	def archive_create_7z(self, widget, data):
		filepath = self.get_selection()
		archive_path = os.path.dirname(filepath)
		archive_file = os.path.basename(filepath) + ".7z"

		#TODO check if the archive does not already exist

		try:
			call(["7za", "a", archive_path + "/" + archive_file, filepath])
		except Exception, e:
			print e


def register_plugin(application):
	plugin = SevenZip(application)
	application.register_popup_menu_action(plugin.menu_mimes, plugin.sevenzip_menu)
