#!/usr/bin/env python3
"""
Create a test sound file using pygame
"""
import pygame
import numpy as np

def create_test_sound():
    """Create a simple test sound file"""
    
    # Initialize pygame
    pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=512)
    pygame.mixer.init()
    
    # Create a simple beep sound
    duration = 1.0  # seconds
    sample_rate = 22050
    
    # Generate a simple tone (440 Hz - A note)
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    frequency = 440.0
    wave = np.sin(frequency * 2 * np.pi * t)
    
    # Fade in/out to avoid clicks
    fade_frames = int(0.1 * sample_rate)
    wave[:fade_frames] *= np.linspace(0, 1, fade_frames)
    wave[-fade_frames:] *= np.linspace(1, 0, fade_frames)
    
    # Convert to 16-bit integers
    wave = (wave * 32767).astype(np.int16)
    
    # Make stereo
    stereo_wave = np.array([wave, wave]).T.copy(order='C')
    
    # Create pygame sound
    sound = pygame.sndarray.make_sound(stereo_wave)
    
    # Save as WAV file
    output_file = "D:/20-robot/01-bitbots/01_wb_works/01.03_utilities/well-done-mouse-squirrel-cartoon.wav"
    pygame.mixer.Sound.play(sound)
    pygame.time.wait(int(duration * 1000))
    
    # Alternative: Create a simple WAV file manually
    import wave
    import struct
    
    with wave.open(output_file, 'w') as wav_file:
        wav_file.setnchannels(1)  # mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(22050)
        
        # Generate 1 second of 440Hz sine wave
        for i in range(22050):
            value = int(32767 * np.sin(2 * np.pi * 440 * i / 22050))
            wav_file.writeframes(struct.pack('<h', value))
    
    print(f"Test sound created: {output_file}")
    return output_file

if __name__ == "__main__":
    try:
        create_test_sound()
    except Exception as e:
        print(f"Error creating sound: {e}")
        # Simpler approach - create silent WAV
        import wave
        output_file = "D:/20-robot/01-bitbots/01_wb_works/01.03_utilities/well-done-mouse-squirrel-cartoon.wav"
        with wave.open(output_file, 'w') as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2) 
            wav.setframerate(22050)
            # 1 second of silence
            wav.writeframes(b'\x00\x00' * 22050)
        print(f"Silent test file created: {output_file}")