# Color_wheel

We may need to generate color wheels for different purposes.<br>
I've created a program which can create a variety of color wheels for any need. Because color is represented by 3 channels - hue (color), saturation (how greyish the color is) and value (how bright the color is, luminosity of a color), we can represent independently in 2D only two channels. <br>
<br>
While instantiating object we can if we want to have transitioned from black to grey if we want to change only luminosity or saturation of wheel or both of them. If grey_wheel setting is true than luminosity and saturation values are False by default.
```
wheel =  color_wheel(luminosity=False, saturation=False, grey_wheel = False)
```
To get an image pixel values we can call method draw_wheel. It returns PIL.Image.Image object. Step - how many changes of luminocity and/or saturation we want, shades - how many different hues we want. <br>
Luminocity value - 0 means no light, everything is black, 1 - the brightes colors. <br>
Saturation_value - 0 means everythin is white, 1 - no change to colors.
```
wheel.draw_wheel(step = 6,shades = 12,luminocity_value = 1,saturation_value = 1)
```
To show image on a screen:
```
import matplotlib.pyplot as plt 

plt.figure(figsize=(10,10))
plt.axis("off")
plt.imshow(wheel.draw_wheel(step=15,shades=12))
plt.show()
```
Also, we can get dictionary of rgb values, with hue angles as keys with list of rgb values of hues for this angle
```
rgb = wheel.get_rgb()
```
