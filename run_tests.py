import sublime, sublime_plugin, os, re

class RunTests(sublime_plugin.TextCommand):
  def run(self, edit, single):
    current_file_path = self.view.file_name()

    if re.search("\/spec\/", current_file_path) == None:
      return sublime.error_message("You're not in a spec, bro.")

    root_path = re.sub("\/spec\/.*", "", current_file_path)

    file_path = self.view.file_name()
    if single:
      line_number, column = self.view.rowcol(self.view.sel()[0].begin())
      line_number += 1
      file_path += ":" + str(line_number)

    cmd = 'osascript<<-END\n'
    cmd += '  tell app "Terminal"\n'
    cmd += '    set currentTab to do script "cd ' + root_path + ' && bundle exec rspec ' + file_path + '"\n'
    cmd += '  end tell\nEND'

    os.system(cmd)

    focus_cmd = 'osascript<<-END\n'
    focus_cmd += '  tell app "Terminal" to activate\nEND'
    os.system(focus_cmd)
