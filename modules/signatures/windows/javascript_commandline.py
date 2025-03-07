# Copyright (C) 2017 Kevin Ross
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

class JavaScriptCommandline(Signature):
    name = "javascript_commandline"
    description = "Executes JavaScript in a commandline"
    severity = 3
    categories = ["javascript", "persistence", "downloader"]
    authors = ["Kevin Ross"]
    minimum = "2.0"
    ttp = ["T1059_007"]

    def on_complete(self):
        for cmdline in self.get_command_lines():
            if "javascript:" in cmdline.lower():
                self.mark_ioc("cmdline", cmdline)

        return self.has_marks()
