#!/usr/bin/env python3
"""
Debug Claude Code Hook Issues
"""
import os
import sys
from pathlib import Path

def debug_hook_setup():
    """Debug the hook configuration and file setup"""
    
    print("=== Claude Code Hook Debug ===\n")
    
    # Check sound file
    sound_file = Path("D:/20-robot/01-bitbots/01_wb_works/01.03_utilities/well-done-mouse-squirrel-cartoon.wav")
    print(f"1. Sound file check:")
    print(f"   Path: {sound_file}")
    print(f"   Exists: {sound_file.exists()}")
    if sound_file.exists():
        print(f"   Size: {sound_file.stat().st_size:,} bytes")
    else:
        print("   ERROR: Sound file not found!")
    print()
    
    # Check script file
    script_file = Path("D:/20-robot/01-bitbots/01_wb_works/01.03_utilities/play_completion_sound.py")
    print(f"2. Script file check:")
    print(f"   Path: {script_file}")
    print(f"   Exists: {script_file.exists()}")
    if script_file.exists():
        print(f"   Size: {script_file.stat().st_size:,} bytes")
    else:
        print("   ERROR: Script file not found!")
    print()
    
    # Check settings file
    settings_file = Path("D:/20-robot/01-bitbots/.claude/settings.local.json")
    print(f"3. Settings file check:")
    print(f"   Path: {settings_file}")
    print(f"   Exists: {settings_file.exists()}")
    if settings_file.exists():
        with open(settings_file, 'r') as f:
            content = f.read()
        print(f"   Content:\n{content}")
    else:
        print("   ERROR: Settings file not found!")
    print()
    
    # Test pygame
    print("4. Pygame test:")
    try:
        import pygame
        print(f"   Pygame available: YES (version: {pygame.version.ver})")
    except ImportError:
        print("   Pygame available: NO")
    print()
    
    # Test manual script execution
    print("5. Manual script test:")
    if script_file.exists():
        print("   Running script manually...")
        import subprocess
        try:
            result = subprocess.run([
                sys.executable, 
                str(script_file)
            ], capture_output=True, text=True, timeout=30)
            print(f"   Return code: {result.returncode}")
            print(f"   Stdout: {result.stdout}")
            if result.stderr:
                print(f"   Stderr: {result.stderr}")
        except Exception as e:
            print(f"   Error: {e}")
    else:
        print("   Cannot test - script file missing")

if __name__ == "__main__":
    debug_hook_setup()