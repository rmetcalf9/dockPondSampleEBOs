
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceEBO:SpaceEBOTypeV1':
      return flaskRestPlusAPI.model('SpaceEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceRBO:IdentificationTypeV1')),
        'Name': fields.String(default='',description='Name of the Space'),
        'Description': fields.String(default='',description='Name of the Space'),
        'EffectiveDates': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),
        'AreaInformation': fields.Nested(flaskRestPlusAPI.model('InlineAreaInformationType', {
          #Element NetArea has a type that is not catered for (xsd:decimal) 0
          #Element GrossArea has a type that is not catered for (xsd:decimal) 0
          #Element UpliftedArea has a type that is not catered for (xsd:decimal) 0
          #Element Height has a type that is not catered for (xsd:decimal) 0
        })),
        #Element Capacity has a type that is not catered for (xsd:int) 0
        'SpaceCategory': fields.String(default='',description='Space Category e.g Core This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Space\V1\XXIC_SpaceCategory.dvm'),
        'SpaceType': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceEBO:SpaceTypeV1')),
        'Building': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Building/V1/BuildingRBO:BuildingReferenceTypeV1')),
        'Floor': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Floor/V1/FloorRBO:FloorReferenceTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceEBO:SpaceTypeV1':
      return flaskRestPlusAPI.model('SpaceTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'Code': fields.String(default='',description='Code of Space Type'),
        })),
        'Name': fields.String(default='',description='Name of Space Type'),
        'Description': fields.String(default='',description='Description of Space Type'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Building/V1/BuildingRBO:BuildingReferenceTypeV1':
      return flaskRestPlusAPI.model('BuildingReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Building/V1/BuildingRBO:IdentificationTypeV1')),
        'Name': fields.String(default='',description=''),
        'Description': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Building/V1/BuildingRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'Code': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Floor/V1/FloorRBO:FloorReferenceTypeV1':
      return flaskRestPlusAPI.model('FloorReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Floor/V1/FloorRBO:IdentificationTypeV1')),
        'Name': fields.String(default='',description=''),
        'Description': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Floor/V1/FloorRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'Code': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceRBO:SpaceReferenceTypeV1':
      return flaskRestPlusAPI.model('SpaceReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceRBO:IdentificationTypeV1')),
        'Name': fields.String(default='',description=''),
        'Description': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'Code': fields.String(default='',description='Code of the Space will consist of BuildingCode-FloorCode-SpaceCode as SpaceCode itself is not unique by itself'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1':
      return flaskRestPlusAPI.model('EffectiveDateTypeV1', {
        #Element StartDateTime has a type that is not catered for (xsd:dateTime) 0
        #Element EndDateTime has a type that is not catered for (xsd:dateTime) 0

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('SpaceEBOV1', {
    'SpaceEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceEBO:SpaceEBOTypeV1')),

  })

