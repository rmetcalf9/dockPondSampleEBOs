
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:PublicationEBOTypeV1':
      return flaskRestPlusAPI.model('PublicationEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationRBO:IdentificationTypeV1')),
        'Journal': fields.Nested(flaskRestPlusAPI.model('InlineJournalType', {
          'Title': fields.String(default='',description=''),
          'ISSN': fields.String(default='',description=''),
          'eISSN': fields.String(default='',description=''),
        })),
        'Conference': fields.Nested(flaskRestPlusAPI.model('InlineConferenceType', {
          'Title': fields.String(default='',description=''),
        })),
        'Type': fields.String(default='',description=''),
        'Title': fields.String(default='',description=''),
        'PublicationLink': fields.String(default='',description=''),
        #Element DateOfAcceptance has a type that is not catered for (xsd:dateTime) 0
        'CorrespondingAuthorInstitution': fields.String(default='',description=''),
        'PageCharges': fields.String(default='',description=''),
        'Authors': fields.Nested(flaskRestPlusAPI.model('InlineAuthorsType', {
          'Author': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:AuthorTypeV1'))),
        })),
        'ClaimedAuthors': fields.Nested(flaskRestPlusAPI.model('InlineClaimedAuthorsType', {
          'ClaimedAuthor': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:ClaimedAuthorTypeV1'))),
        })),
        #Element LastModified has a type that is not catered for (xsd:dateTime) 0
        #Element Created has a type that is not catered for (xsd:dateTime) 0
        'RepositoryItems': fields.Nested(flaskRestPlusAPI.model('InlineRepositoryItemsType', {
          'RepositoryItem': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:RepositoryItemTypeV1'))),
        })),
        'RequestedEmbargoPeriod': fields.String(default='',description=''),
        'RepositoryLicenceID': fields.String(default='',description=''),
        'Grants': fields.Nested(flaskRestPlusAPI.model('InlineGrantsType', {
          'Grant': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Grant/V1/GrantRBO:GrantRBOTypeV1'))),
        })),
        #Element OpenAccessRequired has a type that is not catered for (xsd:boolean) 0
        'Language': fields.String(default='',description=''),
        'Issue': fields.String(default='',description=''),
        #Element PublicationDate has a type that is not catered for (xsd:date) 0
        #Element EverApproved has a type that is not catered for (xsd:boolean) 0
        'Currency': fields.String(default='',description=''),
        'Cost': fields.String(default='',description=''),
        'Comments': fields.String(default='',description=''),
        'VerificationStatus': fields.String(default='',description=''),
        #Element IsNotExternallyFunded has a type that is not catered for (xsd:boolean) 0
        #Element LastFlaggedAsGrantNotListed has a type that is not catered for (xsd:dateTime) 0
        'MergeHistory': fields.Nested(flaskRestPlusAPI.model('InlineMergeHistoryType', {
          'Merge': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:MergeHistoryTypeV1'))),
        })),
        'Publisher': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:MergeHistoryTypeV1':
      return flaskRestPlusAPI.model('MergeHistoryTypeV1', {
        #Element Created has a type that is not catered for (xsd:dateTime) 0
        'merged-object': fields.String(default='',description=''),
        'merged-into-object': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:AuthorTypeV1':
      return flaskRestPlusAPI.model('AuthorTypeV1', {
        'LastName': fields.String(default='',description=''),
        'Initials': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:ClaimedAuthorTypeV1':
      return flaskRestPlusAPI.model('ClaimedAuthorTypeV1', {
        #Element EntryUpdated has a type that is not catered for (xsd:dateTime) 0
        #Element LastModifiedWhen has a type that is not catered for (xsd:dateTime) 0
        'ProprietaryID': fields.String(default='',description=''),
        'AuthenticatingAuthority': fields.String(default='',description=''),
        'Username': fields.String(default='',description=''),
        #Element everApproved has a type that is not catered for (xsd:boolean) 0
        #Element isCurrentStaff has a type that is not catered for (xsd:boolean) 0
        #Element isAcademic has a type that is not catered for (xsd:boolean) 0
        'Title': fields.String(default='',description=''),
        'Initials': fields.String(default='',description=''),
        'FirstName': fields.String(default='',description=''),
        'LastName': fields.String(default='',description=''),
        'EmailAddress': fields.String(default='',description=''),
        'PrimaryGroupDescriptor': fields.String(default='',description=''),
        'CID': fields.String(default='',description=''),
        'Faculty': fields.String(default='',description=''),
        'PrimaryHRO': fields.String(default='',description=''),
        'LowLevelHRO': fields.String(default='',description=''),
        'Campus': fields.String(default='',description=''),
        'Building': fields.String(default='',description=''),
        'Room': fields.String(default='',description=''),
        'PositionName': fields.String(default='',description=''),
        'Status': fields.String(default='',description=''),
        'Grading': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:RepositoryItemTypeV1':
      return flaskRestPlusAPI.model('RepositoryItemTypeV1', {
        'RepositoryID': fields.String(default='',description=''),
        'RepositoryName': fields.String(default='',description=''),
        'Status': fields.String(default='',description=''),
        'RepositoryFiles': fields.Nested(flaskRestPlusAPI.model('InlineRepositoryFilesType', {
          'RepositoryFile': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:RepositoryFileTypeV1'))),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:RepositoryFileTypeV1':
      return flaskRestPlusAPI.model('RepositoryFileTypeV1', {
        'Type': fields.String(default='',description=''),
        #Element LastModified has a type that is not catered for (xsd:dateTime) 0
        'Name': fields.String(default='',description=''),
        'Mime-Type': fields.String(default='',description=''),
        'Version': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:FundingAcknowledgementTypeV1':
      return flaskRestPlusAPI.model('FundingAcknowledgementTypeV1', {
        'GrantID': fields.String(default='',description=''),
        'Organisation': fields.String(default='',description=''),
        'RequestedEmbargoPeriod': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'PublicationID': fields.String(default='',description=''),
        'DOI': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Grant/V1/GrantRBO:GrantRBOTypeV1':
      return flaskRestPlusAPI.model('GrantRBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Grant/V1/GrantRBO:IdentificationTypeV1')),
        'Description': fields.String(default='',description=''),
        'FunderName': fields.String(default='',description=''),
        'FunderReference': fields.String(default='',description=''),
        'FunderType': fields.String(default='',description=''),
        'InstitutionReference': fields.String(default='',description=''),
        #Element StartDate has a type that is not catered for (xsd:dateTime) 0
        #Element EndDate has a type that is not catered for (xsd:dateTime) 0
        'Title': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Grant/V1/GrantRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'GMSAwardNumber': fields.String(default='',description=''),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('PublicationEBOV1', {
    'PublicationEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Publication/V1/PublicationEBO:PublicationEBOTypeV1')),

  })

