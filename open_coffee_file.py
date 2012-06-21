import sublime
import sublime_plugin
import os
import re

class OpenCoffeeTwinCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.views = []
    window = self.window
    current_file_path = self.window.active_view().file_name()

    if current_file_path.find("/spec/") > 0:
      twin_path = self.app_twin_path(current_file_path)
    else:
      twin_path = self.spec_twin_path(current_file_path)

    if os.path.exists(twin_path) :
      window.open_file(twin_path)
    else :
      if sublime.ok_cancel_dialog("Create file: "+twin_path, "Yeah, fuck it"):
        open(twin_path,"w").close()
        window.open_file(twin_path)
      else:
        sublime.status_message("Could not find " + twin_path)

  def app_twin_path(self, spec_path):
    file_path = re.search(r'scripts(/.*)', spec_path).group(1).replace("_spec.coffee", ".coffee")
    return self.find_app_directory() + file_path

  def find_app_directory(self):
    return self.find_directory([
      "/content/javascripts",
      "/app/assets/javascripts",
      "/app/coffeescripts"
    ])

  def spec_twin_path(self, app_path):
    file_path = re.search(r'scripts(/.*)', app_path).group(1).replace(".coffee", "_spec.coffee")
    return self.find_spec_directory() + file_path

  def find_spec_directory(self):
    return self.find_directory([
      "/spec/coffeescripts",
      "/spec/javascripts",
      "/spec/assets/javascripts"
    ])

  def find_directory(self, candidates):
    root_path = self.window.folders()[0]

    for candidate in candidates:
      print root_path + candidate
      if os.path.exists(root_path + candidate):
        return root_path + candidate

    raise Exception("Unable to find coffeescripts path in " + ','.join(map(str, candidates)))

