# CRYSTALLIS 2022
# generate images which satisfy or dissatisfy Gestalt principle

import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.interpolate import interp1d

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
    
    def __init__(self, num_range = (2, 4),  intensity = 1.0, img_sz = (1, 1), dpi = 128, 
                msz = 10, colors = np.array(["black"]), markers = np.array(["."])) -> None:
        super().__init__()
        self.colors = colors
        self.markers = markers
        self.num_range = num_range
        self.img_sz = img_sz
        self.dpi = dpi
        self.msz = msz   
        self.intensity = intensity
       
    def genPositiveImg(self, path, type= 1):
        '''
        generate positive image, which means that it satisfies Gestalt continuity principle
        
        parameters
        ----------
        type: which type of negative image to generate; two values available now: int (1 / 2)

        '''
        if type == 1:
            self.__genImgType1(path, False)
        elif type == 2:
            self.__genImgType2(path, False)
        elif type == 3:
            self.__genImgType3(path, False)
        else: pass
 
    def genNegativeImg(self, path, type= 1):
        '''
        generate negative image, which means that it dissatisfies Gestalt continuity principle
        
        parameters
        ----------
        type: which type of negative image to generate; two values available now: int (1 / 2)

        '''
        if type == 1:
            self.__genImgType1(path, True)
        elif type == 2:
            self.__genImgType2(path, True)
        elif type == 3:
            self.__genImgType3(path, True)
        else: pass
        
    def genPositiveImgSamples(self, path, plots=(5, 5), type= 1):
        '''
        generate multiple positive images, for display

        '''
        self.__genImgSamples(path, False, plots, type)
        
    def genNegativeImgSamples(self, path, plots=(5, 5), type= 1):
        '''
        generate multiple pnegative images, for display
        
        parameters
        ----------
        type: which type of negative image to generate; two values available now: int (1 / 2)

        '''
        self.__genImgSamples(path, True, plots, type)
        
    # <------------------------------------------------------------->
    # | The functions below are essential tool functions            |
    # <------------------------------------------------------------->
    
    def __genImgType1(self, path, isN):
        '''
        prototype for generating both positive & negative image
        
        parameters
        ----------
        path : where to save the image
        isN : whether generate negative image
        
        '''
        c_num, m_num = len(self.colors), len(self.markers)
        plt.figure(figsize=self.img_sz, dpi=self.dpi)
        x_lists, y_lists = self.__genImgDataType1(isN)
        for i in range(len(x_lists)): 
            plt.scatter(x_lists[i], y_lists[i], s=self.msz, c=self.colors[random.randint(0, c_num-1)], 
                        marker=self.markers[random.randint(0, m_num-1)])
        plt.axis('off')
        plt.savefig(path)
        plt.close()
        
    def __genImgType2(self, path, isN):
        '''
        prototype for generating image type 2
        
        disconnect a continued curve
        
        parameters
        ----------
        path : where to save the image
        isN : whether generate negative image
        
        '''
        plt.figure(figsize=self.img_sz, dpi=self.dpi)
        x_lists, y_lists, crs, mks, szs = self.__setListsType2(isN)
        for i in range(len(x_lists)):
            plt.scatter(x_lists[i], y_lists[i], s=szs[i], c=crs[i], marker=mks[i])
        plt.axis('off')
        plt.savefig(path)
        plt.close()
        
    def __genImgType3(self, path, isN):
        '''
        prototype for generating image type 3
        
        lines and curves
        
        parameters
        ----------
        path : where to save the image
        isN : whether generate negative image
        
        '''
        c_num = len(self.colors)
        plt.figure(figsize=self.img_sz, dpi=self.dpi)
        x_lists, y_lists = self.__genImgDataType3(isN)
        fg = True if random.randint(0,1) == 1 else False
        for i in range(len(x_lists)): 
            if fg:
                plt.plot(x_lists[i], y_lists[i], linewidth=2, c=self.colors[random.randint(0, c_num-1)]) # or linestyle = "dashed"
            else:
                plt.plot(y_lists[i], x_lists[i], linewidth=2, c=self.colors[random.randint(0, c_num-1)]) # or linestyle = "dashed"
        plt.axis('off')
        plt.savefig(path)
        plt.close()

    def __genImgSamples(self, path, isN, plots, type):
        '''
        prototype for generating either positive or negative image massive samples
        
        only used for display
        
        parameters
        ----------
        path : where to save the image
        isN : whether generate negative image
        plots : (x, y) subplots
        
        '''
        c_num, m_num = len(self.colors), len(self.markers)
        fig = plt.figure(figsize=plots, dpi=self.dpi)
        rows, cols = plots[0], plots[1]
        for i in range(1, rows*cols+1):
            fig.add_subplot(rows, cols, i)
            if type == 1:
                x_lists, y_lists = self.__genImgDataType1(isN)
                for i in range(len(x_lists)): 
                    plt.scatter(x_lists[i], y_lists[i], s=self.msz, c=self.colors[random.randint(0, c_num-1)], 
                            marker=self.markers[random.randint(0, m_num-1)])
            elif type == 2:
                x_lists, y_lists, crs, mks, szs = self.__setListsType2(isN)
                for i in range(len(x_lists)):
                    plt.scatter(x_lists[i], y_lists[i], s=szs[i], c=crs[i], marker=mks[i])
            elif type == 3:
                x_lists, y_lists = self.__genImgDataType3(isN)
                fg = True if random.randint(0,1) == 1 else False
                for i in range(len(x_lists)): 
                    if fg:
                        plt.plot(x_lists[i], y_lists[i], linewidth=2, c=self.colors[random.randint(0, c_num-1)]) # or linestyle = "dashed"
                    else:
                        plt.plot(y_lists[i], x_lists[i], linewidth=2, c=self.colors[random.randint(0, c_num-1)]) # or linestyle = "dashed"
            else: pass
            plt.tick_params(axis='both', which='both', bottom=False, left=False, labelbottom=False, labelleft=False)
            # plt.axis('off')
        plt.savefig(path)
        plt.close()
    
    def __genImgDataType1(self, isN, num=None):
        '''
        generate data which is needed for __genImg() and __genImgSample()
        
        return 2 lists of lists (which contain x & y points respectively)
        
        parameters
        ----------
        isN : whether generate negative image
        
        '''
        x_lists, y_lists = [], []
        if not num:
            num = random.randint(self.num_range[0], self.num_range[1])
        fg = True if random.randint(0,1) == 1 else False
        for _ in range(num):
            x_list, y_list = self.__setPointsType1(isN, rev=fg)
            x_lists.append(x_list), y_lists.append(y_list)
            fg = not fg if num==2 else True if random.randint(0,1) == 1 else False
        return x_lists, y_lists

    def __genImgDataType3(self, isN):
        '''
        generate data which is needed for __genImg() and __genImgSample()
        
        return lists for type3 image
        
        parameters
        ----------
        isN : whether generate negative image
        scale: noise added to curves
        
        '''
        # set parameters
        GRAIN = 100
        END = int(GRAIN*0.3)
        SHIFT = 6
        XSHIFT = 0.4
        # <set for pos or neg>
        scale = 0.1 if not isN else 1
        cut = random.randint(6, int(GRAIN*0.1)) if not isN else random.randint(int(GRAIN*0.18), int(GRAIN*0.24))
        # <set for pos or neg>
        cut_point = random.randint(END, GRAIN-END)
        front_end, rear_start = int(cut_point-cut/2), int(cut_point+cut/2)
        fg = True if random.randint(0,1) == 1 else False
        # set curve list
        x_list, y_list = self.__setPointsType1(False, rev=fg)
        # for pos
        y_list = [y + np.random.normal(scale=scale) for y in y_list]
        x, y = np.array(x_list), np.array(y_list)
        cubic_interploation_model = interp1d(x, y, kind = "cubic")
        x_ = np.linspace(x.min(), x.max(), GRAIN)
        y_ = cubic_interploation_model(x_)
        # cut off a part of the curve (for positive images)
        x_f, x_r = x_[:front_end], x_[rear_start:]
        y_f, y_r = y_[:front_end], y_[rear_start:]
        if isN:
            shift = SHIFT if random.randint(0,1) == 1 else -SHIFT
            if fg:
                y_r = [y + shift for y in y_r]
                x_r = [x + XSHIFT for x in x_r]
            else:
                y_f = [y + shift for y in y_f]
                x_f = [x + XSHIFT for x in x_f]
        return [x_f, x_r], [y_f, y_r]
        
    def __setListsType2(self, isN, drop_rate=0.2):
        '''
        setup the point lists for drawing
        
        parameters
        ----------
        drop_rate: the percentage of a part of the points in the curve to be dropped
        
        '''
        x_list_f, x_list_r, y_list1_f, y_list1_r, y_list2_f, y_list2_r = self.__setPointsType2()
        crs, mks, szs, fg = self.__setParamsType2(isN)
        x_list1_f, x_list1_r, x_list2_f, x_list2_r = x_list_f, x_list_r, x_list_f, x_list_r
        drop0 = lambda ls: int(drop_rate*len(ls))
        drop = lambda ls: 1 if drop0(ls) < 1 else drop0(ls)
        if isN:
            if fg:
                x_list1_f, x_list1_r = x_list1_f[:-drop(x_list1_f)], x_list1_r[drop(x_list1_r):]
                y_list1_f, y_list1_r = y_list1_f[:-drop(y_list1_f)], y_list1_r[drop(y_list1_r):]
            else:
                x_list2_f, x_list2_r = x_list2_f[:-drop(x_list2_f)], x_list2_r[drop(x_list2_r):]
                y_list2_f, y_list2_r = y_list2_f[:-drop(y_list2_f)], y_list2_r[drop(y_list2_r):]
        x_lists = [x_list1_f, x_list1_r, x_list2_f, x_list2_r]
        y_lists = [y_list1_f, y_list1_r, y_list2_f, y_list2_r]
        return x_lists, y_lists, crs, mks, szs

    def __setParamsType2(self, isN):
        '''
        set various parameters for image type2
        
        actions
        -------
        1. resize the points before or after cross point
        2. reset the point marker before or after cross point
        3. reset the point color before or after cross point
        4. wipe out some points near the cross point ####
        
        '''
        c_num, m_num = len(self.colors), len(self.markers)
        l1_cf, l2_cf = self.colors[random.randint(0, c_num-1)], self.colors[random.randint(0, c_num-1)]
        l1_mf, l2_mf = self.markers[random.randint(0, m_num-1)], self.markers[random.randint(0, m_num-1)]
        l1_sf, l2_sf = self.msz, self.msz
        l1_cr, l2_cr = l1_cf, l2_cf
        l1_mr, l2_mr = l1_mf, l2_mf
        l1_sr, l2_sr = l1_sf, l2_sf
        fg = True if random.randint(0, 1) else False
        if isN:
            '''
            if fg: # set changing color as essential
                while(l1_cr == l1_cf): l1_cr = self.colors[random.randint(0, c_num-1)]
            else: 
                while(l2_cr == l2_cf): l2_cr = self.colors[random.randint(0, c_num-1)]
            '''
            if fg:
                while(l1_mr == l1_mf): l1_mr = self.markers[random.randint(0, m_num-1)]
                l1_sr = self.msz*2
            else:
                while(l2_mr == l2_mf): l2_mr = self.markers[random.randint(0, m_num-1)]
                l2_sr = self.msz*2
        return [l1_cf, l1_cr, l2_cf, l2_cr], [l1_mf, l1_mr, l2_mf, l2_mr], \
                [l1_sf, l1_sr, l2_sf, l2_sr], fg

    def __setPointsType1(self, isN, rev=True, p_num=10, funcs=10, n_min=0.6, n_max=1.0):
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
        rd_func = self.__randomFuncType1(random.randint(0, funcs))
        y_list = [rd_func(x) for x in x_list]
        scale = tl_pts/max(y_list)
        y_list = [y*scale for y in y_list]
        if rev: y_list.reverse()
        if isN: x_list, y_list = self.__addNoise(x_list, y_list)
        return x_list, y_list
    
    def __setPointsType2(self, p_num=12, funcs=6, n_min=0.6, n_max=1.0):
        '''
        return 4 x_lists, 4 y_lists of 2 crossed curves
        
        parameters
        ----------
        p_num : maximal point number
        funcs : total number of functions which can be generated by randomFunc()
        n_min & n_max : control the range of numbers of generated points

        '''
        # set total points of a curve & curve type
        tl_pts = random.randint(int(p_num*n_min), int(p_num*n_max))
        x_list = list(range(1, tl_pts+1))
        rd_func1 = self.__randomFuncType2(random.randint(0, funcs))
        rd_func2 = self.__randomFuncType2(random.randint(0, funcs))
        y_list1, y_list2 = [rd_func1(x) for x in x_list], [rd_func2(x) for x in x_list]
        scale1, scale2 = tl_pts/max(y_list1), tl_pts/max(y_list2)
        y_list1, y_list2 = [y*scale1 for y in y_list1], [y*scale2 for y in y_list2]
        y_list2.reverse()
        x0 = 0
        for i in range(len(x_list)):
            if y_list1[i] >= y_list2[i]:
                x0 = i
                break
        return x_list[:x0], x_list[x0:], y_list1[:x0], y_list1[x0:], y_list2[:x0], y_list2[x0:]
    
    def __addNoise(self, x_list, y_list):
        '''
        generate noise; after points are set, adding some noise to make the points more disordered

        '''
        return [x + np.random.normal(scale=self.intensity) for x in x_list],\
                [y + np.random.normal(scale=self.intensity) for y in y_list]
    
    def __randomFuncType1(self, id):
        '''
        return a curve function y=f(x) by id
        
        parameters
        ----------
        id : can be a randomly generated number
        
        '''
        if id == 0:
            return lambda x : 5
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
        
    def __randomFuncType2(self, id):
        '''
        an alternate method for randomFunc()
        
        '''
        if id == 0:
            return lambda x : x
        elif id == 1:
            return lambda x : x**2
        elif id == 2:
            return lambda x: x**3
        elif id == 3:
            return lambda x: x**0.5
        elif id == 4:
            return lambda x: np.log(x)
        else:
            return lambda x : 2*x      