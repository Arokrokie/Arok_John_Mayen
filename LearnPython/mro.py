# Method Resolution Order (MRO) real-world example 1
class HardwareCamera:
    def capture(self):
        print("Capturing RAW image (Hardware)")


class AICamera(HardwareCamera):
    def capture(self):
        print("Enhancing with AI (Auto-HDR, Face Detection)")
        super().capture()  # Call parent's method


class FilterCamera(HardwareCamera):
    def capture(self):
        print("Applying Instagram-like filters")
        super().capture()  # Call parent's method


class SmartphoneCamera(AICamera, FilterCamera):
    def capture(self):
        print("Smartphone Camera Processing...")
        super().capture()


# Usage
phone = SmartphoneCamera()
phone.capture()


# Method Resolution Order (MRO) real-world example 2
class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.powered_on = False

    def power(self):
        self.powered_on = not self.powered_on
        status = "ON" if self.powered_on else "OFF"
        print(f"{self.name} power: {status}")


class VoiceControlled(SmartDevice):
    def control(self):
        print(f"Voice command executed on {self.name}")


class AppControlled(SmartDevice):
    def control(self):
        print(f"App command executed on {self.name}")


class SmartSpeaker(VoiceControlled, AppControlled):
    def play_music(self):
        if self.powered_on:
            print(f"{self.name} playing music")
        else:
            print("Can't play - device is off")


# Check MRO
print(SmartSpeaker.__mro__)
# Output:
# (<class '__main__.SmartSpeaker'>,
#  <class '__main__.VoiceControlled'>,
#  <class '__main__.AppControlled'>,
#  <class '__main__.SmartDevice'>,
#  <class 'object'>)

# Usage
print("\nDevice Actions:")
speaker = SmartSpeaker("Living Room Speaker")
speaker.power()  # Output: "Living Room Speaker power: ON"
speaker.control()  # Output: "Voice command executed on Living Room Speaker"
speaker.play_music()  # Output: "Living Room Speaker playing music"
