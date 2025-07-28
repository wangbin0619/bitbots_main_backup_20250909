#!/usr/bin/env python3
"""
Play completion sound for Claude Code hooks

This script plays a sound file when called by Claude Code hooks to indicate
job completion. Uses pygame for cross-platform audio playback.

Usage: python play_completion_sound.py [sound_file]
"""

import sys
import os
from pathlib import Path

def install_pygame():
    """Install pygame if not available"""
    try:
        import pygame
        return True
    except ImportError:
        print("pygame not found. Installing...")
        import subprocess
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
            print("pygame installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to install pygame: {e}")
            return False

def play_sound(sound_file):
    """
    Play a sound file using pygame
    
    Args:
        sound_file (str): Path to the sound file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        import pygame
    except ImportError:
        print("pygame library not available after installation attempt")
        return False
    
    # Validate sound file
    sound_path = Path(sound_file)
    if not sound_path.exists():
        print(f"Error: Sound file not found: {sound_file}")
        return False
    
    try:
        # Initialize pygame mixer
        pygame.mixer.pre_init()
        pygame.mixer.init()
        
        print(f"Playing sound: {sound_path.name}")
        
        # Load and play sound
        sound = pygame.mixer.Sound(str(sound_path))
        sound.play()
        
        # Wait for sound to finish
        while pygame.mixer.get_busy():
            pygame.time.wait(100)
        
        print("Sound playback completed!")
        return True
        
    except Exception as e:
        print(f"Error playing sound: {e}")
        return False
    finally:
        try:
            pygame.mixer.quit()
        except:
            pass

def main():
    """Main function to handle command line arguments and play sound"""
    print("=== Claude Code Completion Sound Hook ===\n")
    
    # Default sound file if none provided
    default_sound = "D:/20-robot/01-bitbots/01_wb_works/01.03_utilities/well-done-mouse-squirrel-cartoon.wav"
    
    # Get sound file from command line or use default
    if len(sys.argv) > 1:
        sound_file = sys.argv[1]
    else:
        sound_file = default_sound
    
    print(f"Target sound file: {sound_file}")
    
    # Install pygame if needed
    if not install_pygame():
        print("Cannot proceed without pygame library")
        sys.exit(1)
    
    # Play the sound
    success = play_sound(sound_file)
    
    if success:
        print("Job completion sound played successfully!")
        sys.exit(0)
    else:
        print("Failed to play completion sound!")
        sys.exit(1)

if __name__ == "__main__":
    main()