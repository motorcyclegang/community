# Copyright (C) 2012 Anderson Tamborim (@y2h4ck)
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

# Based on information from http://antivirus.about.com/od/windowsbasics/tp/autostartkeys.htm

from lib.cuckoo.common.abstracts import Signature

class BypassFirewall(Signature):
    name = "bypass_firewall"
    description = "Operates on local firewall's policies and settings"
    severity = 3
    categories = ["bypass"]
    authors = ["Anderson Tamborim", "nex", "Kevin Ross"]
    minimum = "2.0"
    ttp = ["T1543_003"]
    indicator = ".*\\\\SYSTEM\\\\CurrentControlSet\\\\Services\\\\SharedAccess\\\\Parameters\\\\FirewallPolicy\\\\.*"

    def on_complete(self):
        regkey = self.check_key(pattern=self.indicator, regex=True)
        if regkey:
            self.mark_ioc("registry", regkey)
            return True

        for cmdline in self.get_command_lines():
            if "netsh" in cmdline.lower() and "advfirewall" in cmdline.lower():
                self.mark_ioc("cmdline", cmdline)

        return self.has_marks()
