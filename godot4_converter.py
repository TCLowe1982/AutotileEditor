#!/usr/bin/env python3
"""
Godot 3 to Godot 4 conversion helper script
"""
import re
import os

def convert_file(filepath):
    """Convert a GDScript file from Godot 3 to Godot 4 syntax"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Basic keyword replacements
    content = re.sub(r'\bonready\b', '@onready', content)
    content = re.sub(r'\bexport\(', '@export(', content)
    content = re.sub(r'\btool\b', '@tool', content)
    
    # Rect properties
    content = re.sub(r'\.rect_size\b', '.size', content)
    content = re.sub(r'\.rect_position\b', '.position', content)
    content = re.sub(r'\.rect_min_size\b', '.custom_minimum_size', content)
    content = re.sub(r'\.rect_global_position\b', '.global_position', content)
    content = re.sub(r'\.rect_scale\b', '.scale', content)
    
    # Tooltip
    content = re.sub(r'\.hint_tooltip\b', '.tooltip_text', content)
    
    # Pool arrays
    content = re.sub(r'\bPoolStringArray\b', 'PackedStringArray', content)
    content = re.sub(r'\bPoolVector2Array\b', 'PackedVector2Array', content)
    content = re.sub(r'\bPoolIntArray\b', 'PackedInt32Array', content)
    
    # Instance -> Instantiate
    content = re.sub(r'\.instance\(\)', '.instantiate()', content)
    
    # Yield -> Await
    content = re.sub(r'\byield\((.*?), "idle_frame"\)', r'await \1.process_frame', content)
    content = re.sub(r'\byield\((.*?), "(.*?)"\)', r'await \1.\2', content)
    
    # File system API  
    content = re.sub(r'\bFile\.new\(\)', 'FileAccess', content)
    content = re.sub(r'var (\w+) = File\.new\(\)', r'var \1', content)
    content = re.sub(r'\bDirectory\.new\(\)', 'DirAccess', content)
    
    # Signal connections with 3 arguments (signal, target, method)
    # .connect("signal", self, "method") -> .connect("signal", method)
    content = re.sub(
        r'\.connect\("([^"]+)",\s*self,\s*"([^"]+)"',
        r'.connect("\1", \2',
        content
    )
    
    # is_connected with old style
    content = re.sub(
        r'\.is_connected\("([^"]+)",\s*self,\s*"([^"]+)"',
        r'.is_connected("\1", Callable(self, "\2")',
        content
    )
    
    # OS API changes
    content = re.sub(r'\bOS\.get_screen_size\(\)', 'DisplayServer.screen_get_size()', content)
    content = re.sub(r'\bOS\.set_window_size\(', 'get_window().size = ', content)
    content = re.sub(r'\bOS\.set_window_position\(', 'get_window().position = ', content)  
    content = re.sub(r'\bOS\.set_window_always_on_top\(', 'get_window().always_on_top = ', content)
    content = re.sub(r'\.scancode\b', '.keycode', content)
    content = re.sub(r'\bOS\.get_scancode_string\(', 'OS.get_keycode_string(', content)
    
    # Scene tree
    content = re.sub(r'\.filename\b', '.scene_file_path', content)
    
    # JSON
    content = re.sub(r'\bparse_json\(', 'JSON.parse_string(', content)
    content = re.sub(r'\bto_json\(', 'JSON.stringify(', content)
    
    # ImageTexture changes
    content = re.sub(
        r'(\w+)\s*=\s*ImageTexture\.new\(\)\s*\n\s*\1\.create_from_image\(([^)]+)\)',
        r'\1 = ImageTexture.create_from_image(\2)',
        content, 
        flags=re.MULTILINE
    )
    
    if content != original:
        # Backup original
        backup_path = filepath + '.godot3.bak'
        if not os.path.exists(backup_path):
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original)
        
        # Write converted
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Converted: {filepath}")
        return True
    else:
        print(f"No changes: {filepath}")
        return False

if __name__ == '__main__':
    import sys
    
    addon_path = r'd:\Games\Godot\AutotileEditorFork\AutotileEditor\addons\RPG_maker_Autotile2_3x3'
    
    gd_files = [
        'CreateAutoTile.gd',
        'custom_scrollbar.gd',
        'CustomFile.gd',
        'CustomFileDialog.gd',
        'CustomToolTip.gd',
        'save_panel.gd'
    ]
    
    for filename in gd_files:
        filepath = os.path.join(addon_path, filename)
        if os.path.exists(filepath):
            convert_file(filepath)
        else:
            print(f"File not found: {filepath}")
