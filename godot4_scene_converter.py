#!/usr/bin/env python3
"""
Convert Godot 3 scene files (.tscn) to Godot 4 format
"""
import os
import re

def convert_tscn_file(filepath):
    """Convert a .tscn file from Godot 3 to Godot 4 format"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Node type changes
    content = re.sub(r'type="WindowDialog"', 'type="Window"', content)
    
    # Property name changes
    content = re.sub(r'\brect_size\s*=', 'size =', content)
    content = re.sub(r'\brect_position\s*=', 'position =', content)
    content = re.sub(r'\brect_min_size\s*=', 'custom_minimum_size =', content)
    content = re.sub(r'\brect_global_position\s*=', 'global_position =', content)
    content = re.sub(r'\brect_scale\s*=', 'scale =', content)
    content = re.sub(r'\brect_pivot_offset\s*=', 'pivot_offset =', content)
    content = re.sub(r'\brect_clip_content\s*=', 'clip_contents =', content)
    content = re.sub(r'\bhint_tooltip\s*=', 'tooltip_text =', content)
    content = re.sub(r'\bwindow_title\s*=', 'title =', content)
    content = re.sub(r'\bmargin_left\s*=', 'offset_left =', content)
    content = re.sub(r'\bmargin_top\s*=', 'offset_top =', content)
    content = re.sub(r'\bmargin_right\s*=', 'offset_right =', content)
    content = re.sub(r'\bmargin_bottom\s*=', 'offset_bottom =', content)
    
    # Custom constants changed to theme overrides
    content = re.sub(r'custom_constants/', 'theme_override_constants/', content)
    content = re.sub(r'custom_colors/', 'theme_override_colors/', content)
    content = re.sub(r'custom_fonts/', 'theme_override_fonts/', content)
    content = re.sub(r'custom_styles/', 'theme_override_styles/', content)
    
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
    addon_path = r'd:\Games\Godot\AutotileEditorFork\AutotileEditor\addons\RPG_maker_Autotile2_3x3'
    
    # Find all .tscn files
    for filename in os.listdir(addon_path):
        if filename.endswith('.tscn'):
            filepath = os.path.join(addon_path, filename)
            convert_tscn_file(filepath)
