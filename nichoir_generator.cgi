#!/usr/bin/python
# must be in 705 permission
import sdxf
import cgi, cgitb 
import os

form = cgi.FieldStorage() 

# Get data from fields
hauteur = form.getvalue('hauteur')
largeur  = form.getvalue('largeur')
trou  = form.getvalue('trou')

print "Content-type: text/html\n\n"
print "<html><head><title>Nichoir Generator</title></head><body>\n"
print "<p>Nichoir Generator</p>\n"
print "</body></html>\n"
d=sdxf.Drawing()
#d.append(sdxf.Text("Hello World!",point=(3,0,1))) #generer du texte
#d.append(sdxf.Line(points=[(0,0,0),(1,1,1)])) #une ligne
linePoints = [(0,0),(0,hauteur),(largeur,hauteur),(largeur,0)] #tableau de points
d.append(sdxf.LwPolyLine(points=linePoints,flag=1)) #generation d'une polyligne
linePoints = [(0,hauteur),(int(largeur)/2,int(hauteur)+int(hauteur)/2),(largeur,hauteur)] #tableau de points
d.append(sdxf.LwPolyLine(points=linePoints,flag=1,color=3)) #generation d'une polyligne
d.append(sdxf.Arc(center=(int(largeur)/2,int(hauteur)/2),radius=trou,startAngle=0,endAngle=360)) # un cercle
d.saveas("beau_nichoir.dxf")
print """

 <a href="http://moumoute.biz/nichoir_generator/beau_nichoir.dxf">Telechargez votre nichoir</a>  <br>

"""
