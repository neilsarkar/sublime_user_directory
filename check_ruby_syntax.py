import sublime, sublime_plugin
import subprocess
import re

class CheckRubySyntax(sublime_plugin.TextCommand):
  def run(self, edit):
    file_name = self.view.file_name()

    check_syntax_command = subprocess.Popen(["ruby","-wc",file_name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out, err = check_syntax_command.communicate()

    if re.match(r"Syntax OK", out):
      sublime.message_dialog("Syntax OK")
    else:
      sublime.message_dialog(out)
