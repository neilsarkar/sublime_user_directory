import sublime
import sublime_plugin
import os

class OpenCoffeeTwinCommand(sublime_plugin.WindowCommand):
  def run(self):
    # print("feck")
    self.views = []
    window = self.window
    current_file_path = self.window.active_view().file_name()

    if current_file_path.find("/spec/") > 0:
      twin_path = current_file_path.replace("/spec/","/app/").replace("_spec.coffee", ".coffee")
    else:
      twin_path = current_file_path.replace("/app/", "/spec/").replace(".coffee", "_spec.coffee")

    if os.path.exists(twin_path) :
      window.open_file(twin_path)
    else :
      sublime.status_message("Could not find " + twin_path)
