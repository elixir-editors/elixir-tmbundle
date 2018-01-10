import os
import sublime
import sublime_plugin
import subprocess

class MixFormatFileCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    window = self.view.window()
    window.run_command("save")
    window.run_command("mix_format_file_without_save")

class MixFormatOnSave(sublime_plugin.EventListener):
  def on_post_save(self, view):
    sel = view.sel()[0]
    region = view.word(sel)
    scope = view.scope_name(region.b)

    if scope.find('source.elixir') != -1:
      settings = sublime.load_settings('Elixir.sublime-settings')

      if settings.get('mix_format_on_save', False):
        view.run_command('mix_format_file_without_save')

class MixFormatFileWithoutSaveCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    window = self.view.window()

    # Hide the console window on Windows
    shell = False
    path_separator = ':'
    if os.name == 'nt':
        shell = True
        path_separator = ';'

    cmd = ['mix', 'format', self.view.file_name()]

    p = subprocess.Popen(
      cmd,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      shell=shell
    )

    _, stderrdata = p.communicate()

    stderrdata = stderrdata.strip()

    if stderrdata:
      panel_view = window.create_output_panel('mix_format')
      panel_view.set_read_only(False)

      panel_view.run_command('erase_view')
      panel_view.run_command('append', {'characters': stderrdata.decode()})

      panel_view.set_read_only(True)
      window.run_command('show_panel', {'panel': 'output.mix_format'})
    else:
      window.run_command('hide_panel', {'panel': 'output.mix_format'})
      window.status_message('Formatting successful!')


