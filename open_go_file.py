import sublime
import sublime_plugin
import os

class OpenGoTwinCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.views = []
    window = self.window
    current_file_path = self.window.active_view().file_name()



    if current_file_path.find("_test") > 0:
      twin_path = self.app_twin_path(current_file_path)
    else:
      twin_path = self.test_twin_path(current_file_path)

    if os.path.exists(twin_path) :
      window.open_file(twin_path)
    else :
      if sublime.ok_cancel_dialog("Create file: "+twin_path, "Yeah, fuck it"):
        open(twin_path,"w").close()
        window.open_file(twin_path)
      else:
        sublime.status_message("Could not find " + twin_path)

  def app_twin_path(self, spec_path):
    return spec_path.replace("_test.go", ".go")
  def test_twin_path(self, spec_path):
    return spec_path.replace(".go", "_test.go")
