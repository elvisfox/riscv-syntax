riscv-syntax
===========
This repository is forked and adapted from [mips-syntax](https://github.com/contradictioned/mips-syntax)

RISC-V syntax highlighting (adapted from MIPS) package for [Sublime Text 2](https://www.sublimetext.com/) and [Sublime Text 3](https://www.sublimetext.com/3).


For users
---------
Click on "Download ZIP", extract the archive into sublime's package folder, e.g. `~/.config/sublime-text-3/Packages/User/`.


For developers
--------------

If you want to change something, you need to install AAAPackageDev for sublime and then:

* edit `mips.JSON-tmLanguage`
* run *build* in Sublime and select *Convert to: Property List*
* increment version number in `packages.json`

In order to test your changes, you can symlink the repository to sublime's package folder, e.g.

    $ ln -s /tmp/riscv-syntax/ ~/.config/sublime-text-3/Packages/User/


Feel free to send merge requests!
