project = QgsProject.instance()
path = os.getcwd()+ '/cursos/pyqgis/seção 4/dados/'
path_layer = path + '/aeroportos.shp'
layer = QgsVectorLayer(path_layer,"aeroportos","ogr")
project.addMapLayer(layer)

layer.startEditing()
campos=layer.fields().names()
i=int(0)
for campos in campos:

    if campos == 'y' :
        layer.deleteAttribute(i)
        print(campos,i)
    i += 1


layer.startEditing()
layer.addAttribute(QgsField('x',QVariant.String))
layer.addAttribute(QgsField('y',QVariant.String))
for feature in layer.getFeatures():
        id = feature.id()
        x = feature.geometry().asPoint()[0]
        attr_value = {14:x}
        layer.changeAttributeValues(id,attr_value)
        
for feature in layer.getFeatures():
        id = feature.id()
        y = feature.geometry().asPoint()[1]
        attr_value = {15:y}
        layer.changeAttributeValues(id,attr_value)
        
#selecionar por expressão
layer.selectByExpression("TipoAero = 'Nacional'",QgsVectorLayer.SetSelection)
layer.invertSelection()
layer.selectByExpression("nome iLike 'N%'",QgsVectorLayer.RemoveFromSelection)
layer.selectByExpression("nome iLike 'N%'",QgsVectorLayer.AddToSelection)
layer.removeSelection()

selection = layer.selectedFeatures()
for feature in selection:
    print(feature.attributes())

layer.startEditing()
layer.addAttribute(QgsField('executor',QVariant.String,'text',255))
layer.commitChanges()

layer.startEditing()
for feature in selection:
    id = feature.id()
    layer.changeAttributeValue(id,14,'newmar')


layer.commitChanges()
    



# Importe as classes necessárias
from qgis.core import QgsExpression, QgsFeatureRequest

# Avalie a expressão que será usada para atualizar os atributos
expression = QgsExpression('"executor" + 1')

# Defina quais recursos serão atualizados
request = QgsFeatureRequest().setFilterExpression('"executor" ')
layer = iface.activeLayer() # substitua pelo nome da camada desejada, se necessário
features = layer.getFeatures(request)

# Atualize os atributos dos recursos selecionados
layer.startEditing()
for feature in features:
    feature["executor"] = expression.evaluate(feature)
    layer.updateFeature(feature)
layer.commitChanges()


path = os.getcwd()+ '/cursos/pyqgis/seção 4/dados/'

for root, directory, files in os.walk(path):
    for file in files:
        if file.endswith('.shp'):
           path_vector = os.path.join(path,file)
           layer = QgsVectorLayer(path_vector,file[0:-4],"ogr")
           QgsProject.instance().addMapLayer(layer)

aeroportos = QgsProject.instance().mapLayersByName("aeroportos")[0]
municipios = QgsProject.instance().mapLayersByName("municipios")[0]
rodovias = QgsProject.instance().mapLayersByName("rodovias")[0]

d= QgsDistanceArea()
d.setEllipsoid("GRS80")

print(municipios)
count = 0
for feature in municipios.getFeatures():
    if count < 5:
        municipio = feature["municipio"]
        geom = feature.geometry()
        area = d.measureArea(geom)
        areaha = d.convertAreaMeasurement(area,QgsUnitTypes.AreaHectares)
        perimeter = d.measurePerimeter(geom)
        print(municipio)
        print('Area m2: ', area)
        print('Area Ha: ', areaha)
        print('Perimetro: ',perimeter)
        print(municipio)
        count += 1
    else:
        break

#distancia entre pontos
aeroportos.selectByExpression("FID_1 in (2411,2425)",QgsVectorLayer.SetSelection)
selected = aeroportos.selectedFeatures()

pontos = []
for feature in selected:
    municipio = feature["nm_municip"]
    geom = feature.geometry()
    pontos.append([municipio,geom.asPoint()])
    print(pontos)
    
distancia = d.measureLine(pontos[0][1], pontos[1][1])
 