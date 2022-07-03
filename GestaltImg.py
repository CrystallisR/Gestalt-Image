# CRYSTALLIS 2022
# generate images which satisfy or dissatisfy Gestalt principle

import numpy as np
import matplotlib.pyplot as plt
import random

class Gestalt(object):
    
    def __init__(self) -> None:
        pass
    
    def genPositiveImg():
        pass
    
    def genNegativeImg():
        pass
    
class Continuity(Gestalt):
    '''
    generate images which satisfy or dissatisfy Gestalt continuity principle
    
    parameters
    ----------
    num_range : range of numbers of lines or curves 
    img_sz : width & height ratio of the image
    dpi : resolution
    msz : marker size
    intensity : the degree of noise intended to add to negative images
    colors : list of colors
    markers : list of various types of marker (of points)

    '''
    
    def __init__(self, num_range = (2, 5), img_sz = (1, 1), dpi = 128, msz = 10, 
                intensity = 1.0, colors = np.array(["black"]), markers = np.array(["."])) -> None:
        super().__init__()
        self.colors = colors
        self.markers = markers
        self.num_range = num_range
        self.img_sz = img_sz
        self.dpi = dpi
        self.msz = msz   
        self.intensity = intensity
       
    def genPositiveImg(self, path):
        '''
        generate positive image, which means that it satisfies Gestalt continuity principle
        
        image contents : scattered points which seems like curves if connected

        '''
        self.__genImg(path, False)
 
    def genNegativeImg(self, path):
        '''
        generate negative image, which means that it dissatisfies Gestalt continuity principle
        
        image contents : scattered points which seems like nothing if connected (disordered)

        '''
        self.__genImg(path, True)
        
    def genPositiveImgSamples(self, path, plots=(5, 5)):
        '''
        generate multiple positive images, for display

        '''
        self.__genImgSamples(path, False, plots)
        
    def genNegativeImgSamples(self, path, plots=(5, 5)):
        '''
        generate multiple pnegative images, for display

        '''
        self.__genImgSamples(path, True, plots)
        
    # <------------------------------------------------------------->
    # | The functions below are necessary in the case of continuity |
    # <------------------------------------------------------------->
    
    def __genImg(self, path, isN):
        '''
        prototype for generating both positive & negative image
        
        parameters
        ----------
        path : where to save the image
        isN : whether generate negative image
        
        '''
        colors, markers, num_range, img_sz, dpi, msz = \
        self.colors, self.markers, self.num_range, self.img_sz, self.dpi, self.msz
        c_num, m_num, num = len(colors), len(markers), random.randint(self.num_range[0], self.num_range[1])
        plt.figure(figsize=img_sz, dpi=dpi)
        fg = True if random.randint(0,1) == 1 else False
        x_list, y_list = self.__setPoints(isN, rev=fg)
        plt.scatter(x_list, y_list, s=msz, c=colors[random.randint(0, c_num-1)], marker=markers[random.randint(0, m_num-1)])
        if num > 1:
            x_list, y_list = self.__setPoints(isN, rev=(not fg))
            plt.scatter(x_list, y_list, s=msz, c=colors[random.randint(0, c_num-1)], marker=markers[random.randint(0, m_num-1)])
            for _ in range(num-2):
                fg = True if random.randint(0,1) == 1 else False
                x_list, y_list = self.__setPoints(isN, rev=fg)
                plt.scatter(x_list, y_list, s=msz, c=colors[random.randint(0, c_num-1)], marker=markers[random.randint(0, m_num-1)])
        plt.axis('off')
        plt.savefig(path)
        plt.close()
        
    def __genImgSamples(self, path, isN, plots):
        '''
        prototype for generating both positive & negative image massive samples
        
        only used for display
        
        parameters
        ----------
        path : where to save the image
        isN : whether generate negative image
        
        '''
        colors, markers, dpi, msz = self.colors, self.markers, self.dpi, self.msz
        num = random.randint(self.num_range[0], self.num_range[1])
        c_num, m_num = len(colors), len(markers)
        fig = plt.figure(figsize=plots, dpi=dpi)
        rows, cols = plots[0], plots[1]
        for i in range(1, rows*cols+1):
            fig.add_subplot(rows, cols, i)
            fg = True if random.randint(0,1) == 1 else False
            x_list, y_list = self.__setPoints(isN, rev=fg)
            plt.scatter(x_list, y_list, s=msz, c=colors[random.randint(0, c_num-1)], marker=markers[random.randint(0, m_num-1)])
            if num > 1:
                x_list, y_list = self.__setPoints(isN, rev=(not fg))
                plt.scatter(x_list, y_list, s=msz, c=colors[random.randint(0, c_num-1)], marker=markers[random.randint(0, m_num-1)])
                for _ in range(num-2):
                    fg = True if random.randint(0,1) == 1 else False
                    x_list, y_list = self.__setPoints(isN, rev=fg)
                    plt.scatter(x_list, y_list, s=msz, c=colors[random.randint(0, c_num-1)], marker=markers[random.randint(0, m_num-1)])
            plt.axis('off')
        plt.savefig(path)
        plt.close()

    def __setPoints(self, isN, rev=True, p_num=10, funcs=10, n_min=0.6, n_max=1.0):
        '''
        return (x, y) coordinates of a set of points
        
        parameters
        ----------
        isN : whether generate negative image
        rev : whether use the symmetric function of the function generated by randomFunc()
        p_num : maximal point number
        funcs : total number of functions which can be generated by randomFunc()
        n_min & n_max : control the range of numbers of generated points

        '''
        # set total points of a curve & curve type
        tl_pts = random.randint(int(p_num*n_min), int(p_num*n_max))
        x_list = list(range(1, tl_pts+1))
        rd_func = self.__randomFunc(random.randint(0, funcs))
        y_list = [rd_func(x) for x in x_list]
        scale = tl_pts/max(y_list)
        y_list = [y*scale for y in y_list]
        if rev: y_list.reverse()
        if isN: x_list, y_list = self.__addNoise(x_list, y_list)
        return x_list, y_list
    
    def __addNoise(self, x_list, y_list):
        '''
        generate noise; after points are set, adding some noise to make the points more disordered

        '''
        return [x + np.random.normal(scale=self.intensity) for x in x_list],\
                [y + np.random.normal(scale=self.intensity) for y in y_list]
    
    def __randomFunc(self, id):
        '''
        return a curve function y=f(x) by id
        
        parameters
        ----------
        id : can be a randomly generated number
        
        '''
        if id == 0:
            return lambda x : 1
        elif id == 1:
            return lambda x : x
        elif id == 2:
            return lambda x: x**2
        elif id == 3:
            return lambda x: x**0.5
        elif id == 4:
            return lambda x: np.log(x)
        elif id == 5:
            return lambda x: np.exp(x)
        elif id == 6:
            return lambda x: x**2 - 2*x
        elif id == 7:
            return lambda x: x**3 -2*x**2 + x
        elif id == 8:
            return lambda x: np.exp(x) - np.log(x)
        else:
            return lambda x : 1/(1 + np.exp(-x))