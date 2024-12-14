# TinyPomodoro4Mac

**TinyPomodoro4Mac** is a lightweight Pomodoro timer designed specifically for macOS. This project was created in an afternoon as an experiment to learn how to code with the assistance of ChatGPT. The app resides in the macOS menu bar and helps you manage your work and break cycles effectively.

## Features

- **Simple Pomodoro Timer**: Predefined work (25 minutes) and break (5 minutes) durations.
- **Menu Bar Integration**: Displays the remaining time directly in the menu bar for easy tracking.
- **Intuitive Controls**: Start, pause, and reset the timer with simple menu options.
- **Lightweight and Distraction-Free**: Focus on your tasks without unnecessary distractions.

## Installation

1. **Clone the Repository**: Clone the repository to your local machine:

   ```bash
   git clone https://github.com/USERNAME/TinyPomodoro4Mac.git
   cd TinyPomodoro4Mac
   ```

2. **Install Dependencies**: Ensure you have Python 3 and `py2app` installed:

   ```bash
   pip3 install py2app
   ```

3. **Compile the App**: Use the provided `setup.py` to build the macOS application:

   ```bash
   python3 setup.py py2app
   ```

4. **Run**: The compiled `.app` will be available in the `dist` folder. Move it to your Applications folder for easier access. This is the Apple Silicon version; if you need an Intel-compatible version, ensure you're using the correct Python environment.
3. **Add to Applications** (Optional): Drag and drop the app into your macOS `Applications` folder for easier access.

## How to Use

1. **Launch the App**: Open **TinyPomodoro4Mac** from your Applications folder or directly from the `.app` file.
2. **Access Menu Options**: Click the icon in the menu bar to view the available options:
   - **Start/Pause Timer**: Starts or pauses the Pomodoro session.
   - **Reset Timer**: Resets the timer and cycle count to the initial state.
   - **Quit**: Closes the application.
3. **Track Your Time**: Monitor the countdown directly from the menu bar as you work through your Pomodoro cycles.

## Example Display

```
Focus    25:00
```

or

```
Break    05:00
```

## About This Project

This project was developed in a single afternoon as a learning exercise to understand how to create a basic macOS menu bar application using Python with the help of ChatGPT. The goal was to implement a functional Pomodoro timer that integrates seamlessly with the macOS environment.

## License

Creative Commons Attribution 4.0 International 
