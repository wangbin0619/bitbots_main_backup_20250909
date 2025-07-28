# Claude Code Sound Hook Setup

## Overview
This setup enables Claude Code to play a completion sound when jobs finish using the hook system.

## Files Created

### 1. Sound Player Script
**File:** `play_completion_sound.py`
- Automatically installs pygame for audio playback
- Plays WAV files with cross-platform compatibility
- Default sound: `well-done-mouse-squirrel-cartoon.wav`
- Can accept custom sound file as argument

### 2. Hook Configuration
**File:** `.claude/settings.local.json`
- Configured `tool-call-finish` hook to trigger sound
- Runs after each tool operation completes
- Uses absolute path for reliability

## Hook Configuration Details
```json
{
  "hooks": {
    "tool-call-finish": "python \"D:\\20-robot\\01-bitbots\\01_wb_works\\01.03_utilities\\play_completion_sound.py\""
  }
}
```

## How It Works
1. **Trigger:** Every time Claude Code finishes executing a tool
2. **Action:** Runs the sound player script 
3. **Sound:** Plays the completion sound file
4. **Feedback:** Audio notification that operation completed

## Usage
The hook runs automatically - no manual intervention needed. Each tool completion will play the sound.

### Manual Testing
```bash
# Test the sound player directly
python play_completion_sound.py

# Test with custom sound file
python play_completion_sound.py "path/to/custom/sound.wav"
```

## Requirements
- pygame library (auto-installed by script)
- Sound file at specified path
- Working audio system

## Hook Types Available
- `tool-call-finish` - After each tool execution (CONFIGURED)
- `user-prompt-submit` - When user submits prompt  
- `assistant-response-start` - When assistant starts responding
- `assistant-response-finish` - When assistant completes response

## Customization
To change when sound plays, modify the hook type in `settings.local.json`:
- Use `assistant-response-finish` for end of full response
- Use `user-prompt-submit` for when user asks question
- Current: `tool-call-finish` for each tool operation

## Troubleshooting
- Ensure sound file exists at specified path
- Check audio system is working
- Verify pygame installation
- Check file path formatting (use double backslashes on Windows)