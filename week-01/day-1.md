Day 1
====================
### Video Resources
- [Week 1 Videos](https://www.youtube.com/playlist?list=PLu0CiQ7bzwEQbhg6rzm8h41r4c08KNij0)

### Computer Setup
This will be chaos. Your goal is to get a working environment, not to understand everything that happens. Please follow along closely!
* Apple ID / XCode (Should start the download in the morning or come in with it downloaded)
* [Slack](https://slack.com/downloads/osx) - for all communication purposes
* [Zoom](https://zoom.us/download)
* Sign up for [Operation Code](https://operationcode.org/join)
* [iTerm2](http://www.iterm2.com/)
* [VSCode](https://code.visualstudio.com/download)
* [Complete Installfest](https://gist.github.com/JYoung217/5a4bfdfecac5aa864075cfa68250bf5c)

### Challenges
* [99 Bottles](https://github.com/codeplatoon/99-Bottles) in JS
* [Deaf Grandma](https://github.com/codeplatoon/Deaf-Grandma) in JS
* [Terminal Commands In Depth](https://github.com/codeplatoon/Command-Line) - nothing to submit here but necessary reading

### Lecture Topics
* Your new Integrated Development Environment (IDE)
  * Your IDE is where you write, execute, and view your code in the browser. For us, we'll be using VSCode to write code, iTerm2 to execute code, and Google Chrome as the browser.
* Unix Commands / The Command Line
  * A frequent flyer who travels to the same hotel chain over and over again will have his preferences known by the hotel so that whenever they arrive, they get a similar experience. The same applies to your terminal - you want the same settings each time you load it up. Run `code ~/.bash_profile` to customize your terminal (unless you have settings you like already):
  ```
  parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
  }

  if [ -f ~/.git-completion.bash ]; then
    . ~/.git-completion.bash
  fi

  export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$(parse_git_branch) \[\033[00m\]$\[\033[00m\] "
  export PROMPT_COMMAND='echo -ne "\033]0;${PWD##*/}\007"'
  export CLICOLOR=1
  export LSCOLORS=ExFxBxDxCxegedabagacad
  ```

* VSCode Settings / Extensions
  * Add these to your settings under Code -> Preferences -> Settings in VSCode:
  ```
  {
    "editor.fontSize": 14,
    "files.autoSave": "onFocusChange",
    "editor.tabSize": 2,
    "editor.wordWrap": "on",
    "editor.multiCursorModifier": "ctrlCmd",
    "explorer.confirmDelete": false,
    "window.zoomLevel": 0,
    "workbench.startupEditor": "newUntitledFile",
    "workbench.colorTheme": "Visual Studio Dark",
    "workbench.iconTheme": "vscode-icons",
    "explorer.confirmDragAndDrop": false
  }
  ```
* Extensions are tools to make your job as a developer easier. Please install these:
  * Sublime Text Keymap and Settings Importer
  * Beautify
  * VSCode Icons
  * Bracket Pair Colorizer
  * Path IntelliSense
  * Preview on web server
  * Python


### Additonal Resources
* Sublime and Atom are two other text editors to edit code. They use the same keyboard shortcuts and save a lot of time when you're writing code. Luckily for us, the creators of VSCode have also accounted for these shortcuts in a package that we installed earlier.
  * Bookmark and use the [Shortcuts](http://docs.sublimetext.info/en/latest/reference/keyboard_shortcuts_osx.html)
  * VSCode [Shortcuts](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-macos.pdf)

### Homework
* Finish up the work from today and get used to the shortcuts from within VSCode
