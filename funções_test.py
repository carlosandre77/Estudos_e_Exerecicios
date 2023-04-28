def list_files(path,type):
    lst=[]
    for root, directory, files in os.walk(path):
        for file in files:
            if file.endswith(type):
                lst.append(file)
    return lst

def abrir_camadas(path,type):
    files = list_files(path,type)
    vectors = {}
    for file in files:
        filename = file.split('.')[0]
        vector = iface.addVectorLayer(path+file,filename,"ogr")
        vectors.update({filename:vector})
    return vectors

path = ( r'C:\Users\Carlos André-DIGITAL\Documents\digital map - geo\PROJETOS DMG\PAU_DARCO\SHAPES\Nova pasta'.replace('\\', '/')+'/')

print(path)
layers = QgsProject.instance().mapLayers().values()
list_files(layers,'.shp')
abrir_camadas(path,'.shp')