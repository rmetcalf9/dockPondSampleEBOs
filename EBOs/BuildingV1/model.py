
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Building/V1/BuildingEBO:BuildingEBOTypeV1':
      return flaskRestPlusAPI.model('BuildingEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Building/V1/BuildingRBO:IdentificationTypeV1')),
        'Name': fields.String(default='',description='Name of the Building'),
        'Origin': fields.String(default='',description='Origin of Building within Pythagoras'),
        'Address': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:PhysicalAddressTypeV1')),
        'AreaInformation': fields.Nested(flaskRestPlusAPI.model('InlineAreaInformationType', {
          'GeoLocation': fields.Nested(flaskRestPlusAPI.model('InlineGeoLocationType', {
            'geoX': fields.String(default='',description='Longitude of the Building'),
            'geoY': fields.String(default='',description='Latitude of the Building'),
            'geoRotation': fields.String(default='',description='geoRotation of the Building'),
          })),
          'NetArea': fields.String(default='',description='NetArea of the Building'),
          'GrossArea': fields.String(default='',description='GrossArea of the Building'),
        })),
        'Campus': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Campus/V1/CampusRBO:CampusReferenceTypeV1')),
        'Floors': fields.Nested(flaskRestPlusAPI.model('InlineFloorsType', {
          'Floor': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Floor/V1/FloorRBO:FloorReferenceTypeV1'))),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Campus/V1/CampusRBO:CampusReferenceTypeV1':
      return flaskRestPlusAPI.model('CampusReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Campus/V1/CampusRBO:IdentificationTypeV1')),
        'Name': fields.String(default='',description=''),
        'Description': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Campus/V1/CampusRBO:IdentificationTypeV1':
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
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'AddressNumber': fields.String(default='',description='Address Unique Identifier'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:PhysicalAddressTypeV1':
      return flaskRestPlusAPI.model('PhysicalAddressTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:IdentificationTypeV1')),
        'AddressUsages': fields.Nested(flaskRestPlusAPI.model('InlineAddressUsagesType', {
          'AddressUsage': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/UsageType:UsageTypeV1'))),
        })),
        'Address1': fields.String(default='',description='The first Line of address'),
        'Address2': fields.String(default='',description='Second line of address'),
        'Address3': fields.String(default='',description='Third line of Address'),
        'Address4': fields.String(default='',description='Fourth Line of Address'),
        'Region': fields.String(default='',description='County/Region/District/Province/State'),
        'City': fields.String(default='',description='City or Town'),
        'PostalCode': fields.String(default='',description='Post Code of an address'),
        'Country': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_Country.dvm'),
        'EffectiveDates': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1':
      return flaskRestPlusAPI.model('EffectiveDateTypeV1', {
        #Element StartDateTime has a type that is not catered for (xsd:dateTime) 0
        #Element EndDateTime has a type that is not catered for (xsd:dateTime) 0

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/UsageType:UsageTypeV1':
      return flaskRestPlusAPI.model('UsageTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'UsageID': fields.String(default='',description='The usage identifier'),
        })),
        'UsageCode': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_UsageCode.dvm'),
        'PreferredIndicator': fields.String(default='',description='Indicates if this is the preferred usage'),
        'EffectiveDates': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('BuildingEBOV1', {
    'BuildingEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Building/V1/BuildingEBO:BuildingEBOTypeV1')),

  })

