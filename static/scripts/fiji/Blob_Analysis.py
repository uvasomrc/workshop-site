from ij import IJ

imp = IJ.openImage("http://imagej.nih.gov/ij/images/blobs.gif")
IJ.run(imp, "Median...", "radius=2")
IJ.run(imp, "Options...", "iterations=1 count=1 black")
IJ.setAutoThreshold(imp, "Default")
IJ.run(imp, "Convert to Mask", "")
IJ.run(imp, "Watershed", "")
IJ.run(imp, "Set Measurements...", "area mean min centroid integrated display redirect=None decimal=3")
IJ.run(imp, "Analyze Particles...", "size=50-Infinity display exclude clear summarize add")
imp.show()
