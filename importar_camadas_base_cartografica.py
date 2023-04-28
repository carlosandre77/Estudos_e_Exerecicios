from qgis.core import QgsExpression, QgsVectorLayer

project= QgsProject.instance()

##nome do local que sera corfigurada a base
base_proj=('pau_darco')

##caminho dos arquivos
path = ( r'C:\Users\Carlos André-DIGITAL\Documents\digital map - geo\PROJETOS DMG\PAU_DARCO\SHAPES\Nova pasta'.replace('\\', '/'+'/'))

for root, directory, files in os.walk(path):
    for file in files:
        if file.endswith('.shp'):
           path_vector = os.path.join(path,file)
           layer = QgsVectorLayer(path_vector,file[0:-4],"ogr")
           QgsProject.instance().addMapLayer(layer)
           ##identificação das principais feições
           if layer.name() == 'bairro_'+ base_proj:
               lay_bairros = QgsProject.instance().mapLayersByName(layer.name())[0]
               print(lay_bairros.name())
               lay_bairros.setName("bairros")
           if layer.name() == 'lotes_'+ base_proj:
               lay_lotes = QgsProject.instance().mapLayersByName(layer.name())[0]
               print(lay_lotes.name())
               lay_lotes.setName("lotes")
           if layer.name() == 'quadras_'+ base_proj:
               lay_quadras = QgsProject.instance().mapLayersByName(layer.name())[0]
               print(lay_quadras.name())
               lay_quadras.setName("quadras")
           if layer.name() == 'edificacoes_'+ base_proj:
               lay_edificacoes = QgsProject.instance().mapLayersByName(layer.name())[0]
               print(lay_edificacoes.name())
               lay_edificacoes.setName("edificacoes")
           if layer.name() == 'logradouros_'+ base_proj:
               lay_logradouros = QgsProject.instance().mapLayersByName(layer.name())[0]
               print(lay_logradouros.name())
               lay_logradouros.setName("logradouros")
           if layer.name() == 'confrontantes_'+ base_proj:
               lay_confrontantes = QgsProject.instance().mapLayersByName(layer.name())[0]
               print(lay_confrontantes.name())
               lay_confrontantes.setName("confrontantes")