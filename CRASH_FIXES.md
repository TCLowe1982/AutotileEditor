# Godot 4 Crash Fixes Applied

## Issues That Caused CTD (Crash To Desktop)

### 1. **WindowDialog Node Type** ✅ FIXED
**Problem:** The `.tscn` files contained `WindowDialog` nodes which don't exist in Godot 4.  
**Fix:** Replaced all `type="WindowDialog"` with `type="Window"` in scene files.

**Files affected:**
- CreateAutoTile.tscn

### 2. **Input Constants Changed** ✅ FIXED
**Problem:** Mouse and keyboard constants were renamed in Godot 4.  
**Fixes applied:**

| Godot 3 Constant | Godot 4 Constant |
|-----------------|------------------|
| `BUTTON_WHEEL_UP` | `MOUSE_BUTTON_WHEEL_UP` |
| `BUTTON_WHEEL_DOWN` | `MOUSE_BUTTON_WHEEL_DOWN` |
| `BUTTON_LEFT` | `MOUSE_BUTTON_LEFT` |
| `KEY_CONTROL` | `KEY_CTRL` |

**Files updated:**
- CreateAutoTile.gd (3 instances)
- custom_scrollbar.gd (3 instances)

### 3. **Scene Property Names** ✅ FIXED
**Problem:** Scene files (.tscn) used Godot 3 property names.  
**Fixes applied:**

| Old Property | New Property |
|-------------|--------------|
| `rect_size` | `size` |
| `rect_position` | `position` |
| `rect_min_size` | `custom_minimum_size` |
| `rect_scale` | `scale` |
| `rect_clip_content` | `clip_contents` |
| `window_title` | `title` |
| `margin_left/top/right/bottom` | `offset_left/top/right/bottom` |
| `custom_constants/` | `theme_override_constants/` |
| `custom_colors/` | `theme_override_colors/` |
| `custom_fonts/` | `theme_override_fonts/` |
| `custom_styles/` | `theme_override_styles/` |

**Files converted:**
- CreateAutoTile.tscn
- CustomFile.tscn
- CustomFileDialog.tscn
- CustomToolTip.tscn
- custom_scrollbar.tscn
- save_panel.tscn

## How to Test

1. **Close Godot completely** if it's open
2. **Delete the `.godot` folder** in your project (if it exists) to force a clean reimport
3. **Open the project** in Godot 4.5.1
4. The project should now import without crashing

## What Was Done

### Scripts Updated
- Fixed all input constants to Godot 4 equivalents
- Already had most API changes from previous conversion

### Scene Files Updated  
- Converted all 6 .tscn files to Godot 4 format
- Replaced WindowDialog with Window
- Updated all property names
- Updated theme override syntax

## Backup Files

All original .tscn files have been backed up with `.godot3.bak` extension.

## If You Still Experience Issues

### Check for:
1. **Console output** in Godot - look for specific error messages
2. **Missing dependencies** - ensure all resource files are present
3. **Path issues** - verify all file paths are correct
4. **Theme resources** - may need manual conversion

### Common Post-Import Issues:
- **UI elements misaligned**: Godot 4 changed some layout behavior
- **Fonts not loading**: May need to reconvert font resources
- **Theme looks different**: Godot 4's theme system changed

### Debugging Steps:
1. Open Godot with `--verbose` flag to see detailed logs
2. Check the Output panel in Godot for warnings
3. Open individual scene files to see if they load
4. Test the addon in a minimal project first

## Next Steps

After successful import:
1. Test opening the AutoTile Editor from the Tools menu
2. Try loading an image
3. Test creating an autotile
4. Verify save functionality
5. Check all dialogs and UI elements

If everything works, you're good to go! If not, check the error messages and refer to QUICK_FIX_GUIDE.md.
