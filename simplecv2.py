import sys
from SimpleCV import Camera, Color
from SimpleCV.Display import Display

def main():
    # Try to connect to the camera.
    cam  = Camera()

    if not cam:
        print 'Error opening camera. Exiting...'
        sys.exit(1)

    # Create PyGame display.
    disp = Display()

    # Main processing loop.
    while not disp.isDone():
        # Get an image from the camera.
        img = cam.getImage()

        faces = img.findHaarFeatures("face.xml")
        i = 0
        if not faces is None:
            for f in faces:
                f.draw(Color.GREEN)

        # Show the camera image.
        img.save(disp)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "\nStopping..."
        sys.exit(1)
