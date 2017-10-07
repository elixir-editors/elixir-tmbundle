import sublime, sublime_plugin

class MixFormatFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    window = self.view.window()
    window.run_command("save")
    window.run_command("exec", {
      "cmd": ["mix", "format", self.view.file_name()],
      "working_dir": window.folders()[0]
    })
    window.run_command("hide_panel")
