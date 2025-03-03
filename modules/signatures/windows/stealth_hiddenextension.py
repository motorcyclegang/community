# Copyright (C) 2016 Kevin Ross
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

class StealthHiddenExtension(Signature):
    name = "stealth_hidden_extension"
    description = "Attempts to modify Explorer settings to prevent file extensions from being displayed"
    severity = 3
    categories = ["stealth"]
    authors = ["Kevin Ross"]
    minimum = "2.0"
    ttp = ["T1564_001", "T1562_006"]

    regkeys_re = [
        ".*\\\\Software\\\\(Wow6432Node\\\\)?Microsoft\\\\Windows\\\\CurrentVersion\\\\Explorer\\\\Advanced\\\\HideFileExt$",
    ]

    def on_complete(self):
        for indicator in self.regkeys_re:
            for regkey in self.check_key(pattern=indicator, regex=True, actions=["regkey_written"], all=True):
                self.mark_ioc("registry", regkey)

        return self.has_marks()
