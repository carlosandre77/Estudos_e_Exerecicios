
def list_files(path,type):
    lst=[]
    for root, directory, files in os.walk(path):
        for file in files:
            if file.endswith(type):
                lst.append(file)
                print(lst)
    return lst

def abrir_camadas(path,type):
    files = list_files(path,type)
    vectors = {}
    for file in files:
        filename = file.split('.')[0]
        vector = iface.addVectorLayer(path+file,filename,"ogr")
        vectors.update({filename:vector})
    return vectors
    
def atualizar_bairros():
    layers = QgsProject.instance().mapLayers().values()
    for layer in layers:
        if (layer.name().split('_')[0] == 'bairros' 
        or layer.name().split('_')[0] == 'bairro'):
            lay_bairros = QgsProject.instance().mapLayersByName(layer.name())[0]
            print(lay_bairros.name())
        if layer.name().split('_')[0] == 'lotes':
            lay_lotes = QgsProject.instance().mapLayersByName(layer.name())[0]
            print(lay_lotes.name())
            
        if layer.name().split('_')[0] == 'quadras':
            lay_quadras = QgsProject.instance().mapLayersByName(layer.name())[0]
            print(lay_quadras.name())
            
        if layer.name().split('_')[0] == 'edificacoes':
            lay_edificacoes = QgsProject.instance().mapLayersByName(layer.name())[0]
            print(lay_edificacoes.name())
            
        if layer.name().split('_')[0] == 'logradouros':
            lay_logradouros = QgsProject.instance().mapLayersByName(layer.name())[0]
            print(lay_logradouros.name())
            
        if layer.name().split('_')[0] == 'confrontantes':
            lay_confrontantes = QgsProject.instance().mapLayersByName(layer.name())[0]
            print(lay_confrontantes.name())
    
    
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
            campos = lay_bairros.fields()
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
            



layers = QgsProject.instance().mapLayers().values()
path = ( r'C:\Users\Carlos André-DIGITAL\Documents\digital map - geo\PROJETOS DMG\PAU_DARCO\SHAPES\Nova pasta'.replace('\\', '/')+'/')




abrir_camadas(path,'.shp')
atualizar_bairros()









