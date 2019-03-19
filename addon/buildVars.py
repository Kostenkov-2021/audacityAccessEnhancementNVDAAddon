# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "audacityAccessEnhancement",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Audacity multi-track editor: accessibility enhancement"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""This add-on adds extra functionality when working with Audacity

* a script to report audio position,
* a script to report start and end of selection,
* a script to announce the state of the  "Pause",  "Play" and "record" buttons,
* automatic audio position changes report ,
* automatic selection changes report (can be disabled),
* timer control editting support,
* use of spacebar to press a button,
* script to report playback/recording peak level,
* script to report playback/record slider level,
* script to report playback speed,
* script to display add-on user manual,
* script to display audacity guide written by David Bailes.


This addon's version has been tested with NVDA 2018.4, 2019.1 and audacity v2.3.0.

Previous versions of Audacity are not  supported.
"""),

	# version
	"addon_version" : "1.1",
	# Author(s)
	"addon_author" : "paulber19",
	# URL for the add-on documentation support
	"addon_url" : "paulber19@laposte.net",
	# Documentation file name
	"addon_docFileName" : "addonUserManual.html",
	# Minimum NVDA version supported (e.g. "2018.3")
	"addon_minimumNVDAVersion" : "2018.4.0",
	# Last NVDA version supported/tested (e.g. "2018.4", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2019.1.0",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
mainPath = os.path.join("addon", "appModules", "audacity")
pythonSources = [
os.path.join("addon", "*.py"),
os.path.join("addon", "appModules", "audacity", "*.py"),
]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []