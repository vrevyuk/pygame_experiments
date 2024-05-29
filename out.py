import pygame
import time
import os

DEBUG = True


class PyScope:
    screen = None;

    def __init__(self):
        os.environ["SDL_FBDEV"] = "/dev/fbt"
        os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"  # Use touchscreen instead of event0
        os.environ["SDL_MOUSEDRV"] = "TSLIB"

        # Based on "Python GUI in Linux frame buffer"
        # http://www.karoltomala.com/blog/?p=679
        disp_no = os.getenv("DISPLAY")
        if disp_no:
            if DEBUG:
                print("I'm running under X display = {0}".format(disp_no))

        # Check which frame buffer drivers are available
        # Start with fbcon since directfb hangs with composite output
        drivers = ['x11', 'fbcon', 'directfb', 'svgalib']
        found = False
        # for driver in drivers:
        #     if not os.getenv('SDL_VIDEODRIVER'):
        #         os.putenv('SDL_VIDEODRIVER', driver)
        #     # try:
        #     #     pygame.display.init()
        #     # except pygame.error:
        #     #     if DEBUG:
        #     #         print('Driver: {0} failed.'.format(driver))
        #     #     os.putenv('SDL_VIDEODRIVER', '')
        #     #     continue
        #     found = True
        #     break

        if not found:
            print('No suitable video driver found!')
            # exit(1)

        pygame.init()

        size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
        if DEBUG:
            print("Framebuffer size: %d x %d" % (size[0], size[1]))
        self.screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        # Clear the screen to start
        self.screen.fill((100, 100, 100))
        # Initialise font support
        pygame.font.init()
        # Render the screen
        pygame.display.update()

    def __del__(self):
        pygame.display.quit()

    def test(self):
        # Fill the screen with red (255, 0, 0)
        red = (255, 0, 0)
        self.screen.fill(red)
        # Update the display
        pygame.display.update()


def main():
    pyscope = PyScope()
    pyscope.test()
    time.sleep(4)


if __name__ == "__main__":
    main()
