from flask import Flask, request
from experta import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    args = request.args.get('problem', '')

    class PCProblem(Fact):
        """Information about the PC problem"""
        pass

    class PCExpertSystem(KnowledgeEngine):
        @DefFacts()
        def _initial_action(self):
            yield Fact(action="find_problem")

        @Rule(Fact(action='find_problem'),
              NOT(PCProblem(problem=W())))
        def ask_problem(self):
            self.problem = args
            self.declare(PCProblem(problem=self.problem))
            self.solution = {"message":"hello to our project "}

            ##Display Problems##

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'no display' in x.lower())))
        def no_display(self):
            self.solution = {"proplem": "No display on the monitor",
                             "solution-1": " Ensure the monitor is powered on.",
                             "solution-2": " Check the video cable connection between the monitor and the PC.",
                             "solution-3": " Try connecting the monitor to another PC to rule out monitor issues.",
                             "solution-4": " If using a dedicated GPU, ensure the monitor is connected to the GPU and not the motherboard.",

                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'flickering screen' in x.lower())))
        def flickering_screen(self):
            self.solution = {"proplem": "flickering screen",
                             "solution-1": " Check the video cable for any damage or loose connections.",
                             "solution-2": " Update or reinstall the graphics driver.",
                             "solution-3": " Try a different monitor to rule out monitor issues..",
                             "solution-4": " If the problem persists, it could be a GPU issue.",

                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'black screen' in x.lower())))
        def black_screen(self):
            self.solution = {"proplem": "Black screen on the monitor",
                             "solution-1": " Ensure the monitor is powered on and the power cable is securely connected.",
                             "solution-2": " Check the video cable connection between the monitor and the PC.",
                             "solution-3": " Try connecting the monitor to another PC to rule out monitor issues.",
                             "solution-4": " If using a dedicated GPU, ensure the monitor is connected to the GPU and not the motherboard.",
                             "solution-5": " Restart the computer and check if the display returns."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'screen goes blank' in x.lower())))
        def screen_goes_blank(self):
            self.solution = {"proplem": "Screen goes blank after a few seconds",
                             "solution-1": " Check the power settings and disable 'Turn off display' or 'Sleep' mode.",
                             "solution-2": " Ensure the video cable is securely connected and not damaged.",
                             "solution-3": " Update the graphics driver to the latest version.",
                             "solution-4": " Test the monitor on another PC to rule out hardware issues.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'lines on screen' in x.lower())))
        def lines_on_screen(self):
            self.solution = {"proplem": "Lines or streaks on the screen",
                             "solution-1": " Check the video cable for damage or loose connections.",
                             "solution-2": " Update or reinstall the graphics driver.",
                             "solution-3": " Test the monitor on another PC to rule out monitor issues.",
                             "solution-4": " If the problem persists, it could be a GPU or monitor hardware issue.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'screen flickering' in x.lower())))
        def screen_flickering(self):
            self.solution = {"proplem": "Screen flickering",
                             "solution-1": " Check the video cable for any damage or loose connections.",
                             "solution-2": " Update or reinstall the graphics driver.",
                             "solution-3": " Adjust the screen refresh rate in the display settings.",
                             "solution-4": " Test the monitor on another PC to rule out monitor issues.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'wrong resolution' in x.lower())))
        def wrong_resolution(self):
            self.solution = {"proplem": "Incorrect screen resolution",
                             "solution-1": " Right-click on the desktop and select 'Display settings'.",
                             "solution-2": " Adjust the resolution to the recommended setting.",
                             "solution-3": " Update the graphics driver to the latest version.",
                             "solution-4": " Restart the computer and check if the resolution is correct.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'screen tearing' in x.lower())))
        def screen_tearing(self):
            self.solution = {"proplem": "Screen tearing during video playback or gaming",
                             "solution-1": " Enable V-Sync in the graphics settings of your game or application.",
                             "solution-2": " Update the graphics driver to the latest version.",
                             "solution-3": " Adjust the screen refresh rate in the display settings.",
                             "solution-4": " If using a dedicated GPU, ensure the monitor is connected to the GPU and not the motherboard.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'dead pixels' in x.lower())))
        def dead_pixels(self):
            self.solution = {"proplem": "Dead or stuck pixels on the screen",
                             "solution-1": " Use a dead pixel fixer tool or video to attempt to revive the pixels.",
                             "solution-2": " Gently massage the affected area of the screen (if it's safe to do so).",
                             "solution-3": " If the issue persists, contact the manufacturer for a warranty replacement.",
                             "solution-4": " Consider replacing the monitor if it's out of warranty.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'oversized display' in x.lower())))
        def oversized_display(self):
            self.solution = {"proplem": "Display is oversized or doesn't fit the screen",
                             "solution-1": " Adjust the screen resolution in the display settings.",
                             "solution-2": " Check the monitor's settings for a 'Scaling' or 'Aspect Ratio' option.",
                             "solution-3": " Update the graphics driver to the latest version.",
                             "solution-4": " If using a TV as a monitor, ensure the TV's display mode is set to 'PC' or 'Just Scan'.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'no signal' in x.lower())))
        def no_signal(self):
            self.solution = {"proplem": "Monitor shows 'No Signal'",
                             "solution-1": " Ensure the monitor is powered on and the video cable is securely connected.",
                             "solution-2": " Check if the PC is powered on and the GPU is functioning.",
                             "solution-3": " Try using a different video cable or port.",
                             "solution-4": " Test the monitor on another PC to rule out monitor issues.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'color distortion' in x.lower())))
        def color_distortion(self):
            self.solution = {"proplem": "Colors on the screen are distorted or incorrect",
                             "solution-1": " Check the video cable for damage or loose connections.",
                             "solution-2": " Adjust the color settings in the monitor's on-screen display (OSD).",
                             "solution-3": " Update or reinstall the graphics driver.",
                             "solution-4": " Test the monitor on another PC to rule out monitor issues.",
                             }

            ##Hard Drive Problems ##

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive not detected' in x.lower())))
        def hard_drive_not_detected(self):
            self.solution = {"proplem": "Hard drive not detected",
                             "solution-1": " Ensure the hard drive is properly connected to the motherboard and power supply.",
                             "solution-2": " Check the BIOS/UEFI settings to see if the hard drive is recognized.",
                             "solution-3": " Try using a different SATA cable or port.",
                             "solution-4": " If the drive is still not detected, it may be faulty.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'slow performance' in x.lower())))
        def slow_performance(self):
            self.solution = {"proplem": "Slow performance",
                             "solution-1": " Check the hard drive's health using diagnostic tools.",
                             "solution-2": " Ensure the hard drive has sufficient free space.",
                             "solution-3": " Defragment the hard drive (if it's an HDD).",
                             "solution-4": " Consider upgrading to an SSD for better performance.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive making noise' in x.lower())))
        def hard_drive_making_noise(self):
            self.solution = {"proplem": "Hard drive making noise",
                             "solution-1": " Back up your data immediately as the drive may be failing.",
                             "solution-2": " Check the drive's health using diagnostic tools.",
                             "solution-3": " Ensure the drive is securely mounted and not vibrating.",
                             "solution-4": " Replace the hard drive if the noise persists.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive full' in x.lower())))
        def hard_drive_full(self):
            self.solution = {"proplem": "Hard drive is full",
                             "solution-1": " Delete unnecessary files and programs.",
                             "solution-2": " Move files to an external drive or cloud storage.",
                             "solution-3": " Use disk cleanup tools to remove temporary files.",
                             "solution-4": " Consider upgrading to a larger capacity drive.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive corrupted' in x.lower())))
        def hard_drive_corrupted(self):
            self.solution = {"proplem": "Hard drive is corrupted",
                             "solution-1": " Run a disk check using `chkdsk` in Command Prompt.",
                             "solution-2": " Use data recovery software to retrieve important files.",
                             "solution-3": " Format the drive and reinstall the operating system if necessary.",
                             "solution-4": " Replace the hard drive if it cannot be repaired.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive overheating' in x.lower())))
        def hard_drive_overheating(self):
            self.solution = {"proplem": "Hard drive is overheating",
                             "solution-1": " Ensure the computer has adequate ventilation and cooling.",
                             "solution-2": " Clean any dust from the internal components.",
                             "solution-3": " Check the drive's health using diagnostic tools.",
                             "solution-4": " Replace the hard drive if it continues to overheat.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive not booting' in x.lower())))
        def hard_drive_not_booting(self):
            self.solution = {"proplem": "Hard drive not booting",
                             "solution-1": " Ensure the boot order is set correctly in the BIOS/UEFI.",
                             "solution-2": " Check if the operating system files are corrupted.",
                             "solution-3": " Use a bootable USB to repair the operating system.",
                             "solution-4": " Replace the hard drive if it cannot boot.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive bad sectors' in x.lower())))
        def hard_drive_bad_sectors(self):
            self.solution = {"proplem": "Hard drive has bad sectors",
                             "solution-1": " Run a disk check using `chkdsk /r` in Command Prompt.",
                             "solution-2": " Back up your data immediately.",
                             "solution-3": " Use disk repair tools to attempt to fix the bad sectors.",
                             "solution-4": " Replace the hard drive if the bad sectors cannot be repaired.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive not recognized' in x.lower())))
        def hard_drive_not_recognized(self):
            self.solution = {"proplem": "Hard drive not recognized by the operating system",
                             "solution-1": " Check Disk Management to see if the drive needs to be initialized or formatted.",
                             "solution-2": " Update the storage controller drivers.",
                             "solution-3": " Try connecting the drive to another PC.",
                             "solution-4": " Replace the hard drive if it is not recognized.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive clicking' in x.lower())))
        def hard_drive_clicking(self):
            self.solution = {"proplem": "Hard drive is clicking",
                             "solution-1": " Back up your data immediately as the drive may be failing.",
                             "solution-2": " Check the drive's health using diagnostic tools.",
                             "solution-3": " Ensure the drive is securely connected and not loose.",
                             "solution-4": " Replace the hard drive if the clicking persists.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive not spinning' in x.lower())))
        def hard_drive_not_spinning(self):
            self.solution = {"proplem": "Hard drive is not spinning",
                             "solution-1": " Ensure the power cable is securely connected to the drive.",
                             "solution-2": " Try using a different power cable or port.",
                             "solution-3": " Check if the drive is recognized in the BIOS/UEFI.",
                             "solution-4": " Replace the hard drive if it does not spin up.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive write errors' in x.lower())))
        def hard_drive_write_errors(self):
            self.solution = {"proplem": "Hard drive write errors",
                             "solution-1": " Run a disk check using `chkdsk` in Command Prompt.",
                             "solution-2": " Check the drive's health using diagnostic tools.",
                             "solution-3": " Update the storage controller drivers.",
                             "solution-4": " Replace the hard drive if the errors persist.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive read errors' in x.lower())))
        def hard_drive_read_errors(self):
            self.solution = {"proplem": "Hard drive read errors",
                             "solution-1": " Run a disk check using `chkdsk` in Command Prompt.",
                             "solution-2": " Check the drive's health using diagnostic tools.",
                             "solution-3": " Update the storage controller drivers.",
                             "solution-4": " Replace the hard drive if the errors persist.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive not formatting' in x.lower())))
        def hard_drive_not_formatting(self):
            self.solution = {"proplem": "Hard drive not formatting",
                             "solution-1": " Use Disk Management or a third-party tool to format the drive.",
                             "solution-2": " Check if the drive is write-protected and remove the protection.",
                             "solution-3": " Update the storage controller drivers.",
                             "solution-4": " Replace the hard drive if it cannot be formatted.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'hard drive not showing full capacity' in x.lower())))
        def hard_drive_not_showing_full_capacity(self):
            self.solution = {"proplem": "Hard drive not showing full capacity",
                             "solution-1": " Check Disk Management to see if the drive has unallocated space.",
                             "solution-2": " Extend the partition to use the full capacity.",
                             "solution-3": " Update the storage controller drivers.",
                             "solution-4": " Replace the hard drive if the issue persists.",
                             }

            ##RAM Problems##

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'computer crashes' in x.lower())))
        def computer_crashes(self):
            self.solution = {"proplem": "Computer crashes or blue screens",
                             "solution-1": " Run a memory diagnostic tool to check for RAM issues.",
                             "solution-2": " Ensure the RAM sticks are properly seated in their slots.",
                             "solution-3": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-4": " If the problem persists, consider replacing the RAM.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'insufficient memory' in x.lower())))
        def insufficient_memory(self):
            self.solution = {"proplem": "Insufficient memory",
                             "solution-1": " Close unnecessary programs to free up RAM.",
                             "solution-2": " Consider upgrading your RAM if you frequently run out of memory.",
                             "solution-3": " Check for memory leaks in running applications."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not detected' in x.lower())))
        def ram_not_detected(self):
            self.solution = {"proplem": "RAM not detected",
                             "solution-1": " Ensure the RAM sticks are properly seated in their slots.",
                             "solution-2": " Check the BIOS/UEFI settings to see if the RAM is recognized.",
                             "solution-3": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-4": " If the problem persists, consider replacing the RAM."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not working' in x.lower())))
        def ram_not_working(self):
            self.solution = {"proplem": "RAM not working",
                             "solution-1": " Ensure the RAM sticks are properly seated in their slots.",
                             "solution-2": " Check the BIOS/UEFI settings to see if the RAM is recognized.",
                             "solution-3": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-4": " If the problem persists, consider replacing the RAM."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram overheating' in x.lower())))
        def ram_overheating(self):
            self.solution = {"proplem": "RAM overheating",
                             "solution-1": " Ensure the computer has adequate ventilation and cooling.",
                             "solution-2": " Clean any dust from the internal components.",
                             "solution-3": " Check the RAM's health using diagnostic tools.",
                             "solution-4": " Replace the RAM if it continues to overheat."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not compatible' in x.lower())))
        def ram_not_compatible(self):
            self.solution = {"proplem": "RAM not compatible",
                             "solution-1": " Check the motherboard's specifications for compatible RAM types.",
                             "solution-2": " Ensure the RAM sticks are of the same type and speed.",
                             "solution-3": " Update the BIOS/UEFI to the latest version.",
                             "solution-4": " Replace the RAM with compatible modules."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not running at full speed' in x.lower())))
        def ram_not_running_at_full_speed(self):
            self.solution = {"proplem": "RAM not running at full speed",
                             "solution-1": " Check the BIOS/UEFI settings to ensure the RAM is running at its rated speed.",
                             "solution-2": " Enable XMP (Extreme Memory Profile) in the BIOS/UEFI.",
                             "solution-3": " Update the BIOS/UEFI to the latest version.",
                             "solution-4": " Replace the RAM if it cannot run at its rated speed."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not enough' in x.lower())))
        def ram_not_enough(self):
            self.solution = {"proplem": "Not enough RAM",
                             "solution-1": " Close unnecessary programs to free up RAM.",
                             "solution-2": " Consider upgrading your RAM if you frequently run out of memory.",
                             "solution-3": " Check for memory leaks in running applications.",
                             "solution-4": " Add more RAM modules to your system."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not recognized' in x.lower())))
        def ram_not_recognized(self):
            self.solution = {"proplem": "RAM not recognized",
                             "solution-1": " Ensure the RAM sticks are properly seated in their slots.",
                             "solution-2": " Check the BIOS/UEFI settings to see if the RAM is recognized.",
                             "solution-3": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-4": " If the problem persists, consider replacing the RAM."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not booting' in x.lower())))
        def ram_not_booting(self):
            self.solution = {"proplem": "RAM not booting",
                             "solution-1": " Ensure the RAM sticks are properly seated in their slots.",
                             "solution-2": " Check the BIOS/UEFI settings to see if the RAM is recognized.",
                             "solution-3": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-4": " If the problem persists, consider replacing the RAM."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not working after upgrade' in x.lower())))
        def ram_not_working_after_upgrade(self):
            self.solution = {"proplem": "RAM not working after upgrade",
                             "solution-1": " Ensure the new RAM sticks are compatible with your motherboard.",
                             "solution-2": " Check the BIOS/UEFI settings to see if the RAM is recognized.",
                             "solution-3": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-4": " If the problem persists, consider replacing the RAM."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not working after bios update' in x.lower())))
        def ram_not_working_after_bios_update(self):
            self.solution = {"proplem": "RAM not working after BIOS update",
                             "solution-1": " Revert to the previous BIOS version if possible.",
                             "solution-2": " Check the BIOS/UEFI settings to see if the RAM is recognized.",
                             "solution-3": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-4": " If the problem persists, consider replacing the RAM."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not working after overclocking' in x.lower())))
        def ram_not_working_after_overclocking(self):
            self.solution = {"proplem": "RAM not working after overclocking",
                             "solution-1": " Reset the BIOS/UEFI settings to default.",
                             "solution-2": " Check the BIOS/UEFI settings to see if the RAM is recognized.",
                             "solution-3": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-4": " If the problem persists, consider replacing the RAM."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not working after cleaning' in x.lower())))
        def ram_not_working_after_cleaning(self):
            self.solution = {"proplem": "RAM not working after cleaning",
                             "solution-1": " Ensure the RAM sticks are properly seated in their slots.",
                             "solution-2": " Check the BIOS/UEFI settings to see if the RAM is recognized.",
                             "solution-3": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-4": " If the problem persists, consider replacing the RAM."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not working after power surge' in x.lower())))
        def ram_not_working_after_power_surge(self):
            self.solution = {"proplem": "RAM not working after power surge",
                             "solution-1": " Check the BIOS/UEFI settings to see if the RAM is recognized.",
                             "solution-2": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-3": " Replace the RAM if it is damaged.",
                             "solution-4": " Consider using a surge protector to prevent future damage."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ram not working after moving' in x.lower())))
        def ram_not_working_after_moving(self):
            self.solution = {"proplem": "RAM not working after moving",
                             "solution-1": " Ensure the RAM sticks are properly seated in their slots.",
                             "solution-2": " Check the BIOS/UEFI settings to see if the RAM is recognized.",
                             "solution-3": " Try using one RAM stick at a time to identify a faulty module.",
                             "solution-4": " If the problem persists, consider replacing the RAM."
                             }

            ##Keyboard Problems##

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'keyboard not working' in x.lower())))
        def keyboard_not_working(self):
            self.solution = {"proplem": "Keyboard not working",
                             "solution-1": " Ensure the keyboard is properly connected to the PC.",
                             "solution-2": " Try using a different USB port or PS/2 port.",
                             "solution-3": " Check if the keyboard works on another PC.",
                             "solution-4": " Restart your computer to see if the keyboard is detected.",
                             "solution-5": " Update or reinstall the keyboard drivers in Device Manager.",
                             "solution-6": " If it's a wireless keyboard, replace or recharge the batteries."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'some keys not working' in x.lower())))
        def some_keys_not_working(self):
            self.solution = {"proplem": "Some keys on the keyboard are not working",
                             "solution-1": " Clean the keyboard to remove dust or debris under the keys.",
                             "solution-2": " Restart your computer to rule out a software glitch.",
                             "solution-3": " Test the keyboard on another PC to confirm if it's a hardware issue.",
                             "solution-4": " If it's a laptop, check if the keyboard driver needs updating.",
                             "solution-5": " Consider replacing the keyboard if cleaning doesn't resolve the issue.",
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'sticky keys' in x.lower())))
        def sticky_keys(self):
            self.solution = {"proplem": "Sticky keys",
                             "solution-1": " Turn off the 'Sticky Keys' feature in your operating system's accessibility settings.",
                             "solution-2": " Clean the keyboard to remove any spilled liquids or debris",
                             "solution-3": " If a key is physically stuck, gently remove it and clean underneath.",
                             "solution-4": " Replace the keyboard if the issue persists after cleaning."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'keyboard typing wrong characters' in x.lower())))
        def keyboard_typing_wrong_characters(self):
            self.solution = {"proplem": "Keyboard typing wrong characters",
                             "solution-1": " Check if the keyboard layout is set correctly in your operating system.",
                             "solution-2": " Restart your computer to rule out a software glitch.",
                             "solution-3": " Test the keyboard on another PC to confirm if it's a hardware issue.",
                             "solution-4": " If it's a laptop, ensure the 'Fn' key is not accidentally enabled.",
                             "solution-5": " Update the keyboard driver in Device Manager."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'wireless keyboard not connecting' in x.lower())))
        def wireless_keyboard_not_connecting(self):
            self.solution = {"proplem": "Wireless keyboard not connecting",
                             "solution-1": " Ensure the keyboard has fresh or charged batteries.",
                             "solution-2": " Check if the USB receiver is properly plugged into the PC.",
                             "solution-3": " Press the 'Connect' button on the keyboard and receiver (if applicable).",
                             "solution-4": " Restart your computer and try reconnecting the keyboard.",
                             "solution-5": " Update the keyboard driver in Device Manager.",
                             "solution-6": " Try using the keyboard on another PC to rule out a hardware issue."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'keyboard backlight not working' in x.lower())))
        def keyboard_backlight_not_working(self):
            self.solution = {"proplem": "Keyboard backlight not working",
                             "solution-1": " Check if the backlight feature is enabled (usually via a function key).",
                             "solution-2": " Restart your computer to rule out a software glitch.",
                             "solution-3": " Update the keyboard driver in Device Manager.",
                             "solution-4": " If it's a laptop, check the BIOS settings for backlight options.",
                             "solution-5": " If the backlight still doesn't work, it may be a hardware issue."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'keyboard repeating characters' in x.lower())))
        def keyboard_repeating_characters(self):
            self.solution = {"proplem": "Keyboard repeating characters",
                             "solution-1": " Adjust the 'Repeat Delay' and 'Repeat Rate' settings in your operating system's keyboard settings.",
                             "solution-2": " Clean the keyboard to remove any debris under the keys.",
                             "solution-3": " Test the keyboard on another PC to confirm if it's a hardware issue.",
                             "solution-4": " If it's a laptop, update the keyboard driver in Device Manager.",
                             "solution-5": " Replace the keyboard if cleaning and settings adjustments don't resolve the issue."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'keyboard lagging' in x.lower())))
        def keyboard_lagging(self):
            self.solution = {"proplem": "Keyboard lagging or delayed input",
                             "solution-1": " Restart your computer to rule out a software glitch.",
                             "solution-2": " Disconnect other USB devices to reduce potential interference.",
                             "solution-3": " Update the keyboard driver in Device Manager.",
                             "solution-4": " If it's a wireless keyboard, ensure the batteries are charged.",
                             "solution-5": " Test the keyboard on another PC to confirm if it's a hardware issue."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'keyboard not detected' in x.lower())))
        def keyboard_not_detected(self):
            self.solution = {"proplem": "Keyboard not detected by the computer",
                             "solution-1": " Ensure the keyboard is properly connected to the PC.",
                             "solution-2": " Try using a different USB port or PS/2 port.",
                             "solution-3": " Restart your computer to see if the keyboard is detected.",
                             "solution-4": " Check the BIOS/UEFI settings to ensure USB ports are enabled.",
                             "solution-5": " Update the keyboard driver in Device Manager.",
                             "solution-6": " Test the keyboard on another PC to confirm if it's a hardware issue."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'keyboard making noise' in x.lower())))
        def keyboard_making_noise(self):
            self.solution = {"proplem": "Keyboard making noise (e.g., clicking or rattling)",
                             "solution-1": " Clean the keyboard to remove any debris or dust.",
                             "solution-2": " Check if any keys are loose or damaged.",
                             "solution-3": " If it's a mechanical keyboard, consider lubricating the switches.",
                             "solution-4": " Replace the keyboard if the noise persists and is bothersome."
                             }

            # internet Problems#

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'no internet connection' in x.lower())))
        def no_internet_connection(self):
            self.solution = {"proplem": "No internet connection",
                             "solution-1": " Restart your router and modem.",
                             "solution-2": " Check if other devices can connect to the internet.",
                             "solution-3": " Ensure the network adapter is enabled in your PC's settings.",
                             "solution-4": " Update or reinstall the network adapter driver.",
                             "solution-5": " Run the network troubleshooter in your operating system.",
                             "solution-6": " Check for physical issues with the Ethernet or Wi-Fi connection."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'slow internet' in x.lower())))
        def slow_internet(self):
            self.solution = {"proplem": "Slow internet",
                             "solution-1": " Check your internet speed using an online speed test.",
                             "solution-2": " Disconnect other devices that may be using bandwidth.",
                             "solution-3": " Move closer to the router if using Wi-Fi.",
                             "solution-4": " Restart your router and modem.",
                             "solution-5": " Update the firmware on your router.",
                             "solution-6": " Contact your ISP to check for service issues."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'wifi not working' in x.lower())))
        def wifi_not_working(self):
            self.solution = {"proplem": "Wi-Fi not working",
                             "solution-1": " Ensure Wi-Fi is enabled on your PC (check the Wi-Fi button or settings).",
                             "solution-2": " Restart your router and modem.",
                             "solution-3": " Check if other devices can connect to the Wi-Fi.",
                             "solution-4": " Forget the Wi-Fi network on your PC and reconnect.",
                             "solution-5": " Update the network adapter driver.",
                             "solution-6": " Reset your router to factory settings if necessary."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'limited internet access' in x.lower())))
        def limited_internet_access(self):
            self.solution = {"proplem": "Limited internet access",
                             "solution-1": " Restart your router and modem.",
                             "solution-2": " Check if your IP address is configured correctly (use DHCP).",
                             "solution-3": " Update the network adapter driver.",
                             "solution-4": " Run the network troubleshooter in your operating system.",
                             "solution-5": " Reset your TCP/IP stack using the command: `netsh int ip reset`.",
                             "solution-6": " Contact your ISP to check for service issues."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'dns server not responding' in x.lower())))
        def dns_server_not_responding(self):
            self.solution = {"proplem": "DNS server not responding",
                             "solution-1": " Restart your router and modem.",
                             "solution-2": " Change your DNS server to a public DNS like Google DNS (8.8.8.8, 8.8.4.4).",
                             "solution-3": " Flush the DNS cache using the command: `ipconfig /flushdns`.",
                             "solution-4": " Update the network adapter driver.",
                             "solution-5": " Disable any VPN or proxy settings that may interfere with DNS.",
                             "solution-6": " Contact your ISP to check for DNS server issues."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ethernet not working' in x.lower())))
        def ethernet_not_working(self):
            self.solution = {"proplem": "Ethernet not working",
                             "solution-1": " Ensure the Ethernet cable is properly connected to both the PC and the router.",
                             "solution-2": " Try using a different Ethernet cable.",
                             "solution-3": " Restart your router and modem.",
                             "solution-4": " Update the network adapter driver.",
                             "solution-5": " Check if the Ethernet port is enabled in your PC's settings.",
                             "solution-6": " Test the Ethernet connection on another device."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'cannot connect to specific website' in x.lower())))
        def cannot_connect_to_specific_website(self):
            self.solution = {"proplem": "Cannot connect to a specific website",
                             "solution-1": " Check if the website is down using a service like 'isitdownrightnow.com'.",
                             "solution-2": " Clear your browser's cache and cookies.",
                             "solution-3": " Try accessing the website from a different browser or device.",
                             "solution-4": " Flush the DNS cache using the command: `ipconfig /flushdns`.",
                             "solution-5": " Disable any VPN or proxy settings that may interfere with the connection.",
                             "solution-6": " Check your firewall or antivirus settings to ensure they are not blocking the website."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'high ping or latency' in x.lower())))
        def high_ping_or_latency(self):
            self.solution = {"proplem": "High ping or latency",
                             "solution-1": " Restart your router and modem",
                             "solution-2": " Disconnect other devices that may be using bandwidth.",
                             "solution-3": " Use a wired Ethernet connection instead of Wi-Fi for lower latency.",
                             "solution-4": " Check for background applications using internet bandwidth.",
                             "solution-5": " Contact your ISP to check for network congestion or service issues.",
                             "solution-6": " Consider upgrading your internet plan for better performance."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'ip address conflict' in x.lower())))
        def ip_address_conflict(self):
            self.solution = {"proplem": "IP address conflict",
                             "solution-1": " Restart your router and modem",
                             "solution-2": " Release and renew your IP address using the commands: `ipconfig /release` and `ipconfig /renew`.",
                             "solution-3": " Assign a static IP address to your PC if necessary.",
                             "solution-4": " Update the network adapter driver.",
                             "solution-5": " Reset your router to factory settings if the issue persists.",
                             "solution-6": " Contact your ISP for further assistance."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'vpn not working' in x.lower())))
        def vpn_not_working(self):
            self.solution = {"proplem": "VPN not working",
                             "solution-1": " Restart your VPN application.",
                             "solution-2": " Check if your internet connection is working without the VPN.",
                             "solution-3": " Update the VPN application to the latest version.",
                             "solution-4": " Try connecting to a different VPN server.",
                             "solution-5": " Disable any firewall or antivirus software that may be blocking the VPN.",
                             "solution-6": " Contact your VPN provider for further assistance."
                             }

            # Boot & OS  Problems#

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'pc won\'t boot' in x.lower())))
        def pc_wont_boot(self):
            self.solution = {"proplem": "PC won't boot",
                             "solution-1": " Ensure the power cable is properly connected to the PC and the wall outlet.",
                             "solution-2": " Check if the power supply unit (PSU) switch is turned on.",
                             "solution-3": " Disconnect all external devices (USB drives, external drives, etc.) and try booting again.",
                             "solution-4": " Check if the BIOS/UEFI recognizes the boot drive.",
                             "solution-5": " Try booting from a different drive or USB.",
                             "solution-6": " If the problem persists, it could be a hardware issue (e.g., faulty PSU, motherboard, or hard drive)."
                             }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'boot loop' in x.lower())))
        def boot_loop(self):
            self.solution = {
                "problem": "Boot loop (PC keeps restarting)",
                "solution-1": "Try booting into Safe Mode (usually by pressing F8 or Shift + F8 during startup).",
                "solution-2": "Uninstall recently installed software or drivers that may be causing the issue.",
                "solution-3": "Run a system repair using your OS installation media.",
                "solution-4": "Restore the system to a previous restore point.",
                "solution-5": "Check for corrupted system files using the command: `sfc /scannow`.",
                "solution-6": "If the issue persists, consider reinstalling the operating system."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'black screen on boot' in x.lower())))
        def black_screen_on_boot(self):
            self.solution = {
                "problem": "Black screen on boot",
                "solution-1": "Ensure the monitor is powered on and properly connected to the PC.",
                "solution-2": "Disconnect all external devices and try booting again.",
                "solution-3": "Boot into Safe Mode and uninstall recently installed drivers or software.",
                "solution-4": "Check if the BIOS/UEFI recognizes the boot drive.",
                "solution-5": "Run a system repair using your OS installation media.",
                "solution-6": "If the problem persists, it could be a hardware issue (e.g., faulty GPU or hard drive)."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'missing operating system' in x.lower())))
        def missing_operating_system(self):
            self.solution = {
                "problem": "Missing operating system",
                "solution-1": "Check if the boot drive is properly connected to the motherboard.",
                "solution-2": "Enter BIOS/UEFI and ensure the correct drive is set as the boot device.",
                "solution-3": "Use your OS installation media to repair the bootloader.",
                "solution-4": "If the drive is not recognized, it may be faulty and need replacement.",
                "solution-5": "Reinstall the operating system if necessary."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'blue screen of death' in x.lower())))
        def blue_screen_of_death(self):
            self.solution = {
                "problem": "Blue Screen of Death (BSOD)",
                "solution-1": "Note the error code displayed on the BSOD and search for its meaning online.",
                "solution-2": "Boot into Safe Mode and uninstall recently installed drivers or software.",
                "solution-3": "Update all device drivers, especially for the GPU, chipset, and storage.",
                "solution-4": "Run a memory diagnostic tool to check for RAM issues.",
                "solution-5": "Check for corrupted system files using the command: `sfc /scannow`.",
                "solution-6": "If the issue persists, consider reinstalling the operating system."
            }

        # Operating System Problems
        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'os running slow' in x.lower())))
        def os_running_slow(self):
            self.solution = {
                "problem": "Operating system running slow",
                "solution-1": "Check for high CPU, memory, or disk usage in Task Manager.",
                "solution-2": "Disable unnecessary startup programs.",
                "solution-3": "Run a disk cleanup to free up space on your system drive.",
                "solution-4": "Defragment the hard drive (if it's an HDD).",
                "solution-5": "Scan for malware using a trusted antivirus program.",
                "solution-6": "Consider upgrading to an SSD for better performance."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'os not updating' in x.lower())))
        def os_not_updating(self):
            self.solution = {
                "problem": "Operating system not updating",
                "solution-1": "Ensure you have a stable internet connection.",
                "solution-2": "Free up space on your system drive (at least 20 GB is recommended).",
                "solution-3": "Run the Windows Update Troubleshooter.",
                "solution-4": "Reset the Windows Update components using the command: `net stop wuauserv`, `net stop bits`, then delete the contents of the `SoftwareDistribution` folder.",
                "solution-5": "Manually download and install the latest updates from the official OS website.",
                "solution-6": "If the issue persists, consider repairing or reinstalling the operating system."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'os crashing or freezing' in x.lower())))
        def os_crashing_or_freezing(self):
            self.solution = {
                "problem": "Operating system crashing or freezing",
                "solution-1": "Check for overheating issues (clean fans and ensure proper ventilation).",
                "solution-2": "Update all device drivers, especially for the GPU and chipset.",
                "solution-3": "Run a memory diagnostic tool to check for RAM issues.",
                "solution-4": "Scan for malware using a trusted antivirus program.",
                "solution-5": "Check for corrupted system files using the command: `sfc /scannow`.",
                "solution-6": "If the issue persists, consider reinstalling the operating system."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'os not recognizing hardware' in x.lower())))
        def os_not_recognizing_hardware(self):
            self.solution = {
                "problem": "Operating system not recognizing hardware",
                "solution-1": "Ensure the hardware is properly connected to the PC.",
                "solution-2": "Check if the hardware is recognized in BIOS/UEFI.",
                "solution-3": "Update the device driver for the hardware.",
                "solution-4": "Uninstall the device from Device Manager and restart the PC to reinstall the driver.",
                "solution-5": "Check for OS updates that may include compatibility fixes.",
                "solution-6": "If the issue persists, the hardware may be faulty or incompatible."
            }

            # CPU Problems

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'os activation issue' in x.lower())))
        def os_activation_issue(self):
            self.solution = {
                "problem": "Operating system activation issue",
                "solution-1": "Ensure you have a stable internet connection.",
                "solution-2": "Enter the correct product key in the OS activation settings.",
                "solution-3": "Run the Activation Troubleshooter in the OS settings.",
                "solution-4": "Contact the OS vendor's support team for assistance.",
                "solution-5": "If the issue persists, consider reinstalling the operating system and activating it again."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(
                  lambda x: any(keyword in x.lower() for keyword in ['overheating', 'cpu hot', 'high temperature']))))
        def cpu_overheating(self):
            self.solution = {
                "problem": "CPU Overheating",
                "solution-1": "Ensure the CPU cooler is properly seated and the fan is working.",
                "solution-2": "Clean dust from the CPU cooler and case vents.",
                "solution-3": "Reapply thermal paste between the CPU and cooler.",
                "solution-4": "Check case airflow and add more fans if necessary.",
                "solution-5": "Avoid overclocking if temperatures are unstable.",
                "solution-6": "Use software like HWMonitor to check temperatures; replace the cooler if needed."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'high cpu usage' in x.lower())))
        def high_cpu_usage(self):
            self.solution = {
                "problem": "High CPU Usage",
                "solution-1": "Open Task Manager (Ctrl+Shift+Esc) to identify resource-heavy processes.",
                "solution-2": "Terminate unnecessary background applications.",
                "solution-3": "Scan for malware using antivirus software.",
                "solution-4": "Update software/drivers causing high CPU load.",
                "solution-5": "Disable startup programs in Task Manager.",
                "solution-6": "Consider upgrading your CPU if usage is consistently high."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'computer not turning on' in x.lower() and 'cpu' in x.lower())))
        def cpu_no_power(self):
            self.solution = {
                "problem": "CPU/PC Not Turning On",
                "solution-1": "Ensure the 8-pin CPU power cable is connected to the motherboard.",
                "solution-2": "Test the power supply unit (PSU) with a different system or tester.",
                "solution-3": "Reset the CMOS battery on the motherboard.",
                "solution-4": "Check for damaged CPU pins on the motherboard socket.",
                "solution-5": "Replace the PSU if it fails to deliver power to the CPU."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(
                  lambda x: any(keyword in x.lower() for keyword in ['unexpected shutdown', 'random shutdown']))))
        def cpu_related_shutdown(self):
            self.solution = {
                "problem": "Unexpected Shutdowns (CPU-Related)",
                "solution-1": "Monitor CPU temperatures to rule out overheating.",
                "solution-2": "Update BIOS/UEFI to the latest version.",
                "solution-3": "Test the system with a different PSU.",
                "solution-4": "Run a stress test (e.g., Prime95) to check CPU stability.",
                "solution-5": "Reseat the CPU and check for physical damage."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'slow performance' in x.lower() and 'cpu' in x.lower())))
        def cpu_performance_issue(self):
            self.solution = {
                "problem": "CPU Performance Issues",
                "solution-1": "Close unnecessary programs to free up CPU resources.",
                "solution-2": "Update BIOS/UEFI and chipset drivers.",
                "solution-3": "Disable overclocking if enabled.",
                "solution-4": "Check for background processes consuming CPU cycles.",
                "solution-5": "Upgrade to a faster CPU if hardware is outdated."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'beep code' in x.lower() or 'post error' in x.lower())))
        def cpu_post_error(self):
            self.solution = {
                "problem": "POST Beep Code (CPU Failure)",
                "solution-1": "Refer to the motherboard manual to decode the beep pattern.",
                "solution-2": "Reseat the CPU and ensure it’s properly installed.",
                "solution-3": "Check for bent pins on the CPU or motherboard socket.",
                "solution-4": "Test the CPU on a compatible motherboard.",
                "solution-5": "Replace the CPU if it’s faulty."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'cpu fan not working' in x.lower())))
        def cpu_fan_issue(self):
            self.solution = {
                "problem": "CPU Fan Not Working",
                "solution-1": "Ensure the fan is connected to the CPU_FAN header on the motherboard.",
                "solution-2": "Clean dust/debris blocking the fan blades.",
                "solution-3": "Replace the fan if it’s not spinning.",
                "solution-4": "Check BIOS settings for fan speed controls.",
                "solution-5": "Use a temporary fan to avoid overheating during troubleshooting."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(
                  problem=P(lambda x: any(keyword in x.lower() for keyword in ['cpu not detected', 'no cpu found']))))
        def cpu_not_detected(self):
            self.solution = {
                "problem": "CPU Not Detected",
                "solution-1": "Reseat the CPU and ensure it’s properly aligned.",
                "solution-2": "Update the motherboard BIOS/UEFI.",
                "solution-3": "Check for compatibility between the CPU and motherboard.",
                "solution-4": "Test the CPU on another compatible motherboard.",
                "solution-5": "Replace the CPU or motherboard if faulty."
            }

            # Mouse Problems

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'mouse not working' in x.lower())))
        def mouse_not_working(self):
            self.solution = {
                "problem": "Mouse not working",
                "solution-1": "Ensure the mouse is properly connected to the PC (USB or PS/2 port).",
                "solution-2": "Try using a different USB port or a different mouse.",
                "solution-3": "Restart your computer to see if the mouse is detected.",
                "solution-4": "Check if the mouse works on another PC to rule out hardware issues.",
                "solution-5": "Update or reinstall the mouse driver in Device Manager.",
                "solution-6": "If it's a wireless mouse, replace or recharge the batteries."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'mouse cursor not moving' in x.lower())))
        def mouse_cursor_not_moving(self):
            self.solution = {
                "problem": "Mouse cursor not moving",
                "solution-1": "Clean the mouse sensor (laser or optical) to remove dust or debris.",
                "solution-2": "Try using the mouse on a different surface or mouse pad.",
                "solution-3": "Restart your computer to rule out a software glitch.",
                "solution-4": "Update the mouse driver in Device Manager.",
                "solution-5": "Test the mouse on another PC to confirm if it's a hardware issue.",
                "solution-6": "Replace the mouse if cleaning and driver updates don't resolve the issue."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'mouse cursor jumping' in x.lower())))
        def mouse_cursor_jumping(self):
            self.solution = {
                "problem": "Mouse cursor jumping or erratic movement",
                "solution-1": "Clean the mouse sensor and ensure the surface is clean and even.",
                "solution-2": "Try using the mouse on a different surface or mouse pad.",
                "solution-3": "Update the mouse driver in Device Manager.",
                "solution-4": "Disconnect other USB devices that may cause interference.",
                "solution-5": "If it's a wireless mouse, ensure the receiver is close to the mouse.",
                "solution-6": "Replace the mouse if the issue persists."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'mouse buttons not working' in x.lower())))
        def mouse_buttons_not_working(self):
            self.solution = {
                "problem": "Mouse buttons not working",
                "solution-1": "Clean the mouse buttons to remove dust or debris.",
                "solution-2": "Test the mouse on another PC to confirm if it's a hardware issue.",
                "solution-3": "Update the mouse driver in Device Manager.",
                "solution-4": "Check the mouse settings in your operating system's control panel.",
                "solution-5": "If it's a gaming mouse, configure the buttons using the manufacturer's software.",
                "solution-6": "Replace the mouse if cleaning and driver updates don't resolve the issue."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'scroll wheel not working' in x.lower())))
        def scroll_wheel_not_working(self):
            self.solution = {
                "problem": "Scroll wheel not working",
                "solution-1": "Clean the scroll wheel to remove dust or debris.",
                "solution-2": "Test the mouse on another PC to confirm if it's a hardware issue.",
                "solution-3": "Update the mouse driver in Device Manager.",
                "solution-4": "Check the mouse settings in your operating system's control panel.",
                "solution-5": "If it's a gaming mouse, configure the scroll wheel using the manufacturer's software.",
                "solution-6": "Replace the mouse if cleaning and driver updates don't resolve the issue."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'wireless mouse not connecting' in x.lower())))
        def wireless_mouse_not_connecting(self):
            self.solution = {
                "problem": "Wireless mouse not connecting",
                "solution-1": "Ensure the mouse has fresh or charged batteries.",
                "solution-2": "Check if the USB receiver is properly plugged into the PC.",
                "solution-3": "Press the 'Connect' button on the mouse and receiver (if applicable).",
                "solution-4": "Restart your computer and try reconnecting the mouse.",
                "solution-5": "Update the mouse driver in Device Manager.",
                "solution-6": "Try using the mouse on another PC to rule out a hardware issue."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'mouse lagging' in x.lower())))
        def mouse_lagging(self):
            self.solution = {
                "problem": "Mouse lagging or delayed input",
                "solution-1": "Restart your computer to rule out a software glitch.",
                "solution-2": "Disconnect other USB devices to reduce potential interference.",
                "solution-3": "Update the mouse driver in Device Manager.",
                "solution-4": "If it's a wireless mouse, ensure the batteries are charged.",
                "solution-5": "Test the mouse on another PC to confirm if it's a hardware issue.",
                "solution-6": "Replace the mouse if the issue persists."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'mouse not detected' in x.lower())))
        def mouse_not_detected(self):
            self.solution = {
                "problem": "Mouse not detected by the computer",
                "solution-1": "Ensure the mouse is properly connected to the PC.",
                "solution-2": "Try using a different USB port or PS/2 port.",
                "solution-3": "Restart your computer to see if the mouse is detected.",
                "solution-4": "Check the BIOS/UEFI settings to ensure USB ports are enabled.",
                "solution-5": "Update the mouse driver in Device Manager.",
                "solution-6": "Test the mouse on another PC to confirm if it's a hardware issue."
            }

            # Audio Problems

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'no sound' in x.lower())))
        def no_sound(self):
            self.solution = {
                "problem": "No sound",
                "solution-1": "Ensure the speakers or headphones are properly connected to the PC.",
                "solution-2": "Check if the volume is muted or turned down in the system settings.",
                "solution-3": "Restart your computer to rule out a software glitch.",
                "solution-4": "Update or reinstall the audio driver in Device Manager.",
                "solution-5": "Test the speakers or headphones on another device to rule out hardware issues.",
                "solution-6": "Check the audio settings in your operating system to ensure the correct output device is selected."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'distorted sound' in x.lower())))
        def distorted_sound(self):
            self.solution = {
                "problem": "Distorted sound",
                "solution-1": "Check the audio cable for damage or loose connections.",
                "solution-2": "Test the speakers or headphones on another device to rule out hardware issues.",
                "solution-3": "Update the audio driver in Device Manager.",
                "solution-4": "Adjust the sound quality settings in your operating system.",
                "solution-5": "Disable any audio enhancements in the sound settings.",
                "solution-6": "If using external speakers, ensure they are not placed near magnetic interference."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'audio crackling or popping' in x.lower())))
        def audio_crackling(self):
            self.solution = {
                "problem": "Audio crackling or popping",
                "solution-1": "Check the audio cable for damage or loose connections.",
                "solution-2": "Update the audio driver in Device Manager.",
                "solution-3": "Disable audio enhancements in the sound settings.",
                "solution-4": "Adjust the sample rate and bit depth in the audio settings.",
                "solution-5": "Test the speakers or headphones on another device to rule out hardware issues.",
                "solution-6": "If the issue persists, consider replacing the audio hardware."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'microphone not working' in x.lower())))
        def microphone_not_working(self):
            self.solution = {
                "problem": "Microphone not working",
                "solution-1": "Ensure the microphone is properly connected to the PC.",
                "solution-2": "Check if the microphone is muted in the system settings.",
                "solution-3": "Update or reinstall the audio driver in Device Manager.",
                "solution-4": "Test the microphone on another device to rule out hardware issues.",
                "solution-5": "Check the microphone settings in your operating system to ensure it is set as the default input device.",
                "solution-6": "If using a USB microphone, try a different USB port."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'audio lagging' in x.lower())))
        def audio_lagging(self):
            self.solution = {
                "problem": "Audio lagging or out of sync",
                "solution-1": "Restart your computer to rule out a software glitch.",
                "solution-2": "Update the audio driver in Device Manager.",
                "solution-3": "Adjust the buffer size in the audio settings of your software or operating system.",
                "solution-4": "Disable any audio enhancements in the sound settings.",
                "solution-5": "Test the audio on another device to rule out hardware issues.",
                "solution-6": "If using Bluetooth audio, ensure the device is within range and free from interference."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'no audio after update' in x.lower())))
        def no_audio_after_update(self):
            self.solution = {
                "problem": "No audio after system update",
                "solution-1": "Restart your computer to see if the issue resolves.",
                "solution-2": "Roll back the audio driver to a previous version in Device Manager.",
                "solution-3": "Check the audio settings in your operating system to ensure the correct output device is selected.",
                "solution-4": "Update the audio driver to the latest version.",
                "solution-5": "Run the audio troubleshooter in your operating system.",
                "solution-6": "If the issue persists, consider reinstalling the operating system."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'audio device not detected' in x.lower())))
        def audio_device_not_detected(self):
            self.solution = {
                "problem": "Audio device not detected",
                "solution-1": "Ensure the audio device is properly connected to the PC.",
                "solution-2": "Restart your computer to see if the device is detected.",
                "solution-3": "Update or reinstall the audio driver in Device Manager.",
                "solution-4": "Check the BIOS/UEFI settings to ensure the audio device is enabled.",
                "solution-5": "Test the audio device on another PC to rule out hardware issues.",
                "solution-6": "If the issue persists, consider replacing the audio hardware."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'audio quality poor' in x.lower())))
        def poor_audio_quality(self):
            self.solution = {
                "problem": "Poor audio quality",
                "solution-1": "Check the audio cable for damage or loose connections.",
                "solution-2": "Update the audio driver in Device Manager.",
                "solution-3": "Adjust the sound quality settings in your operating system.",
                "solution-4": "Disable any audio enhancements in the sound settings.",
                "solution-5": "Test the speakers or headphones on another device to rule out hardware issues.",
                "solution-6": "If using external speakers, ensure they are not placed near magnetic interference."
            }

            # Printer Problems

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'printer not printing' in x.lower())))
        def printer_not_printing(self):
            self.solution = {
                "problem": "Printer not printing",
                "solution-1": "Ensure the printer is powered on and connected to the PC.",
                "solution-2": "Check if there is paper in the tray and no paper jams.",
                "solution-3": "Ensure the ink or toner cartridges are not empty.",
                "solution-4": "Restart the printer and the computer.",
                "solution-5": "Update or reinstall the printer driver.",
                "solution-6": "Check the printer queue for any stuck print jobs and clear them."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'printer offline' in x.lower())))
        def printer_offline(self):
            self.solution = {
                "problem": "Printer offline",
                "solution-1": "Ensure the printer is powered on and connected to the network or PC.",
                "solution-2": "Restart the printer and the computer.",
                "solution-3": "Check the printer's network connection (if wireless).",
                "solution-4": "Set the printer as the default printer in your operating system.",
                "solution-5": "Update or reinstall the printer driver.",
                "solution-6": "Check the printer queue for any stuck print jobs and clear them."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'poor print quality' in x.lower())))
        def poor_print_quality(self):
            self.solution = {
                "problem": "Poor print quality",
                "solution-1": "Check if the ink or toner cartridges are low or empty.",
                "solution-2": "Run the printer's built-in cleaning cycle.",
                "solution-3": "Ensure you are using the correct type of paper for the print job.",
                "solution-4": "Check the print settings for quality options.",
                "solution-5": "Clean the print head or toner drum.",
                "solution-6": "Replace the ink or toner cartridges if necessary."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'paper jam' in x.lower())))
        def paper_jam(self):
            self.solution = {
                "problem": "Paper jam",
                "solution-1": "Turn off the printer and unplug it from the power source.",
                "solution-2": "Open the printer and carefully remove any jammed paper.",
                "solution-3": "Check for any small pieces of paper stuck inside the printer.",
                "solution-4": "Reload the paper tray and ensure the paper is aligned correctly.",
                "solution-5": "Restart the printer and try printing again.",
                "solution-6": "If the problem persists, consult the printer's manual or contact support."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'printer not recognized' in x.lower())))
        def printer_not_recognized(self):
            self.solution = {
                "problem": "Printer not recognized",
                "solution-1": "Ensure the printer is properly connected to the PC or network.",
                "solution-2": "Restart the printer and the computer.",
                "solution-3": "Check the USB or network cable for damage.",
                "solution-4": "Update or reinstall the printer driver.",
                "solution-5": "Set the printer as the default printer in your operating system.",
                "solution-6": "If using a network printer, ensure it is connected to the same network as the PC."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'slow printing' in x.lower())))
        def slow_printing(self):
            self.solution = {
                "problem": "Slow printing",
                "solution-1": "Check the print settings and select a lower quality if high quality is not needed.",
                "solution-2": "Ensure the printer is not low on ink or toner.",
                "solution-3": "Restart the printer and the computer.",
                "solution-4": "Clear the printer queue of any large or stuck print jobs.",
                "solution-5": "Update the printer driver.",
                "solution-6": "If using a network printer, ensure the network is not congested."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'printer error code' in x.lower())))
        def printer_error_code(self):
            self.solution = {
                "problem": "Printer error code",
                "solution-1": "Refer to the printer's manual or manufacturer's website for the meaning of the error code.",
                "solution-2": "Restart the printer and the computer.",
                "solution-3": "Check for any paper jams or low ink/toner levels.",
                "solution-4": "Update or reinstall the printer driver.",
                "solution-5": "Reset the printer to factory settings if possible.",
                "solution-6": "Contact the printer's support team for further assistance."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'printer not feeding paper' in x.lower())))
        def printer_not_feeding_paper(self):
            self.solution = {
                "problem": "Printer not feeding paper",
                "solution-1": "Ensure the paper tray is not overfilled or underfilled.",
                "solution-2": "Check for any paper jams and clear them if present.",
                "solution-3": "Clean the paper feed rollers with a lint-free cloth.",
                "solution-4": "Ensure the paper is aligned correctly in the tray.",
                "solution-5": "Restart the printer and try printing again.",
                "solution-6": "If the problem persists, consult the printer's manual or contact support."
            }

            # Program Problems

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'program not responding' in x.lower())))
        def program_not_responding(self):
            self.solution={
                "problem": "Program not responding",
                "solution-1": "Close the program and restart it.",
                "solution-2": "Check for updates to the program and install them.",
                "solution-3": "Restart your computer to clear any temporary issues.",
                "solution-4": "Run the program as an administrator.",
                "solution-5": "Check for conflicting software or drivers.",
                "solution-6": "Reinstall the program if the issue persists."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'program crashes' in x.lower())))
        def program_crashes(self):
            self.solution={
                "problem": "Program crashes",
                "solution-1": "Ensure the program is up to date.",
                "solution-2": "Check for conflicting software or drivers.",
                "solution-3": "Run the program as an administrator.",
                "solution-4": "Check for corrupted program files and reinstall the program.",
                "solution-5": "Update your operating system to the latest version.",
                "solution-6": "Check the program's system requirements to ensure compatibility with your hardware."
            }


        # @Rule(Fact(action='find_problem'),
        #       PCProblem(problem=P(lambda x: 'program not responding' in x.lower())))
        # def program_not_responding(self):
        #     self.solution.update( {"program not responding":{
        #         "problem": "Program not responding",
        #         "solution-1": "Close the program and restart it.",
        #         "solution-2": "Check for updates to the program and install them.",
        #         "solution-3": "Restart your computer to clear any temporary issues.",
        #         "solution-4": "Run the program as an administrator.",
        #         "solution-5": "Check for conflicting software or drivers.",
        #         "solution-6": "Reinstall the program if the issue persists."
        #     }})
        #
        # @Rule(Fact(action='find_problem'),
        #       PCProblem(problem=P(lambda x: 'program crashes' in x.lower())))
        # def program_crashes(self):
        #     self.solution.update({"program crashes" : {
        #         "problem": "Program crashes",
        #         "solution-1": "Ensure the program is up to date.",
        #         "solution-2": "Check for conflicting software or drivers.",
        #         "solution-3": "Run the program as an administrator.",
        #         "solution-4": "Check for corrupted program files and reinstall the program.",
        #         "solution-5": "Update your operating system to the latest version.",
        #         "solution-6": "Check the program's system requirements to ensure compatibility with your hardware."
        #     }})

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'program not installing' in x.lower())))
        def program_not_installing(self):
            self.solution = {
                "problem": "Program not installing",
                "solution-1": "Ensure you have sufficient disk space for the installation.",
                "solution-2": "Run the installer as an administrator.",
                "solution-3": "Disable antivirus software temporarily during installation.",
                "solution-4": "Check for compatibility issues with your operating system.",
                "solution-5": "Download the installer again in case the file is corrupted.",
                "solution-6": "Check the program's system requirements and ensure your PC meets them."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'program not opening' in x.lower())))
        def program_not_opening(self):
            self.solution = {
                "problem": "Program not opening",
                "solution-1": "Restart your computer and try opening the program again.",
                "solution-2": "Check for updates to the program and install them.",
                "solution-3": "Run the program as an administrator.",
                "solution-4": "Reinstall the program if it fails to open.",
                "solution-5": "Check for corrupted system files using the command: `sfc /scannow`.",
                "solution-6": "Ensure your operating system meets the program's requirements."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'program running slow' in x.lower())))
        def program_running_slow(self):
            self.solution = {
                "problem": "Program running slow",
                "solution-1": "Close other programs to free up system resources.",
                "solution-2": "Check for updates to the program and install them.",
                "solution-3": "Increase the program's priority in Task Manager.",
                "solution-4": "Check for background processes consuming CPU or memory.",
                "solution-5": "Upgrade your hardware (e.g., RAM, SSD) if the program is resource-intensive.",
                "solution-6": "Reinstall the program if the issue persists."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'program not updating' in x.lower())))
        def program_not_updating(self):
            self.solution = {
                "problem": "Program not updating",
                "solution-1": "Ensure you have a stable internet connection.",
                "solution-2": "Restart the program and try updating again.",
                "solution-3": "Run the program as an administrator.",
                "solution-4": "Check for sufficient disk space for the update.",
                "solution-5": "Disable antivirus software temporarily during the update.",
                "solution-6": "Manually download and install the update from the program's official website."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'program compatibility issues' in x.lower())))
        def program_compatibility_issues(self):
            self.solution = {
                "problem": "Program compatibility issues",
                "solution-1": "Run the program in compatibility mode for an older version of Windows.",
                "solution-2": "Check for updates to the program that add support for your operating system.",
                "solution-3": "Update your operating system to the latest version.",
                "solution-4": "Use virtualization software to run the program in a compatible environment.",
                "solution-5": "Check the program's system requirements and ensure your PC meets them.",
                "solution-6": "Contact the program's support team for further assistance."
            }

        @Rule(Fact(action='find_problem'),
              PCProblem(problem=P(lambda x: 'program not uninstalling' in x.lower())))
        def program_not_uninstalling(self):
            self.solution = {
                "problem": "Program not uninstalling",
                "solution-1": "Restart your computer and try uninstalling again.",
                "solution-2": "Run the uninstaller as an administrator.",
                "solution-3": "Use a third-party uninstaller tool to remove the program.",
                "solution-4": "Manually delete the program's files and registry entries (advanced users only).",
                "solution-5": "Check for any background processes related to the program and terminate them.",
                "solution-6": "Contact the program's support team for further assistance."
            }

    expert = PCExpertSystem()
    expert.reset()
    expert.run()
    return expert.solution
    # return args
app.run()