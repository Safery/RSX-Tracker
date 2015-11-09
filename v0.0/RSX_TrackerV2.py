import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, \
     AnnotationBbox
from matplotlib.cbook import get_sample_data
import matplotlib.image as mpimg

import numpy as np

fig, ax = plt.subplots()

class RSX_Mapper():
    '''Initiate RSX_Mapper Class'''
    
    def __init__(self, rcord=None, lcord=None):
        '''(RSX_Mapper, [float, float], [float, float]) -> NoneType
        '''
        self.MapName = []
        self.rcord = []
        self.lcord = []
        if ((rcord == None) or (lcord == None)):
            
            cords = get_cord()
            self.rcord = cords[0]
            self.lcord = cords[1]
            return None
        else:
            self.rcord = rcord[0]
            self.lcord = lcord[1]            
            ax.set_xlim(float(lcord[0]),float(rcord[0]))
            ax.set_ylim(float(lcord[1]),float(rcord[1]))
            return None
        
    
    def __str__(self):
        '''(RSX_Mapper) -> str
        '''
        pass
    
    def set_custom_cord(self, rcord, lcord):
        '''
        '''
        ax.set_xlim(float(lcord[0]),float(rcord[0]))
        ax.set_ylim(float(lcord[1]),float(rcord[1]))
        self.lcord = [float(lcord[0]),float(rcord[0])]
        self.rcord = [float(lcord[1]),float(rcord[1])]
        plt.draw()
        plt.show()
        return None
        
    def set_range(self, auto=True, ticks=None):
        '''
        '''
        if (auto == True):
            ax.set_xticks([0.000964875])
            ax.set_yticks([0.000964875])
        else:
            ax.set_xticks([float(ticks)])
            ax.set_yticks([float(ticks)])
            
        return None
    
    def set_img(self, longi=None, lat=None, MapName='map.png', lcord, rcord):
        '''
        '''
        if ((longi == None) or (lat == None)):
            get_inp = input('Must provide Longitude and Latitude [Lat, Longi]\n >>> ')
            longi=get_inp[1]
            lat=[0]
        if (MapName in self.MapName):
            get_inp = input('Map Image already exists. Continue (y/n)?\n >>> ')
            if (get_inp == 'y'):
                img = mpimg.imread("img/"+str(MapName))        
                imagebox = OffsetImage(img, zoom=0.5)
                ab = AnnotationBbox(imagebox,
                                    (longi, lat), xybox=(0, 0),
                                    xycoords='data',
                                    boxcoords="offset points",
                                    pad=0, frameon=False)
                self.MapName.append("img/"+str(MapName))
                ax.add_artist(ab)
                plt.draw()                
            else:
                return 'No Map Image added.'
        else:
            '''img = mpimg.imread("img/"+str(MapName))        
            imagebox = OffsetImage(img, zoom=0.5)
            ab = AnnotationBbox(imagebox, (longi, lat),
                                xybox=(0, 0),
                                xycoords='data',
                                boxcoords="offset points", pad=0, frameon=False)                


            self.MapName.append("img/"+str(MapName))            
            ax.add_artist(ab)
            plt.draw()
            '''
            img = mpimg.imread("img/"+str(MapName))
            plt.imshow(img, extent = [float(lcord[0]),float(rcord[0]),float(lcord[1]),float(rcord[1])])
            plt.show()
            
            
    
def get_cord():
    '''
    '''
    # Gets the top right Coordinate (Longitude and Latitude)
    _top_rcord = []
    get_input = raw_input('What is the top right Coordinate?\n>>> ')
    
    _top_rcord.append(get_input[:int(str(get_input.find(',')))])
    _top_rcord.append(get_input[int(str(get_input.find(',')))+1:])
    
    # Gets the bottom left Coordinate (Longitude and Latitude)
    _bottom_rcord = []
    get_input = raw_input('What is the bottom left Coordinate?\n>>> ')
    
    _bottom_rcord.append(get_input[:int(str(get_input.find(',')))])
    _bottom_rcord.append(get_input[int(str(get_input.find(',')))+1:])    
    

    
    # Sets the axis length
    ax.set_xlim(float(_bottom_rcord[0]),float(_top_rcord[0]))
    ax.set_ylim(float(_bottom_rcord[1]),float(_top_rcord[1]))
    
    return [_top_rcord, _bottom_rcord]

