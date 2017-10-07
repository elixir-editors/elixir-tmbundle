import sublime, sublime_plugin, subprocess

class MixFormatFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    window = self.view.window()
    window.run_command("save")

    cmd = ["mix", "format", self.view.file_name()]
    cwd = window.folders()[0]
    returncode = subprocess.call(cmd, cwd=cwd)

    if returncode == 0:
      window.status_message("Formatting successful!")
    else:
      # TODO: Ideally we would show errors in a pane but life
      # is too short to figure it out. Pull requests welcome!
      sublime.error_message("Formatting failed!")
