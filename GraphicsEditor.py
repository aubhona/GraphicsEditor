from tkinter import *
import math


class Polygon(): 
    
    def __init__(self, CenterX, CenterY, NumSides):
        self.CenterX = CenterX # center coordinates of polygon 
        self.CenterY = CenterY
        self.NumSides = NumSides # number of sides of polygon
        
    def draw(self): # drawing a polygon
        ListCoordinates = []
        self.NumSides += 1
        NumSides = self.NumSides
        CenterX = self.CenterX
        CenterY = self.CenterY
        for i in range(NumSides):
            VertexX = CenterX + 50 * math.cos((2 * math.pi * i) / NumSides) # coordinates of the vertices of the polygon
            VertexY = CenterY + 50 * math.sin((2 * math.pi * i) / NumSides)
            ListCoordinates.append((VertexX, VertexY))
        DictObjects[canvas.create_polygon(ListCoordinates)] = self
        
        
def LMBClick(event): # event handler for LMB clicks
    canvas.delete("label")
    CursorX = event.x # cursor coordinates
    CursorY = event.y
    objects = canvas.find_overlapping(CursorX, CursorY, CursorX, CursorY) # polygons on which the cursor is hovered
    if len(objects) == 0:
        Polygon(CursorX, CursorY, 2).draw()
    else:
        for IndexObject in objects:
            canvas.delete(IndexObject)
            DictObjects[IndexObject].draw()
            DictObjects.pop(IndexObject)
                
def clear(event): # the click event handler for the Delete
    global DictObjects
    if DictObjects:
        canvas.delete(ALL)
        DictObjects = {}
    else:
        LabelWarning = canvas.create_text(
            750,
            450,
            anchor = W, 
            text = "ERROR! There aren't figures.",
            tag = "label", 
            font = ("calibri", 30), 
            fill = "#FF0000"
        )
        
        
root = Tk()
canvas = Canvas(root, width = 1500, height = 1000, bg = 'white')
canvas.pack(fill = BOTH)
root.bind('<Button-1>', LMBClick)
root.bind('<Delete>', clear)

DictObjects = {} # dict; object of canvas : object of polygon

root.mainloop()
