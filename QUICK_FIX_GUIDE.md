# Quick Fix Guide for Remaining Issues

## Common Issues You May Encounter

### 1. Scene File (.tscn) Updates

Scene files may reference old node types or properties. Common replacements:

```gdscript
# In .tscn files, you may need to manually update:
[node name="..." type="Control"]
rect_min_size = Vector2(100, 100)  # Change to: custom_minimum_size
rect_position = Vector2(0, 0)       # Change to: position  
rect_size = Vector2(200, 200)       # Change to: size
```

### 2. Window Dialog Changes

WindowDialog was replaced with Window in Godot 4:
- If you have WindowDialog nodes in scenes, change them to Window
- Update properties accordingly

### 3. Input Constants

Some input constants changed:
```gdscript
# Old (Godot 3)
BUTTON_WHEEL_UP
BUTTON_WHEEL_DOWN
KEY_CONTROL

# New (Godot 4) 
MOUSE_BUTTON_WHEEL_UP
MOUSE_BUTTON_WHEEL_DOWN
KEY_CTRL
```

### 4. Color Constructors

```gdscript
# Old
Color("ff0000")

# New (both work, but preferred)
Color("#ff0000")
Color(1.0, 0.0, 0.0)
```

### 5. Texture/Image Size Methods

For textures, use:
```gdscript
# For Image objects (unchanged)
img.get_width()
img.get_height()

# For Texture2D/ImageTexture
texture.get_size()     # Returns Vector2i
texture.get_image()    # Gets the Image, then use image methods
```

### 6. Custom Fonts

If custom fonts don't load:
```gdscript
# Make sure font resources are updated for Godot 4
# FontData replaced the old Font system
```

### 7. Manual Testing Checklist

- [ ] Plugin loads without errors
- [ ] All UI elements visible and positioned correctly
- [ ] File dialogs open and work
- [ ] Images load from file system
- [ ] Autotile creation works
- [ ] Saving works
- [ ] Custom scrollbars function
- [ ] Tooltips display correctly
- [ ] All buttons and inputs respond
- [ ] Collision polygon generation works
- [ ] Animation features work

### 8. If You Get Specific Errors

**"Invalid call" errors on connect:**
- Make sure signal connections use Callable syntax
- Check that method names are spelled correctly

**"Unknown method" errors:**
- Check the Godot 4 API docs - some methods were renamed
- Common: `get_data()` → `get_image()` for textures

**Theme/styling missing:**
- Update theme.tres resource
- Convert custom theme overrides to new format

**Input actions not working:**
- Check InputMap setup
- Update KEY_* constants to Godot 4 versions

### 9. Performance Considerations

Godot 4 has better performance but:
- Image/texture operations may behave differently
- File I/O is now more strict about error checking
- Some operations are now async (use await)

### 10. Compatibility Script

If you find issues with specific Godot 3 code patterns, you can add compatibility helpers:

```gdscript
# compat.gd - Helper functions for compatibility
class_name Compat

static func safe_connect(object: Object, signal_name: String, callable: Callable):
    if not object.is_connected(signal_name, callable):
        object.connect(signal_name, callable)

static func load_image_as_texture(path: String) -> ImageTexture:
    var img = Image.new()
    var error = img.load(path)
    if error != OK:
        push_error("Failed to load image: " + path)
        return null
    return ImageTexture.create_from_image(img)
```

## Getting Help

If you encounter issues:
1. Check the conversion notes (GODOT4_CONVERSION_NOTES.md)
2. Review Godot 4 documentation
3. Check error messages carefully - they often point to the exact issue
4. Use the Godot 4 script editor's built-in error checking

## Reverting Changes

If needed, backup files are available with `.godot3.bak` extension:
```bash
# PowerShell command to restore backups
Get-ChildItem -Filter "*.godot3.bak" | ForEach-Object {
    $original = $_.FullName -replace '.godot3.bak$', ''
    Copy-Item $_.FullName $original -Force
}
```
