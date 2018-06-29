
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeEBO:ProgrammeTypeV1':
      return flaskRestPlusAPI.model('ProgrammeTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeEBO:IdentificationTypeV1')),
        'Awards': fields.Nested(flaskRestPlusAPI.model('InlineAwardsType', {
          'Award': fields.List(fields.String(default='',description='')),
        })),
        'ProgrammeVersions': fields.Nested(flaskRestPlusAPI.model('InlineProgrammeVersionsType', {
          'ProgrammeVersion': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeEBO:ProgrammeVersionTypeV1'))),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeEBO:ProgrammeVersionTypeV1':
      return flaskRestPlusAPI.model('ProgrammeVersionTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeEBO:VersionIdentificationTypeV1')),
        'Description': fields.String(default='',description='This is Programme/Course description or Title e.g Bachelor of Nursing'),
        'ShortDescription': fields.String(default='',description='This is Programme/Course Short name e.g Nursing'),
        'Abbreviation': fields.String(default='',description='This is Programme/Course abbreviated name e.g NUR BSC'),
        'FacultyCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Faculty:FacultyCodeTypeV1')),
        'Department': fields.String(default='',description='Programme department e.g Department of Mental Health'),
        'PrimaryDisciplineCode': fields.String(default='',description='This is the code that identify the programme Programme Field Of Study e.g NUR'),
        'ProgrammeType': fields.String(default='',description='Programme Type can be UG, PG'),
        'Status': fields.String(default='',description='The Status of the Programme, this either be Active or Inactive'),
        #Element GenericProgramme has a type that is not catered for (xsd:boolean) 0
        #Element GraduateStudents has a type that is not catered for (xsd:boolean) 0
        #Element SupplementalExamsPermitted has a type that is not catered for (xsd:boolean) 0
        #Element AllowIntermission has a type that is not catered for (xsd:boolean) 0
        #Element CountInProgression has a type that is not catered for (xsd:boolean) 0
        #Element StartDate has a type that is not catered for (xsd:dateTime) 0
        #Element EndDate has a type that is not catered for (xsd:dateTime) 0
        #Element PlacementFlag has a type that is not catered for (xsd:boolean) 0

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeEBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'ProgrammeCode': fields.String(default='',description='This is Programme/Course unique identifier e.g MED101'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeEBO:VersionIdentificationTypeV1':
      return flaskRestPlusAPI.model('VersionIdentificationTypeV1', {
        #Element Version has a type that is not catered for (xsd:integer) 0

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Faculty:FacultyCodeTypeV1':
      return flaskRestPlusAPI.model('FacultyCodeTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'FacultyCode': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_FacultyCode.dvm'),
        })),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('ProgrammeEBOV1', {
    'ProgrammeEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeEBO:ProgrammeTypeV1')),

  })

