# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "_benkl Generative Scripts",
    "author" : "GenerativeScripts",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . bgs_panel import BGS_PT_Panel
from . bgs_triransub import BGS_OT_Triransub
from . bgs_switchlines import BGS_OT_Switchlines
from . bgs_diffusion import BGS_OT_Diffusion

classes = (
    BGS_PT_Panel,
    BGS_OT_Triransub,
    BGS_OT_Switchlines,
    BGS_OT_Diffusion
)

def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)