import os
from os import path
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

    if scope.find('source.elixir') != -1 and scope.find('HTML (EEx)') == -1:
      settings = sublime.load_settings('Elixir.sublime-settings')

      if settings.get('mix_format_on_save', False):
        view.run_command('mix_format_file_without_save')

        if settings.get('reload_after_mix_format', False):
          view.run_command("revert")

class MixFormatFileWithoutSaveCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    window = self.view.window()
    settings = sublime.load_settings('Elixir.sublime-settings')

    # Hide the console window on Windows
    shell = False
    path_separator = ':'
    if os.name == 'nt':
        shell = True
        path_separator = ';'

    file_name = self.view.file_name()
    cmd = ['mix', 'format', file_name]
    cwd = self.find_cwd(window, settings, file_name)

    p = subprocess.Popen(
      cmd,
      stdout=subprocess.PIPE,
      stderr=subprocess.PIPE,
      shell=shell,
      cwd=cwd
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

  def find_cwd(self, window, settings, file_name):
    cur_dir = path.dirname(file_name)
    cwd = os.path.expanduser("~")
    for root_path in window.folders():
      if cur_dir.startswith(root_path):
        cwd = root_path
        break

    if settings.get('use_root_dir', False):
      cwd
    else:
      while cwd != cur_dir:
        if path.isfile(path.join(cur_dir, 'mix.exs')):
          cwd = cur_dir
          break
        else:
          cur_dir = path.dirname(cur_dir)
          if cur_dir == "/":
            cwd
            break

    return cwd





