import sublime
import sublime_plugin
import os

class OpenRspecFileCommand(sublime_plugin.WindowCommand):
  def run(self, option):
    self.views = []
    window = self.window
    current_file_path = self.window.active_view().file_name()

    if current_file_path.find("/spec/") > 0:
      twin_path = current_file_path.replace("/spec/","/app/").replace("_spec.rb", ".rb")
      if not os.path.exists(twin_path):
        twin_path = current_file_path.replace("/spec/", "/").replace("_spec.rb", ".rb")
    else:
      twin_path = current_file_path.replace("/app/", "/spec/").replace(".rb", "_spec.rb")
      if not os.path.exists(twin_path):
        twin_path = current_file_path.replace("/lib/", "/spec/lib/").replace(".rb", "_spec.rb")

    if os.path.exists(twin_path) :
      window.open_file(twin_path)
    else :
      sublime.error_message("Could not find " + twin_path)
