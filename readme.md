# **Bot for GuitarFlash 3**

## **Introduction**

The bot was designed specifically to function on a 1080p screen. Any deviation from this resolution or a different version of GuitarFlash 3 may require adjustments to the pixel coordinates for each key.

**Note:** Pixel adjustments might be necessary if the "Fretboard" inclination isn't set to its lowest position.

## **Functionality**

The bot operates as follows:

1. It continuously monitors 5 pre-determined pixel in a semi-infinite loop. Each Pixel is monitored by a separeted process
2. The monitoring loop can be interrupted by pressing the "p" key on the keyboard.
3. Under normal conditions, these pixels appear as black and on this state the bot does nothing.
4. When the color of these pixel changes, it is interpreted as the presence of a music note over the corresponding game key.
5. Subsequently, the bot virtually triggers the corresponding key press action.
6. The standart keys are A, S, J, K, L.


## **Additional Information**

Please note that due to the specific configuration required for GuitarFlash 3 and screen resolution dependencies, adjustments may be necessary to ensure accurate key recognition and gameplay.
