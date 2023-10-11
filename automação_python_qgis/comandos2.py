def list_files(path,tipo):
    lst=[]
    for root,directory,files in os.walk(path):
        for file in files:
            if file.endswith(tipo):
                lst.append(file)
    return lst
print(teste.split('.'))    files = list_files(path,type)
    vectors={}
    for file in files:
        filename = file.split('.')[0]
        vector = iface.addVectorLayer(path+file,filename,'ogr')
        vectors.update({filename:vector})
    return vectors




path = os.getcwd()+ '/cursos/pyqgis/seção 4/dados/'
#list_files(path,'.shp')
camadas = open_vector_layers(path,'gpkg')

for i in camadas['piaui_dissolve'].getFeatures():
    print(i.attributes())