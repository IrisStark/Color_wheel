from PIL import Image
import colorsys
import math
import numpy as np

class color_wheel():
    def __init__(self,grey_wheel=False,luminocity = False,saturation = False):
        self.luminocity=luminocity
        self.saturation=saturation
        self.rgb_dict={}
        self.grey_wheel=grey_wheel
        

        
    def draw_wheel(self,step = 6,shades = 12,luminocity_value = 1,saturation_value = 1):
        
        #catching if somebody put shades 0 or step 1 and we get division by zero exception
        if shades==0:
            shades=1
        if step==1:
            self.luminocity=False
            self.saturation=False
        
        im = Image.new("RGB", (300,300),(255,255,255))
        radius = min(im.size)/2
        centre = im.size[0]/2, im.size[1]/2
        pix = im.load()

        
        if self.grey_wheel==True:
            self.saturation=False
            saturation_value=0
            shades=1
            self.luminocity=True
        #create dictioanary with luminocity ranges
        lum_dict = {}
        if self.luminocity == True:
            step_length = radius/step
            if self.grey_wheel==False:
                lum_range = 1, 0.25
            else:
                lum_range = 1,0
            lum_vals = np.round(np.arange(lum_range[1],lum_range[0]+(lum_range[0]-lum_range[1])/(step-1),
                                          (lum_range[0]-lum_range[1])/(step-1)),4)
            lum_vals = reversed(lum_vals)
            start=0
            for lum in lum_vals:
                lum_dict[lum]=(start,start+step_length)
                start+=step_length

        #create dictioanary with saturation ranges
        sat_dict = {}
        if self.saturation == True:
            step_length = radius/step
            sat_range = 1, 0.0
            sat_vals = np.round(np.arange(sat_range[1],sat_range[0]+(sat_range[0]-sat_range[1])/(step-1),
                                          (sat_range[0]-sat_range[1])/(step-1)),4)
            start=0
            for sat in sat_vals:
                sat_dict[sat]=(start,start+step_length)
                start+=step_length    

        #create dictionary to hold hue ranges
        angle_vals = np.round(np.arange(0,1,1/shades),4) 
        angle_dict = {}
        start=0
        for angle in angle_vals:
            angle_dict[angle]=(start/360,(start+360/shades)/360)
            start+=360/shades
            
        #creating dictionary to hold rgb wedges 
        for angle in angle_vals:
            self.rgb_dict[angle]=[]
    #getting colors of pixels
        for x in range(im.width):
            for y in range(im.height):
                #find point
                rx = x - centre[0]
                ry = y - centre[1]
                l = (rx**2 + ry**2)**0.5

                #for points within circle
                if l/radius<=1:
                    if self.luminocity == True:
                        lum=0
                        for key, value in lum_dict.items():
                            if value[0] <= l < value[1]:
                                lum=key

                    else:
                        lum = luminocity_value

                    if self.saturation == True:
                        sat=0
                        for key, value in sat_dict.items():
                            if value[0] <= l < value[1]:
                                sat=key                
                    else:
                        sat = saturation_value 
                        
                    point_angle = ((math.atan2(ry, rx) / math.pi) + 1.0) / 2.0
                    
                    h=0
                    #color wedges
                    for key, value in angle_dict.items():
                        if value[0] <= point_angle < value[1]:
                            h=key
                            
                  
                    rgb = colorsys.hsv_to_rgb(h, sat, lum)
                    pix[x,y] = tuple([int(round(c*255.0)) for c in rgb])
                    if l/radius!=1:
                        self.rgb_dict[h].append(pix[x,y])
        return im
    
    def get_rgb(self):
        for key, value in self.rgb_dict.items():
            self.rgb_dict[key]=list(set(value))
        return self.rgb_dict
    
