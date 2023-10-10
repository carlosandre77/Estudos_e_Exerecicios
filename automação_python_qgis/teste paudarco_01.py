from qgis.core import QgsExpression, QgsVectorLayer, QgsProject, QgsMapLayer

project= QgsProject.instance()

base_proj=('pau_darco')
layer_nome = "bairro_paudarco"

## Obter uma lista de todas as camadas atuais
layers = QgsProject.instance().mapLayers().values()
print(layers)


## Loop sobre todas as camadas atuais e imprimir seus nomes

for layer in layers:
    if layer.name() == 'bairros':
        lay_bairros = QgsProject.instance().mapLayersByName(layer.name())[0]
        print(lay_bairros.name())
        
    if layer.name() == 'lotes':
        lay_lotes = QgsProject.instance().mapLayersByName(layer.name())[0]
        print(lay_lotes.name())
        
    if layer.name() == 'quadras':
        lay_quadras = QgsProject.instance().mapLayersByName(layer.name())[0]
        print(lay_quadras.name())
        
    if layer.name() == 'edificacoes':
        lay_edificacoes = QgsProject.instance().mapLayersByName(layer.name())[0]
        print(lay_edificacoes.name())
        
    if layer.name() == 'logradouros':
        lay_logradouros = QgsProject.instance().mapLayersByName(layer.name())[0]
        print(lay_logradouros.name())
        
    if layer.name() == 'confrontantes':
        lay_confrontantes = QgsProject.instance().mapLayersByName(layer.name())[0]
        print(lay_confrontantes.name())



### alterar campos 
campo_area = "area_m2"
campo_perimetro = "perimetro"

lay_bairros.startEditing()

## adicionar campos
lay_bairros.addAttribute(QgsField(str(campo_area),QVariant.Double))
lay_bairros.addAttribute(QgsField(str(campo_perimetro),QVariant.Double))
lay_bairros.addAttribute(QgsField(str("qtd_quadr"),QVariant.Int))
lay_bairros.addAttribute(QgsField(str("qtd_lote"),QVariant.Int))
lay_bairros.addAttribute(QgsField(str("qtd_edific"),QVariant.Int))



i = 0
for feature in lay_bairros.getFeatures():
        id = feature.id()
        ##instanciando os campos de cada layer
        campos_bairros = lay_bairros.fields()
        campos_qudras = lay_bairros.fields()
        geom = feature.geometry()
        indice_campo_area = campos.indexFromName(str(campo_area))
        indice_campo_perimetro = campos.indexFromName(str(campo_perimetro))
        indice_campo_qtd_quadr = campos.indexFromName("qtd_quadr")
        indice_campo_qtd_lote = campos.indexFromName("qtd_lote")
        indice_campo_qtd_edificacao = campos.indexFromName("qtd_edific")
        indice_campo_area_quadra = campos.indexFromName("area_quadr")
        
        ##calcular area
        area = QgsDistanceArea().measureArea(geom)
        ##calcular o perimetro
        perimetro = QgsDistanceArea().measurePerimeter(geom)
        
        ##alterar os atributos
        lay_bairros.changeAttributeValue(id,indice_campo_area,area)
        lay_bairros.changeAttributeValue(id,indice_campo_perimetro,perimetro)
        lay_bairros.changeAttributeValue(id,indice_campo_qtd_quadr,lay_quadras.featureCount())
        lay_bairros.changeAttributeValue(id,indice_campo_qtd_lote,lay_lotes.featureCount())
        lay_bairros.changeAttributeValue(id,indice_campo_qtd_edificacao,lay_edificacoes.featureCount())
        lay_bairros.changeAttributeValue(id,indice_campo_area_quadra,perimetro)
        i += 1
        

campos = lay_quadras.fields()
geom = feature.geometry()
area = QgsDistanceArea().measureArea(geom)
lay_bairros.changeAttributeValue(0,12,QgsExpression('$area'))
print(campos.indexFromName)

area_total = 0
area_f = 0
i=0
for feature in lay_quadras.getFeatures():
    campos_qudras = lay_bairros.fields()
    geom = feature.geometry()
    area_f= QgsDistanceArea().measureArea(geom)
    area_total += area_f
    i+=1

print(area_total)
    
