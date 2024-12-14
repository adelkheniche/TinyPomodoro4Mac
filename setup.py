from setuptools import setup

APP = ['Focus.py']
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',  # Assurez-vous d'avoir un fichier icon.icns dans le même dossier
    'plist': {
        'CFBundleName': 'FOCUS ',
        'CFBundleDisplayName': 'FOCUS POMODORO ',
        'CFBundleShortVersionString': '1.0',
        'CFBundleVersion': '1.0.0',
        'CFBundleIdentifier': 'com.adelk.pomodorotimer',
    }
}

setup(
    name='Focus',
    version='1.0',
    description='A simple Pomodoro timer for macOS',
    author='Adelk',
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
