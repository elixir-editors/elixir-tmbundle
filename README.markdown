# Elixir.tmbundle

A **TextMate / Sublime Text Bundle** for the [**Elixir**](http://github.com/elixir-lang/elixir) programming language.

It provides syntax highlighting, snippets, and keybindings. Contributions and extensions are welcome!

## Installation

If you are using **TextMate 2** you can install from Preferences → Bundles. To install manually type the following commands in your shell:

    mkdir -p ~/Library/Application\ Support/TextMate/Pristine\ Copy/Bundles
    cd ~/Library/Application\ Support/TextMate/Pristine\ Copy/Bundles
    git clone git://github.com/elixir-lang/elixir-tmbundle Elixir.tmbundle

Type the following commands to setup the bundle for **TextMate 1**:

    mkdir -p ~/Library/Application\ Support/TextMate/Bundles
    cd !$
    git clone git://github.com/elixir-lang/elixir-tmbundle Elixir.tmbundle
    osascript -e 'tell app "TextMate" to reload bundles'

If you are using **Sublime Text 2**, type the following commands in your shell:

    cd ~/.config/sublime-text-2/Packages # If you are on Linux
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages # If you are on OS X
    cd %HOMEPATH%\AppData\Roaming\Sublime^ Text^ 2\Packages # If you are on Windows Vista or above
    cd %HOMEPATH%\Application^ Data\Sublime^ Text^ 2\Packages # If you are on Windows XP
    git clone git://github.com/elixir-lang/elixir-tmbundle Elixir

If you are using **Sublime Text 3**, type the following commands in your shell:

    cd ~/.config/sublime-text-3/Packages # If you are on Linux
    cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages # If you are on OS X
    cd %HOMEPATH%\AppData\Roaming\Sublime^ Text^ 3\Packages # If you are on Windows Vista or above
    cd %HOMEPATH%\Application^ Data\Sublime^ Text^ 3\Packages # If you are on Windows XP
    git clone git://github.com/elixir-lang/elixir-tmbundle Elixir

You can now use Elixir's color syntax in files. In some cases, you should restart Sublime Text to make changes work.

## Code formatting for Sublime Text 3

Elixir v1.6 includes a code formatter. This package includes `super+shift+c` as a keybinding to automatically save and format the current file you are working on. If the file has invalid syntax, an alert will appear.

You can also add your own keybindings as follows:

    { "keys": ["super+e"], "command": "mix_format_file" }

You can also set up the package to automatically format the file on save. To do this,
go to Preferences -> Package Settings -> Elixir -> Settings and add
`"mix_format_on_save": true`.

