# Godot 3.2 to 4.5.1 Conversion Summary

## Files Converted

The following files have been updated from Godot 3.2 to Godot 4.5.1:

1. **plugin.gd** - Main plugin entry point
2. **CreateAutoTile.gd** - Main autotile creation logic (2383 lines)
3. **custom_scrollbar.gd** - Custom scrollbar component
4. **CustomFile.gd** - File representation in file dialog
5. **CustomFileDialog.gd** - Custom file dialog implementation
6. **CustomToolTip.gd** - Custom tooltip widget
7. **save_panel.gd** - Save panel UI component

## Major API Changes Applied

### 1. Annotations and Keywords
- `tool` → `@tool`
- `onready var` → `@onready var`
- `export(Type)` → `@export` with new syntax
  - `@export(String, DIR)` → `@export_dir`
  - `@export(Texture)` → `@export var pattern: Texture2D`
  - `@export(Array, String)` → `@export var array: Array[String]`
- `setget` → proper setter/getter properties

### 2. Node Properties
- `rect_size` → `size`
- `rect_position` → `position`
- `rect_min_size` → `custom_minimum_size`
- `rect_global_position` → `global_position`
- `rect_scale` → `scale`
- `hint_tooltip` → `tooltip_text`

### 3. Signal Connections
- Old: `.connect("signal", self, "method")`
- New: `.connect("signal", method)`
- Old: `.connect("signal", self, "method", [args])`
- New: `.connect("signal", method.bind(args))`
- Old: `is_connected("signal", self, "method")`
- New: `is_connected("signal", Callable(self, "method"))`

### 4. File System API
- `File.new()` → `FileAccess`
  - `file.open(path, File.READ)` → `FileAccess.open(path, FileAccess.READ)`
  - `file.file_exists(path)` → `FileAccess.file_exists(path)`
- `Directory.new()` → `DirAccess`
  - `dir.open(path); dir.list_dir_begin(true, true)` → `dir = DirAccess.open(path); dir.list_dir_begin()`
  - `dir.dir_exists(path)` → `DirAccess.dir_exists_absolute(path)`
  - `dir.make_dir_recursive(path)` → `DirAccess.make_dir_recursive_absolute(path)`
  - `dir.get_drive_count()` → `DirAccess.get_drive_count()`
  - `dir.get_drive(i)` → `DirAccess.get_drive_name(i)`

### 5. OS and Display API
- `OS.get_screen_size()` → `DisplayServer.screen_get_size()`
- `OS.set_window_size(size)` → `get_window().size = size`
- `OS.set_window_position(pos)` → `get_window().position = pos`
- `OS.set_window_always_on_top(bool)` → `get_window().always_on_top = bool`
- `OS.execute(path, args)` → `OS.create_process(path, args)`
- `OS.get_scancode_string(code)` → `OS.get_keycode_string(code)`
- `.scancode` → `.keycode`

### 6. Scene Tree and Resources
- `.filename` → `.scene_file_path`
- `.instance()` → `.instantiate()`
- `get_tree().set_screen_stretch(...)` → Removed (configured in project settings)

### 7. Arrays and Collections
- `PoolStringArray` → `PackedStringArray`
- `PoolVector2Array` → `PackedVector2Array`
- `PoolIntArray` → `PackedInt32Array`

### 8. Async Operations
- `yield(object, "signal")` → `await object.signal`
- `yield(get_tree(), "idle_frame")` → `await get_tree().process_frame`

### 9. JSON and String Utilities
- `parse_json(string)` → `JSON.parse_string(string)`
- `to_json(object)` → `JSON.stringify(object)`
- `.sha1_text()` → `.sha1_text()` (unchanged)

### 10. Image and Texture API
- `ImageTexture.new(); tex.create_from_image(img)` → `ImageTexture.create_from_image(img)`
- `.get_data()` on ImageTexture → `.get_image()`
- Image methods like `get_width()`, `get_height()`, `get_size()` remain the same

### 11. Theme Overrides
- `add_font_override("name", font)` → `add_theme_font_override("name", font)`
- `add_color_override("name", color)` → `add_theme_color_override("name", color)`
- `get_font("name")` → `get_theme_font("name", "ClassName")`
- `custom_colors/property` → Theme override methods

### 12. Input Handling
- Signal names remain largely the same
- `item_rect_changed` → `item_size_changed` (for some Control signals)

## Files Backed Up

All original files have been backed up with `.godot3.bak` extension in case you need to revert.

## Testing Recommendations

1. **Open the project in Godot 4.5.1**
2. **Check for compilation errors** in the script editor
3. **Test the plugin activation** in Project Settings → Plugins
4. **Test core functionality**:
   - Opening the autotile editor
   - Loading images
   - Creating autotiles
   - Saving tilesets
   - File dialogs
   - Custom scrollbars

## Known Limitations

1. **Scene files (.tscn)** were not updated - you may need to update these manually
2. **Theme resources** may need manual adjustment for Godot 4's new theme system
3. **Custom input actions** created at runtime might need adjustment
4. **Bitmap collision generation** may need testing as the API changed slightly

## Next Steps

1. Open project in Godot 4.5.1
2. Fix any remaining compilation errors
3. Update .tscn scene files if needed
4. Test all functionality thoroughly
5. Update theme.tres if styling issues occur

## Additional Resources

- [Godot 4.0 Porting Guide](https://docs.godotengine.org/en/stable/tutorials/migrating/upgrading_to_godot_4.html)
- [Godot 4 API Documentation](https://docs.godotengine.org/en/stable/classes/)
