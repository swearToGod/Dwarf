"""
Dwarf - Copyright (C) 2018 iGio90

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
import subprocess

from PyQt5.QtWidgets import QAction


def get_qmenu_separator():
    separator = QAction("--------------------")
    separator.setEnabled(False)
    return separator


def do_shell_command(cmd):
    result = subprocess.run(cmd.split(' '), stdout=subprocess.PIPE)
    return result.stdout.decode('utf8')
