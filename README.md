# VIVES Stem festival: workshop programmeren

[OpenCV on web](https://opencv.onweb.dev/)


## Hello world

### The easy way

```python 
print("Hello world")
```

### The long way 

```python
def main():
    print("Hello world")

if __name__ == '__main__':
    main()
```

## Inlezen van de camera


<details><summary><a href="https://Example.com">Solution: inlezen van de camera </a></summary>

````python
import cv2
import numpy as np

def main():
# Open the first available camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print('Error: Could not open camera.')
        return

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if not ret:
            print('Error: Could not read frame.')
            break

        # Display the original frame and the edge-detected frame
        cv2.imshow('Original', frame)
      
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()


````
</details>


## Grijswaardes lezen van video

[Go to Script](python_voorbeelden/2_grijswaarde.py)


## Rood filter

[Go to Script](python_voorbeelden/3_rood_kleur.py)

## Edge detectie

[Go to Script](python_voorbeelden/4_edge_detectie.py)

## Cirkel detectie

[Go to Script](python_voorbeelden/5_cirkel_detectie.py)

## Lijn detectie

[Go to Script](python_voorbeelden/6_lijn_detectie.py)

## Vierkant detectie

[Go to Script](python_voorbeelden/7_vierkant_detectie.py)

## Aruco tags

> ⚠️ **Warning:** Werkt niet in Opencv on web!!

Detectie tag [Go to Script](python_voorbeelden/x_aruco_tag.py)

Detectie tag + afstand [Go to Script](python_voorbeelden/x_aruco_tag_distance.py)


## Glimlach detectie

> ⚠️ **Warning:** Werkt niet in Opencv on web!!

Glimlach detectie  [Go to Script](python_voorbeelden/x_smile.py)





