# Elixir.tmbundle

A **TextMate / Sublime Text Bundle** for the [**Elixir**](http://github.com/elixir-lang/elixir) programming language.

## Installation

Type the following commands to setup the bundle for **TextMate**:

    mkdir -p ~/Library/Application\ Support/TextMate/Bundles
    cd !$
    git clone git://github.com/elixir-lang/elixir-tmbundle Elixir.tmbundle
    osascript -e 'tell app "TextMate" to reload bundles'


If you are using **TextMate 2**, type the following commands in your shell:

    mkdir -p ~/Library/Application\ Support/TextMate/Bundles
    cd ~/Library/Application\ Support/TextMate/Bundles
    git clone git://github.com/elixir-lang/elixir-tmbundle Elixir.tmbundle


If you are using **Sublime Text 2**, type the following commands in your shell:

    cd ~/.config/sublime-text-2/Packages # If you are on Linux
    cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages # If you are on OS X
    cd %HOMEPATH%\AppData\Roaming\Sublime^ Text^ 2\Packages # If you are on Windows Vista or above
    cd %HOMEPATH%\Application^ Data\Sublime^ Text^ 2\Packages # If you are on Windows XP
    git clone git://github.com/elixir-lang/elixir-tmbundle Elixir

You can now use Elixir's color syntax in files. In some cases, you should restart Sublime Text to make changes work.

The bundle is still in development and includes syntax highlighting. Contributions and extensions are welcome!
