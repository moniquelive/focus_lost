import time

from AppKit import NSWorkspace


def main():
    while True:
        time.sleep(3)
        activeAppName = NSWorkspace.\
            sharedWorkspace().\
            activeApplication()['NSApplicationName']
        print(f'App In Focus: {activeAppName}')


if __name__ == "__main__":
    main()
