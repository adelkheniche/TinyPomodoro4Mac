import objc
from Foundation import NSObject
from AppKit import (
    NSApplication,
    NSStatusBar,
    NSMenu,
    NSMenuItem,
    NSVariableStatusItemLength
)
import os
import threading
import time

class PomodoroTimerApp(NSObject):
    def init(self):
        self = objc.super(PomodoroTimerApp, self).init()
        self.work_time = 1500  # Work time in seconds (demo purpose)
        self.break_time = 300  # Break time in seconds (demo purpose)
        self.remaining_time = self.work_time
        self.is_work_mode = True
        self.timer_thread = None
        self.running = False
        self.status_item = None
        self.cycle_count = 0
        self.max_cycles = 3  # Number of work-break cycles before ending
        return self

    def applicationDidFinishLaunching_(self, notification):
        # Initialize the status bar item
        self.status_item = NSStatusBar.systemStatusBar().statusItemWithLength_(
            NSVariableStatusItemLength
        )
        self.status_item.button().setTitle_("Ready")  # Static part
        self.status_item.setMenu_(self.create_menu())
        self.update_status_item(initial=True)

    def create_menu(self):
        # Create a menu for the status bar item
        menu = NSMenu.alloc().init()
        start_pause_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "Start/Pause Timer", "startPauseTimer:", ""
        )
        reset_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "Reset Timer", "resetTimer:", ""
        )
        quit_item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(
            "Quit", "terminate:", ""
        )

        menu.addItem_(start_pause_item)
        menu.addItem_(reset_item)
        menu.addItem_(quit_item)
        return menu

    def play_sound(self):
        # Play three beeps without delay
        for _ in range(3):
            os.system("afplay /System/Library/Sounds/Tink.aiff")

    def update_status_item(self, initial=False):
        if initial:
            static_text = "Ready"
            dynamic_text = "25:00"  # Dynamic part
        elif self.cycle_count >= self.max_cycles:
            static_text = "End"
            dynamic_text = ""  # No dynamic part for End
        else:
            mode = "Focus" if self.is_work_mode else "Break"
            static_text = mode
            minutes, seconds = divmod(self.remaining_time, 60)
            dynamic_text = f"{minutes:02}:{seconds:02}"  # Dynamic part

        # Combine static and dynamic text with fixed formatting
        combined_text = f"{static_text:<6} {dynamic_text}".strip()
        button = self.status_item.button()
        button.setTitle_(combined_text)  # Use tooltip for timer display

    def timer_tick(self):
        while self.running:
            if self.cycle_count >= self.max_cycles:
                self.running = False
                self.update_status_item()
                self.play_sound()
                time.sleep(3)  # Delay before showing "Ready"
                self.update_status_item(initial=True)
                break

            if self.remaining_time > 0:
                self.remaining_time -= 1
                self.update_status_item()
                time.sleep(1)
            else:
                if not self.is_work_mode:
                    self.cycle_count += 1
                self.is_work_mode = not self.is_work_mode
                if self.cycle_count < self.max_cycles:
                    self.remaining_time = self.work_time if self.is_work_mode else self.break_time
                self.play_sound()
                self.update_status_item()

    @objc.typedSelector(b"v@:@")
    def startPauseTimer_(self, sender):
        if self.cycle_count >= self.max_cycles:
            self.cycle_count = 0
            self.remaining_time = self.work_time
            self.is_work_mode = True
            self.running = False
            self.update_status_item(initial=True)

        if self.running:
            self.running = False
            if self.timer_thread:
                self.timer_thread.join()  # Wait for the thread to finish
                self.timer_thread = None
        else:
            self.running = True
            self.timer_thread = threading.Thread(target=self.timer_tick)
            self.timer_thread.daemon = True  # Ensure the thread doesn't block app exit
            self.timer_thread.start()

    @objc.typedSelector(b"v@:@")
    def resetTimer_(self, sender):
        self.running = False
        if self.timer_thread:
            self.timer_thread.join()
            self.timer_thread = None

        self.is_work_mode = True
        self.remaining_time = self.work_time
        self.cycle_count = 0
        self.update_status_item(initial=True)

if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    delegate = PomodoroTimerApp.alloc().init()
    app.setDelegate_(delegate)
    app.run()
