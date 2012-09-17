# NOTE: this does not work as is since trim_trailing_white_space runs afterwards
# for now, you can just add this logic to trim_trailing_white_space.py in Default
import sublime, sublime_plugin

class SteadyCursor(sublime_plugin.EventListener):
  def on_pre_save(self, view):
    if self.should_reindent(view):
      view.run_command("reindent")

  # reindent if the cursor is chilling on a non-terminal empty line
  def should_reindent(self, view):
    cursor = view.sel()[0]
    return view.sel().__len__() == 1 and view.line(cursor).empty() and cursor.end() != view.size()
