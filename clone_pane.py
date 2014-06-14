import sublime, sublime_plugin

class ClonePaneCommand(sublime_plugin.WindowCommand):
  def run(self):
    # Use the ST2 built-in split to two panes
    self.window.run_command("set_layout", {"cells": [[0, 0, 1, 1], [1, 0, 2, 1]], "cols": [0.0, 0.5, 1.0], "rows": [0.0, 1.0]})
    # Requires the Origami package
    # self.window.run_command("create_pane", {"direction": "right"})
    self.window.run_command("clone_file_to_pane", {"direction": "right"})
