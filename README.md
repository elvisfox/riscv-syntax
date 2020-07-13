riscv-syntax
===========
This repository is forked from [riscv-syntax](https://github.com/Andreymazepas/riscv-syntax), which was forked and adapted from [mips-syntax](https://github.com/contradictioned/mips-syntax)

RISC-V syntax highlighting (adapted from MIPS) package for [Sublime Text 2](https://www.sublimetext.com/) and [Sublime Text 3](https://www.sublimetext.com/3).
C-style comments are used for compatibility with GNU Assembler.

For users
---------
Clone into sublime's package folder, e.g.:
- `~/.config/sublime-text-3/Packages/User/` for Linux,
- `~/Library/Application Support/Sublime Text 3/Packages/User` for macOS

For developers
--------------

If you want to change something, you need to install AAAPackageDev for sublime and then:

* edit `mips.JSON-tmLanguage`
* run *build* in Sublime and select *Convert to: Property List*
* increment version number in `packages.json`

Feel free to send merge requests!
