bl_info = {
    "name": "Mouse Focus Shotcuts",
    "description": "Adds Shortcuts mouse button4 (focus selected) and button5 (select all)",
    "author": "johnzero7",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "category": "User Interface",
}

import bpy


# store keymaps here to access after registration
addon_keymaps = []


def register():
    addon_keymaps.clear()
    # handle the keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    # Map Dopesheet
    km = kc.keymaps.new(name="Dopesheet", space_type="DOPESHEET_EDITOR")
    kmi = km.keymap_items.new("action.view_selected", "BUTTON4MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new("action.view_all", "BUTTON5MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))

    # Map Outliner
    km = kc.keymaps.new(name="Outliner", space_type="OUTLINER")
    kmi = km.keymap_items.new("outliner.show_active", "BUTTON4MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new("outliner.show_hierarchy", "BUTTON5MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))

    # Map 3D View
    km = kc.keymaps.new(name="3D View", space_type="VIEW_3D")
    kmi = km.keymap_items.new("view3d.view_selected", "BUTTON4MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new("view3d.view_all", "BUTTON5MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))

    # Map Graph Editor
    km = kc.keymaps.new(name="Graph Editor", space_type="GRAPH_EDITOR")
    kmi = km.keymap_items.new("graph.view_selected", "BUTTON4MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new("graph.view_all", "BUTTON5MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))

    # Map Image
    km = kc.keymaps.new(name="Image", space_type="IMAGE_EDITOR")
    kmi = km.keymap_items.new("image.view_selected", "BUTTON4MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new("image.view_all", "BUTTON5MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))

    # Map Node Editor
    km = kc.keymaps.new(name="Node Editor", space_type="NODE_EDITOR")
    kmi = km.keymap_items.new("node.view_selected", "BUTTON4MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new("node.view_all", "BUTTON5MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))

    # Map File Browser Main
    # Nothing

    # Map NLA Editor
    km = kc.keymaps.new(name="NLA Editor", space_type="NLA_EDITOR")
    kmi = km.keymap_items.new("nla.view_selected", "BUTTON4MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new("nla.view_all", "BUTTON5MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))

    # Map Sequencer
    km = kc.keymaps.new(name="Sequencer", space_type="SEQUENCE_EDITOR")
    kmi = km.keymap_items.new("sequencer.view_selected", "BUTTON4MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new("sequencer.view_all", "BUTTON5MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))

    # Map Clip Editor
    km = kc.keymaps.new(name="Clip Editor", space_type="CLIP_EDITOR")
    kmi = km.keymap_items.new("clip.view_selected", "BUTTON4MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))
    kmi = km.keymap_items.new("clip.view_all", "BUTTON5MOUSE", "PRESS")
    addon_keymaps.append((km, kmi))


def unregister():
    # handle the keymap
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    # Loop the Keymaps and remove each Keymap Item
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    # clear the list
    del addon_keymaps[:]


if __name__ == "__main__":
    register()
