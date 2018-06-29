
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1:HROrganizationUnitEBOTypeV1':
      return flaskRestPlusAPI.model('HROrganizationUnitEBOTypeV1', {
        #Element  has a type that is not catered for () 0
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1:IdentificationTypeV1')),
        'Name': fields.String(default='',description=''),
        'OrgCode': fields.String(default='',description='Depreciated - Element now used as Identification so it is in Identification structure'),
        'Description': fields.String(default='',description=''),
        'InternalExternalFlag': fields.String(default='',description=''),
        'Type': fields.String(default='',description=''),
        'DeptCode': fields.String(default='',description='Depreciated - Department now used'),
        'Department': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1/HROrganizatinUnitRBO:HROrganizationUnitReferenceTypeV1')),
        'DefaultUofA1996': fields.String(default='',description=''),
        'DefaultUofA2001': fields.String(default='',description=''),
        'DefaultUofA2008': fields.String(default='',description=''),
        'DefaultUofA2014': fields.String(default='',description=''),
        'HESACostCentre': fields.String(default='',description=''),
        'GLCostCentre': fields.String(default='',description=''),
        #Element  has a type that is not catered for () 0
        'BusinessGroupID': fields.String(default='',description=''),
        'Faculty': fields.String(default='',description='Depreciated - OrgFaculty now used'),
        'FacultyDescription': fields.String(default='',description='Depreciated - OrgFaculty now used'),
        'OrgFaculty': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1/HROrganizatinUnitRBO:HROrganizationUnitReferenceTypeV1')),
        #Element Level has a type that is not catered for (xsd:int) 0
        'ParentHROrganizationUnit': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1:HROrganizationUnitEBOTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'OrgCode': fields.String(default='',description=''),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerPartyContactAddressCommunicationIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomerPartyContactAddressCommunicationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SeasonalEffectivePeriodTypeV1':
      return flaskRestPlusAPI.model('SeasonalEffectivePeriodTypeV1', {
        #Element StartMonthDay has a type that is not catered for (MonthDayType) 0
        #Element EndMonthDay has a type that is not catered for (MonthDayType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSeasonalEffectivePeriodTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentReceiptReferenceTypeV1':
      return flaskRestPlusAPI.model('ShipmentReceiptReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentReceiptTransactionLotIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentReceiptTransactionLotIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentReceiptItemInstanceRangeIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentReceiptItemInstanceRangeIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentReceiptItemInstanceIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentReceiptItemInstanceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DocumentScheduleIdentificationTypeV1':
      return flaskRestPlusAPI.model('DocumentScheduleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DocumentScheduleReferenceTypeV1':
      return flaskRestPlusAPI.model('DocumentScheduleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element CreationDateTime has a type that is not catered for (DateTimeType) 0
        #Element LastUpdateDateTime has a type that is not catered for (DateTimeType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDocumentScheduleReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RMAFulfillmentOrderScheduleReferenceTypeV1':
      return flaskRestPlusAPI.model('RMAFulfillmentOrderScheduleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ReceiptAdviceIdentificationTypeV1':
      return flaskRestPlusAPI.model('ReceiptAdviceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RMASalesOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('RMASalesOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RMASalesOrderScheduleReferenceTypeV1':
      return flaskRestPlusAPI.model('RMASalesOrderScheduleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyLocationTypeV1':
      return flaskRestPlusAPI.model('PartyLocationTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element SeasonalIndicator has a type that is not catered for (IndicatorType) 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyLocationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactAddressCommunicationTypeV1':
      return flaskRestPlusAPI.model('ContactAddressCommunicationTypeV1', {
        #Element  has a type that is not catered for () 0
        'PreferredMediaTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'PreferredMediaFormatCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element SeasonalIndicator has a type that is not catered for (IndicatorType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactAddressCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ComponentIdentificationTypeV1':
      return flaskRestPlusAPI.model('ComponentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ObjectIdentificationTypeV1':
      return flaskRestPlusAPI.model('ObjectIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DocumentReferenceTypeV1':
      return flaskRestPlusAPI.model('DocumentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element CreationDateTime has a type that is not catered for (DateTimeType) 0
        #Element LastUpdateDateTime has a type that is not catered for (DateTimeType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDocumentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DocumentLineReferenceTypeV1':
      return flaskRestPlusAPI.model('DocumentLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element CreationDateTime has a type that is not catered for (DateTimeType) 0
        #Element LastUpdateDateTime has a type that is not catered for (DateTimeType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDocumentLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FundCaptureTransactionExtensionIdentificationTypeV1':
      return flaskRestPlusAPI.model('FundCaptureTransactionExtensionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FundCaptureTransactionExtensionReferenceTypeV1':
      return flaskRestPlusAPI.model('FundCaptureTransactionExtensionReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ReceiptMethodIdentificationTypeV1':
      return flaskRestPlusAPI.model('ReceiptMethodIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ReceiptMethodReferenceTypeV1':
      return flaskRestPlusAPI.model('ReceiptMethodReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentAttachmentTypeV1':
      return flaskRestPlusAPI.model('ShipmentAttachmentTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentAttachmentTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentItemAttachmentTypeV1':
      return flaskRestPlusAPI.model('ShipmentItemAttachmentTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemAttachmentTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentInstrumentTypeV1':
      return flaskRestPlusAPI.model('PaymentInstrumentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentTypeV1':
      return flaskRestPlusAPI.model('ShipmentTypeV1', {
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ServiceLevelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ModeOfTransportationCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'DestinationCountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'OriginCountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element InitialPickupDate has a type that is not catered for (DateType) 0
        #Element UltimateDropOffDate has a type that is not catered for (DateType) 0
        #Element EarliestPickUpDate has a type that is not catered for (DateType) 0
        #Element LatestPickUpDate has a type that is not catered for (DateType) 0
        #Element EarliestDropOffDate has a type that is not catered for (DateType) 0
        #Element LatestDropOffDate has a type that is not catered for (DateType) 0
        'PointofStagingCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'FOBPointCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'PointOfLoadingCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'DockCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'RoutingInstruction': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ShipmentInstruction': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'FreightTermCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TotalFreightAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'VehicleNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'PackingSlipNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'WaybillNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'GrossWeight': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),
        'NetWeight': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),
        'TareWeight': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),
        'ShipmentVolume': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),
        'ShipUnitQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        #Element HazardousMaterialIndicator has a type that is not catered for (IndicatorType) 0
        #Element OwnershipChangeIndicator has a type that is not catered for (xsd:anyType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AppointmentIdentificationTypeV1':
      return flaskRestPlusAPI.model('AppointmentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AppointmentReferenceTypeV1':
      return flaskRestPlusAPI.model('AppointmentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerPartyAccountSiteUsageIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomerPartyAccountSiteUsageIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RecoveryTimePeriodTypeV1':
      return flaskRestPlusAPI.model('RecoveryTimePeriodTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemReturnReasonTypeV1':
      return flaskRestPlusAPI.model('ItemReturnReasonTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemSubstitutionReasonTypeV1':
      return flaskRestPlusAPI.model('ItemSubstitutionReasonTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FulfillmentOrderScheduleIdentificationTypeV1':
      return flaskRestPlusAPI.model('FulfillmentOrderScheduleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FulfillmentOrderHoldIdentificationTypeV1':
      return flaskRestPlusAPI.model('FulfillmentOrderHoldIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerPartyAccountSiteIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomerPartyAccountSiteIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InventoryReservationIdentificationTypeV1':
      return flaskRestPlusAPI.model('InventoryReservationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InventoryReservationReferenceTypeV1':
      return flaskRestPlusAPI.model('InventoryReservationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OperationTypeV1':
      return flaskRestPlusAPI.model('OperationTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FulfillmentOrderScheduleReferenceTypeV1':
      return flaskRestPlusAPI.model('FulfillmentOrderScheduleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OverdueCollectionRuleIdentificationTypeV1':
      return flaskRestPlusAPI.model('OverdueCollectionRuleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OverdueCollectionRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('OverdueCollectionRuleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyRelatedOrganizationPartyIdentificationTypeV1':
      return flaskRestPlusAPI.model('PartyRelatedOrganizationPartyIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesObjectiveIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalesObjectiveIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesObjectiveReferenceTypeV1':
      return flaskRestPlusAPI.model('SalesObjectiveReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesPlanIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalesPlanIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesPlanReferenceTypeV1':
      return flaskRestPlusAPI.model('SalesPlanReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesPlanPeriodIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalesPlanPeriodIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesPlanPeriodReferenceTypeV1':
      return flaskRestPlusAPI.model('SalesPlanPeriodReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentAdviceIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentAdviceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentAdviceReferenceTypeV1':
      return flaskRestPlusAPI.model('ShipmentAdviceReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SWOTAnalysisTypeV1':
      return flaskRestPlusAPI.model('SWOTAnalysisTypeV1', {
        'StrengthsDescription': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'WeaknessesDescription': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'OpportunitiesDescription': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ThreatsDescription': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSWOTAnalysisTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TaskIdentificationTypeV1':
      return flaskRestPlusAPI.model('TaskIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TaskReferenceTypeV1':
      return flaskRestPlusAPI.model('TaskReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InventoryOrganizationIdentificationTypeV1':
      return flaskRestPlusAPI.model('InventoryOrganizationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InventoryOrganizationReferenceTypeV1':
      return flaskRestPlusAPI.model('InventoryOrganizationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentReceiptIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentReceiptIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentReceiptLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentReceiptLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentReceiptTransactionIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentReceiptTransactionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentReceiptTransactionReferenceTypeV1':
      return flaskRestPlusAPI.model('ShipmentReceiptTransactionReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesOrderHoldIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalesOrderHoldIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InstructionListTypeV1':
      return flaskRestPlusAPI.model('InstructionListTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InstructionListLineTypeV1':
      return flaskRestPlusAPI.model('InstructionListLineTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element SequenceNumber has a type that is not catered for (NumericType) 0
        'Instruction': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EFTTypeV1':
      return flaskRestPlusAPI.model('EFTTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'AccountHolder': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'RoutingNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'BankName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Number': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Memo': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element IssuedDate has a type that is not catered for (DateType) 0
        #Element ReceivingDepositoryFinancialInsitution has a type that is not catered for (StringType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TaxExemptionTypeV1':
      return flaskRestPlusAPI.model('TaxExemptionTypeV1', {
        'ReasonCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'CertificateNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element LicenseIndicator has a type that is not catered for (IndicatorType) 0
        #Element IssueDateTime has a type that is not catered for (DateTimeType) 0
        #Element ExpirationDateTime has a type that is not catered for (DateTimeType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element Percentage has a type that is not catered for (PercentType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DepartmentReferenceTypeV1':
      return flaskRestPlusAPI.model('DepartmentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDepartmentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BusinessUnitReferenceTypeV1':
      return flaskRestPlusAPI.model('BusinessUnitReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBusinessUnitReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemReferenceTypeV1':
      return flaskRestPlusAPI.model('ItemReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'ClassificationCode': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1'))),
        #Element ServiceIndicator has a type that is not catered for (IndicatorType) 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element ItemLotControlIndicator has a type that is not catered for (IndicatorType) 0
        #Element ItemSerialControlIndicator has a type that is not catered for (IndicatorType) 0
        'SerialControlAgencyID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element ComposedItemIndicator has a type that is not catered for (IndicatorType) 0
        #Element ServiceInstanceIndicator has a type that is not catered for (IndicatorType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AcademicRankIdentificationTypeV1':
      return flaskRestPlusAPI.model('AcademicRankIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AccountBalanceAdjustmentIdentificationTypeV1':
      return flaskRestPlusAPI.model('AccountBalanceAdjustmentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AccountingPeriodIdentificationTypeV1':
      return flaskRestPlusAPI.model('AccountingPeriodIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AccountingRuleIdentificationTypeV1':
      return flaskRestPlusAPI.model('AccountingRuleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ActivityIdentificationTypeV1':
      return flaskRestPlusAPI.model('ActivityIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AssignmentGradeIdentificationTypeV1':
      return flaskRestPlusAPI.model('AssignmentGradeIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AssignmentGradeStepIdentificationTypeV1':
      return flaskRestPlusAPI.model('AssignmentGradeStepIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AttributeBasedPricingMatrixIdentificationTypeV1':
      return flaskRestPlusAPI.model('AttributeBasedPricingMatrixIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AdvanceShipmentNoticeIdentificationTypeV1':
      return flaskRestPlusAPI.model('AdvanceShipmentNoticeIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BankAccountIdentificationTypeV1':
      return flaskRestPlusAPI.model('BankAccountIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BankBranchIdentificationTypeV1':
      return flaskRestPlusAPI.model('BankBranchIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BargainingUnitIdentificationTypeV1':
      return flaskRestPlusAPI.model('BargainingUnitIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BatchProductionOrderIdentificationTypeV1':
      return flaskRestPlusAPI.model('BatchProductionOrderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillingProfileIdentificationTypeV1':
      return flaskRestPlusAPI.model('BillingProfileIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillOfLadingIdentificationTypeV1':
      return flaskRestPlusAPI.model('BillOfLadingIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BusinessUnitIdentificationTypeV1':
      return flaskRestPlusAPI.model('BusinessUnitIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BusinessUnitFunctionIdentificationTypeV1':
      return flaskRestPlusAPI.model('BusinessUnitFunctionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillOfMaterialsIdentificationTypeV1':
      return flaskRestPlusAPI.model('BillOfMaterialsIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillOfMaterialsComponentItemIdentificationTypeV1':
      return flaskRestPlusAPI.model('BillOfMaterialsComponentItemIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillOfMaterialsConfigurationStructureIdentificationTypeV1':
      return flaskRestPlusAPI.model('BillOfMaterialsConfigurationStructureIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BudgetIdentificationTypeV1':
      return flaskRestPlusAPI.model('BudgetIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CalendarIdentificationTypeV1':
      return flaskRestPlusAPI.model('CalendarIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CarrierRouteStopIdentificationTypeV1':
      return flaskRestPlusAPI.model('CarrierRouteStopIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ClassificationCodeIdentificationTypeV1':
      return flaskRestPlusAPI.model('ClassificationCodeIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ClassificationSpecificationIdentificationTypeV1':
      return flaskRestPlusAPI.model('ClassificationSpecificationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IncentiveCompensationPlanIdentificationTypeV1':
      return flaskRestPlusAPI.model('IncentiveCompensationPlanIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IncentiveCompensationPlanComponentIdentificationTypeV1':
      return flaskRestPlusAPI.model('IncentiveCompensationPlanComponentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CompensationPackageRuleIdentificationTypeV1':
      return flaskRestPlusAPI.model('CompensationPackageRuleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CompensationPackageTemplateIdentificationTypeV1':
      return flaskRestPlusAPI.model('CompensationPackageTemplateIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ConfigurationIdentificationTypeV1':
      return flaskRestPlusAPI.model('ConfigurationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactIdentificationTypeV1':
      return flaskRestPlusAPI.model('ContactIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContainerIdentificationTypeV1':
      return flaskRestPlusAPI.model('ContainerIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContractIdentificationTypeV1':
      return flaskRestPlusAPI.model('ContractIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContractLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('ContractLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreditProfileIdentificationTypeV1':
      return flaskRestPlusAPI.model('CreditProfileIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerPartyAccountIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomerPartyAccountIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerPartyAccountContactIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomerPartyAccountContactIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerPartyIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomerPartyIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreditMemoIdentificationTypeV1':
      return flaskRestPlusAPI.model('CreditMemoIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DepartmentIdentificationTypeV1':
      return flaskRestPlusAPI.model('DepartmentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DirectDebitMandateIdentificationTypeV1':
      return flaskRestPlusAPI.model('DirectDebitMandateIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DocumentIdentificationTypeV1':
      return flaskRestPlusAPI.model('DocumentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DocumentLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('DocumentLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EngineeringChangeOrderIdentificationTypeV1':
      return flaskRestPlusAPI.model('EngineeringChangeOrderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EngineeringChangeOrderLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('EngineeringChangeOrderLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EstablishmentIdentificationTypeV1':
      return flaskRestPlusAPI.model('EstablishmentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FestivalAdvancePayProgramIdentificationTypeV1':
      return flaskRestPlusAPI.model('FestivalAdvancePayProgramIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FinancialAccountIdentificationTypeV1':
      return flaskRestPlusAPI.model('FinancialAccountIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FundIdentificationTypeV1':
      return flaskRestPlusAPI.model('FundIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:GovernmentAgencyIdentificationTypeV1':
      return flaskRestPlusAPI.model('GovernmentAgencyIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:INAILRiskProfileIdentificationTypeV1':
      return flaskRestPlusAPI.model('INAILRiskProfileIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItineraryIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItineraryIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InstalledProductIdentificationTypeV1':
      return flaskRestPlusAPI.model('InstalledProductIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InvoiceIdentificationTypeV1':
      return flaskRestPlusAPI.model('InvoiceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InvoiceLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('InvoiceLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InvoicingRuleIdentificationTypeV1':
      return flaskRestPlusAPI.model('InvoicingRuleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayableInvoiceIdentificationTypeV1':
      return flaskRestPlusAPI.model('PayableInvoiceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayableInvoiceLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('PayableInvoiceLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PositionStandardClassificationIdentificationTypeV1':
      return flaskRestPlusAPI.model('PositionStandardClassificationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FreightInvoiceIdentificationTypeV1':
      return flaskRestPlusAPI.model('FreightInvoiceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ExternalInvoiceIdentificationTypeV1':
      return flaskRestPlusAPI.model('ExternalInvoiceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ExternalInvoiceLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('ExternalInvoiceLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EmploymentGradeIdentificationTypeV1':
      return flaskRestPlusAPI.model('EmploymentGradeIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EmploymentAssignmentIdentificationTypeV1':
      return flaskRestPlusAPI.model('EmploymentAssignmentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItemIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemATPRuleIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItemATPRuleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemPickingRuleIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItemPickingRuleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemFormulaIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItemFormulaIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemFormulaMaterialIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItemFormulaMaterialIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemCatalogIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItemCatalogIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemInstanceGenealogyCompositionIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItemInstanceGenealogyCompositionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemLotIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItemLotIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemStructureIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItemStructureIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemStructureComponentItemIdentificationTypeV1':
      return flaskRestPlusAPI.model('ItemStructureComponentItemIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InventoryTransactionIdentificationTypeV1':
      return flaskRestPlusAPI.model('InventoryTransactionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:JobIdentificationTypeV1':
      return flaskRestPlusAPI.model('JobIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:JobFamilyIdentificationTypeV1':
      return flaskRestPlusAPI.model('JobFamilyIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LaborAgreementIdentificationTypeV1':
      return flaskRestPlusAPI.model('LaborAgreementIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LaborAgreementFirstLevelEmployeeClassificationIdentificationTypeV1':
      return flaskRestPlusAPI.model('LaborAgreementFirstLevelEmployeeClassificationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LaborAgreementSecondLevelEmployeeClassificationIdentificationTypeV1':
      return flaskRestPlusAPI.model('LaborAgreementSecondLevelEmployeeClassificationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LaborAgreementThirdLevelEmployeeClassificationIdentificationTypeV1':
      return flaskRestPlusAPI.model('LaborAgreementThirdLevelEmployeeClassificationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LedgerIdentificationTypeV1':
      return flaskRestPlusAPI.model('LedgerIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LegalEntityIdentificationTypeV1':
      return flaskRestPlusAPI.model('LegalEntityIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LegislativeDataGroupIdentificationTypeV1':
      return flaskRestPlusAPI.model('LegislativeDataGroupIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LocationIdentificationTypeV1':
      return flaskRestPlusAPI.model('LocationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ManufacturingRoutingIdentificationTypeV1':
      return flaskRestPlusAPI.model('ManufacturingRoutingIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ManufacturingRoutingActivityIdentificationTypeV1':
      return flaskRestPlusAPI.model('ManufacturingRoutingActivityIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ManufacturingRoutingOperationIdentificationTypeV1':
      return flaskRestPlusAPI.model('ManufacturingRoutingOperationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MarketingEventIdentificationTypeV1':
      return flaskRestPlusAPI.model('MarketingEventIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MarketingOfferIdentificationTypeV1':
      return flaskRestPlusAPI.model('MarketingOfferIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MarketingOfferTreatmentIdentificationTypeV1':
      return flaskRestPlusAPI.model('MarketingOfferTreatmentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MarketingTreatmentIdentificationTypeV1':
      return flaskRestPlusAPI.model('MarketingTreatmentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OperationIdentificationTypeV1':
      return flaskRestPlusAPI.model('OperationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationIdentificationTypeV1':
      return flaskRestPlusAPI.model('OrganizationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationUnitIdentificationTypeV1':
      return flaskRestPlusAPI.model('OrganizationUnitIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyIdentificationTypeV1':
      return flaskRestPlusAPI.model('PartyIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyAccountIdentificationTypeV1':
      return flaskRestPlusAPI.model('PartyAccountIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyContactIdentificationTypeV1':
      return flaskRestPlusAPI.model('PartyContactIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentIdentificationTypeV1':
      return flaskRestPlusAPI.model('PaymentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('PaymentLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DisbursedPaymentIdentificationTypeV1':
      return flaskRestPlusAPI.model('DisbursedPaymentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayEquityJobClassIdentificationTypeV1':
      return flaskRestPlusAPI.model('PayEquityJobClassIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentProfileIdentificationTypeV1':
      return flaskRestPlusAPI.model('PaymentProfileIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentTermIdentificationTypeV1':
      return flaskRestPlusAPI.model('PaymentTermIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PerformanceReviewRatingIdentificationTypeV1':
      return flaskRestPlusAPI.model('PerformanceReviewRatingIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PerformanceReviewRatingModelIdentificationTypeV1':
      return flaskRestPlusAPI.model('PerformanceReviewRatingModelIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonIdentificationTypeV1':
      return flaskRestPlusAPI.model('PersonIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonNameIdentificationTypeV1':
      return flaskRestPlusAPI.model('PersonNameIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PlanImpactIdentificationTypeV1':
      return flaskRestPlusAPI.model('PlanImpactIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PositionPoolIdentificationTypeV1':
      return flaskRestPlusAPI.model('PositionPoolIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PricingAgreementIdentificationTypeV1':
      return flaskRestPlusAPI.model('PricingAgreementIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProductionOrderActivityIdentificationTypeV1':
      return flaskRestPlusAPI.model('ProductionOrderActivityIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProductionOrderIdentificationTypeV1':
      return flaskRestPlusAPI.model('ProductionOrderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProductionOrderMaterialIdentificationTypeV1':
      return flaskRestPlusAPI.model('ProductionOrderMaterialIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProductionOrderOperationIdentificationTypeV1':
      return flaskRestPlusAPI.model('ProductionOrderOperationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProductionOrderResourceIdentificationTypeV1':
      return flaskRestPlusAPI.model('ProductionOrderResourceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProjectResourceSetIdentificationTypeV1':
      return flaskRestPlusAPI.model('ProjectResourceSetIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProjectNonSchedulableResourceIdentificationTypeV1':
      return flaskRestPlusAPI.model('ProjectNonSchedulableResourceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProjectSchedulableResourceIdentificationTypeV1':
      return flaskRestPlusAPI.model('ProjectSchedulableResourceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseAgreementIdentificationTypeV1':
      return flaskRestPlusAPI.model('PurchaseAgreementIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseAgreementLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('PurchaseAgreementLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseAgreementPriceBreakIdentificationTypeV1':
      return flaskRestPlusAPI.model('PurchaseAgreementPriceBreakIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PriceListIdentificationTypeV1':
      return flaskRestPlusAPI.model('PriceListIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PriceListLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('PriceListLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PriceBreakIdentificationTypeV1':
      return flaskRestPlusAPI.model('PriceBreakIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PriceFormulaIdentificationTypeV1':
      return flaskRestPlusAPI.model('PriceFormulaIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PositionIdentificationTypeV1':
      return flaskRestPlusAPI.model('PositionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProjectIdentficationTypeV1':
      return flaskRestPlusAPI.model('ProjectIdentficationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PromotionIdentificationTypeV1':
      return flaskRestPlusAPI.model('PromotionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseOrderIdentificationTypeV1':
      return flaskRestPlusAPI.model('PurchaseOrderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseOrderLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('PurchaseOrderLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseOrderShipmentIdentificationTypeV1':
      return flaskRestPlusAPI.model('PurchaseOrderShipmentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuoteIdentificationTypeV1':
      return flaskRestPlusAPI.model('QuoteIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuoteLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('QuoteLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuotePriceQualificationIdentificationTypeV1':
      return flaskRestPlusAPI.model('QuotePriceQualificationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RateOfferIdentificationTypeV1':
      return flaskRestPlusAPI.model('RateOfferIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RecipeIdentificationTypeV1':
      return flaskRestPlusAPI.model('RecipeIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RecipeValidityRuleIdentificationTypeV1':
      return flaskRestPlusAPI.model('RecipeValidityRuleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RegionIdentificationTypeV1':
      return flaskRestPlusAPI.model('RegionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ReportingPeriodIdentificationTypeV1':
      return flaskRestPlusAPI.model('ReportingPeriodIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequestForQuoteIdentificationTypeV1':
      return flaskRestPlusAPI.model('RequestForQuoteIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequestForQuoteLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('RequestForQuoteLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequestForQuoteBidderIdentificationTypeV1':
      return flaskRestPlusAPI.model('RequestForQuoteBidderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequestForQuoteChargeCategoryIdentificationTypeV1':
      return flaskRestPlusAPI.model('RequestForQuoteChargeCategoryIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequestForQuoteEvaluatorIdentificationTypeV1':
      return flaskRestPlusAPI.model('RequestForQuoteEvaluatorIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequestForQuoteEvaluationCategoryIdentificationTypeV1':
      return flaskRestPlusAPI.model('RequestForQuoteEvaluationCategoryIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequestForQuotePriceQualificationIdentificationTypeV1':
      return flaskRestPlusAPI.model('RequestForQuotePriceQualificationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequisitionIdentificationTypeV1':
      return flaskRestPlusAPI.model('RequisitionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequisitionLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('RequisitionLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequisitionDistributionIdentificationTypeV1':
      return flaskRestPlusAPI.model('RequisitionDistributionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ResourceIdentificationTypeV1':
      return flaskRestPlusAPI.model('ResourceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RMAIdentificationTypeV1':
      return flaskRestPlusAPI.model('RMAIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceProviderIdentificationTypeV1':
      return flaskRestPlusAPI.model('ServiceProviderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShippingProfileIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShippingProfileIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SellingProfileIdentificationTypeV1':
      return flaskRestPlusAPI.model('SellingProfileIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SettlementIdentificationTypeV1':
      return flaskRestPlusAPI.model('SettlementIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SignatoryGroupIdentificationTypeV1':
      return flaskRestPlusAPI.model('SignatoryGroupIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalaryIncreaseMatrixIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalaryIncreaseMatrixIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalaryPlanIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalaryPlanIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesOrderIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalesOrderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesOrderLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalesOrderLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesOrderScheduleIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalesOrderScheduleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ResourceAvailabilityCalendarIdentificationTypeV1':
      return flaskRestPlusAPI.model('ResourceAvailabilityCalendarIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceCreditCalculationGroupIdentificationTypeV1':
      return flaskRestPlusAPI.model('ServiceCreditCalculationGroupIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentRequestIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentRequestIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentRequestOrderIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentRequestOrderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentRequestOrderLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentRequestOrderLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SupplierPartyTradingLocationProfileIdentificationTypeV1':
      return flaskRestPlusAPI.model('SupplierPartyTradingLocationProfileIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileIdentificationTypeV1':
      return flaskRestPlusAPI.model('TalentProfileIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileInstanceQualifierIdentificationTypeV1':
      return flaskRestPlusAPI.model('TalentProfileInstanceQualifierIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileInstanceQualifierSetIdentificationTypeV1':
      return flaskRestPlusAPI.model('TalentProfileInstanceQualifierSetIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileTypeIdentificationTypeV1':
      return flaskRestPlusAPI.model('TalentProfileTypeIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileTypeSectionIdentificationTypeV1':
      return flaskRestPlusAPI.model('TalentProfileTypeSectionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileContentItemCatalogIdentificationTypeV1':
      return flaskRestPlusAPI.model('TalentProfileContentItemCatalogIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileContentItemIdentificationTypeV1':
      return flaskRestPlusAPI.model('TalentProfileContentItemIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileContentTypeIdentificationTypeV1':
      return flaskRestPlusAPI.model('TalentProfileContentTypeIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileContentTypePropertyIdentificationTypeV1':
      return flaskRestPlusAPI.model('TalentProfileContentTypePropertyIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileItemIdentificationTypeV1':
      return flaskRestPlusAPI.model('TalentProfileItemIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TeamIdentificationTypeV1':
      return flaskRestPlusAPI.model('TeamIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TrainingProgramIdentificationTypeV1':
      return flaskRestPlusAPI.model('TrainingProgramIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProvisioningOrderIdentificationTypeV1':
      return flaskRestPlusAPI.model('ProvisioningOrderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProvisioningOrderLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('ProvisioningOrderLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FulfillmentOrderIdentificationTypeV1':
      return flaskRestPlusAPI.model('FulfillmentOrderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FulfillmentOrderLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('FulfillmentOrderLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TransportationSalesOrderIdentificationTypeV1':
      return flaskRestPlusAPI.model('TransportationSalesOrderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TransportationSalesOrderLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('TransportationSalesOrderLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesOpportunityIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalesOpportunityIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceContractCoverageTemplateIdentificationTypeV1':
      return flaskRestPlusAPI.model('ServiceContractCoverageTemplateIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceContractSubscriptionTemplateIdentificationTypeV1':
      return flaskRestPlusAPI.model('ServiceContractSubscriptionTemplateIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceRequestIdentificationTypeV1':
      return flaskRestPlusAPI.model('ServiceRequestIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesTerritoryIdentificationTypeV1':
      return flaskRestPlusAPI.model('SalesTerritoryIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentItemIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentItemIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentUnitIdentificationTypeV1':
      return flaskRestPlusAPI.model('ShipmentUnitIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SpecificationIdentificationTypeV1':
      return flaskRestPlusAPI.model('SpecificationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SpecificationGroupIdentificationTypeV1':
      return flaskRestPlusAPI.model('SpecificationGroupIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SpecificationValueSetIdentificationTypeV1':
      return flaskRestPlusAPI.model('SpecificationValueSetIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SpecificationValueSetLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('SpecificationValueSetLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SupportTeamIdentificationTypeV1':
      return flaskRestPlusAPI.model('SupportTeamIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BusinessCalendarIdentificationTypeV1':
      return flaskRestPlusAPI.model('BusinessCalendarIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:GLAccountIdentificationTypeV1':
      return flaskRestPlusAPI.model('GLAccountIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CareerPathIdentificationTypeV1':
      return flaskRestPlusAPI.model('CareerPathIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ChartOfAccountsIdentificationTypeV1':
      return flaskRestPlusAPI.model('ChartOfAccountsIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ChartOfAccountsStructureIdentificationTypeV1':
      return flaskRestPlusAPI.model('ChartOfAccountsStructureIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ValueSetIdentificationTypeV1':
      return flaskRestPlusAPI.model('ValueSetIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:VehicleIdentificationTypeV1':
      return flaskRestPlusAPI.model('VehicleIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:VolumeDiscountPlanIdentificationTypeV1':
      return flaskRestPlusAPI.model('VolumeDiscountPlanIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WIPEntityIdentificationTypeV1':
      return flaskRestPlusAPI.model('WIPEntityIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WIPEntityLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('WIPEntityLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WIPOperationIdentificationTypeV1':
      return flaskRestPlusAPI.model('WIPOperationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WIPOperationResourceIdentificationTypeV1':
      return flaskRestPlusAPI.model('WIPOperationResourceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkerIdentificationTypeV1':
      return flaskRestPlusAPI.model('WorkerIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkersCompensationBoardRateGroupIdentificationTypeV1':
      return flaskRestPlusAPI.model('WorkersCompensationBoardRateGroupIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkersCompensationBoardRateGroupClassificationIdentificationTypeV1':
      return flaskRestPlusAPI.model('WorkersCompensationBoardRateGroupClassificationIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkerUnionIdentificationTypeV1':
      return flaskRestPlusAPI.model('WorkerUnionIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkOrderIdentificationTypeV1':
      return flaskRestPlusAPI.model('WorkOrderIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkOrderLineIdentificationTypeV1':
      return flaskRestPlusAPI.model('WorkOrderLineIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ActivityTypeV1':
      return flaskRestPlusAPI.model('ActivityTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomActivityTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ActivityEventTypeV1':
      return flaskRestPlusAPI.model('ActivityEventTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element PlannedStartDateTime has a type that is not catered for (DateTimeType) 0
        'ExpectedStartDateTime': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element ActualStartDateTime has a type that is not catered for (DateTimeType) 0
        #Element ActualCompletionDateTime has a type that is not catered for (DateTimeType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ActivityEventStatusHistoryTypeV1':
      return flaskRestPlusAPI.model('ActivityEventStatusHistoryTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AllowanceTypeV1':
      return flaskRestPlusAPI.model('AllowanceTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Amount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'ReasonCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element PrePaidIndicator has a type that is not catered for (IndicatorType) 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AppointmentWindowTypeV1':
      return flaskRestPlusAPI.model('AppointmentWindowTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'OperationalPreferenceCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAppointmentWindowTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AttachmentTypeV1':
      return flaskRestPlusAPI.model('AttachmentTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'PurposeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Title': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'SizeQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        #Element CreationDateTime has a type that is not catered for (DateTimeType) 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AccountingDistributionTypeV1':
      return flaskRestPlusAPI.model('AccountingDistributionTypeV1', {
        'LedgerID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'AccountClassCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'AllocationTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element AccountingDate has a type that is not catered for (DateType) 0
        #Element Percentage has a type that is not catered for (PercentType) 0
        'Quantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'Amount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'EncumberedQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'EncumberedAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'UnencumberedAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element EncumberedIndicator has a type that is not catered for (IndicatorType) 0
        #Element AllowEncumberanceIndicator has a type that is not catered for (IndicatorType) 0
        'GLEntityID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element  has a type that is not catered for () 0
        'CostCenterCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ProfitCenterCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AddressTypeV1':
      return flaskRestPlusAPI.model('AddressTypeV1', {
        #Element  has a type that is not catered for () 0
        'FormatCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'LineOne': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineTwo': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineThree': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineFour': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineFive': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineSix': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineSeven': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineEight': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineNine': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Building': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element Floor has a type that is not catered for (StringType) 0
        'Area': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'CityName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'StateName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'ProvinceName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'RuralRoute': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'CountyName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'CountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'CountrySubDivisionID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'CitySubDivisionName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'DeliveryPointCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'DeliveryPointBarCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'DeliveryPointTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ProcessingCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'MoveTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element MoveEffectiveDate has a type that is not catered for (DateType) 0
        'AttentionOf': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'CareOf': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'PostalCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'LongPostalCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'GEOCodeID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element InCityLimitIndicator has a type that is not catered for (IndicatorType) 0
        'TimeZoneCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAddressTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BankAccountTypeV1':
      return flaskRestPlusAPI.model('BankAccountTypeV1', {
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'AccountNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'IBANNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'CurrencyCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element CheckDigits has a type that is not catered for (StringType) 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BankDraftTypeV1':
      return flaskRestPlusAPI.model('BankDraftTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'AccountHolderName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'BankName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Number': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'RoutingNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Memo': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element IssuedDate has a type that is not catered for (DateType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankDraftTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BankPaymentTypeV1':
      return flaskRestPlusAPI.model('BankPaymentTypeV1', {
        #Element  has a type that is not catered for () 0
        'ActionTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'InstructionCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'SettlementPriorityCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'SequenceTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ReasonCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'AuthorizationMethodCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'DeliveryMethodCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TransferTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ReferenceCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ChargeBearerCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ChargeAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankPaymentTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BeneficiaryTypeV1':
      return flaskRestPlusAPI.model('BeneficiaryTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element SplitPercent has a type that is not catered for (PercentType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBeneficiaryTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BeneficiaryOrganizationPartyTypeV1':
      return flaskRestPlusAPI.model('BeneficiaryOrganizationPartyTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBeneficiaryOrganizationPartyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BeneficiaryPersonPartyTypeV1':
      return flaskRestPlusAPI.model('BeneficiaryPersonPartyTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBeneficiaryPersonPartyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentDebitCommunicationTypeV1':
      return flaskRestPlusAPI.model('PaymentDebitCommunicationTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentDebitCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentDirectDebitMandateTypeV1':
      return flaskRestPlusAPI.model('PaymentDirectDebitMandateTypeV1', {
        'AuthorizationMethodCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element AuthorizedIndicator has a type that is not catered for (IndicatorType) 0
        #Element SignatureDateTime has a type that is not catered for (DateTimeType) 0
        #Element ElectronicSignature has a type that is not catered for (StringType) 0
        'FrequencyCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element AmendmentIndicator has a type that is not catered for (IndicatorType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentDirectDebitMandateTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentRemittanceCommunicationTypeV1':
      return flaskRestPlusAPI.model('PaymentRemittanceCommunicationTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentRemittanceCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CertificationTypeV1':
      return flaskRestPlusAPI.model('CertificationTypeV1', {
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element IssueDate has a type that is not catered for (DateType) 0
        #Element ExpirationDate has a type that is not catered for (DateType) 0
        'IssuingAuthorityID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element QualifyingGrade has a type that is not catered for (StringType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ChargeTypeV1':
      return flaskRestPlusAPI.model('ChargeTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ChargeFrequencyCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Amount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'ReasonCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element PrePaidIndicator has a type that is not catered for (IndicatorType) 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'DiscountMethodCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CommunicationTypeV1':
      return flaskRestPlusAPI.model('CommunicationTypeV1', {
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AddressCommunicationTypeV1':
      return flaskRestPlusAPI.model('AddressCommunicationTypeV1', {
        #Element  has a type that is not catered for () 0
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EmailCommunicationTypeV1':
      return flaskRestPlusAPI.model('EmailCommunicationTypeV1', {
        #Element HTMLPreferredIndicator has a type that is not catered for (IndicatorType) 0
        #Element URI has a type that is not catered for (URIType) 0
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FaxCommunicationTypeV1':
      return flaskRestPlusAPI.model('FaxCommunicationTypeV1', {
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WebsiteCommunicationTypeV1':
      return flaskRestPlusAPI.model('WebsiteCommunicationTypeV1', {
        #Element WebsiteURI has a type that is not catered for (URIType) 0
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PhoneCommunicationTypeV1':
      return flaskRestPlusAPI.model('PhoneCommunicationTypeV1', {
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CostTypeV1':
      return flaskRestPlusAPI.model('CostTypeV1', {
        'Amount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'PerQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CarryingCostTypeV1':
      return flaskRestPlusAPI.model('CarryingCostTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BaseCostTypeV1':
      return flaskRestPlusAPI.model('BaseCostTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreditCardPaymentTypeV1':
      return flaskRestPlusAPI.model('CreditCardPaymentTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreditChargeAuthorizationTypeV1':
      return flaskRestPlusAPI.model('CreditChargeAuthorizationTypeV1', {
        #Element  has a type that is not catered for () 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TraceNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element VoiceAuthorizationIndicator has a type that is not catered for (IndicatorType) 0
        'ChargeAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element ChargeDateTime has a type that is not catered for (DateTimeType) 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditChargeAuthorizationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreditChargeAuthorizationResponseTypeV1':
      return flaskRestPlusAPI.model('CreditChargeAuthorizationResponseTypeV1', {
        #Element  has a type that is not catered for () 0
        'ActionTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ResponseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'AVSResponseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'PaymentSystemCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'SecurityCheckResponseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element AuthorizationDateTime has a type that is not catered for (DateTimeType) 0
        'AuthorizedAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditChargeAuthorizationResponseTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CurrencyExchangeTypeV1':
      return flaskRestPlusAPI.model('CurrencyExchangeTypeV1', {
        'SourceCurrencyCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element SourceUnitBase has a type that is not catered for (NumericType) 0
        'TargetCurrencyCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element TargetUnitBase has a type that is not catered for (NumericType) 0
        'ConversionRate': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RateTypeV1')),
        #Element RoundingFactor has a type that is not catered for (NumericType) 0
        'ConversionTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element ConversionRateDateTime has a type that is not catered for (DateTimeType) 0
        'SourceCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CheckTypeV1':
      return flaskRestPlusAPI.model('CheckTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'AccountHolder': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'BankName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Number': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'IBAN': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'RoutingNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Memo': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element IssuedDate has a type that is not catered for (DateType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactTypeV1':
      return flaskRestPlusAPI.model('ContactTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element PreferredLanguageCode has a type that is not catered for (LanguageCodeType) 0
        'Department': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'JobTitle': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Responsibility': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element OrganizationIndicator has a type that is not catered for (IndicatorType) 0
        'PreferredCommunicationChannelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'OrganizationName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element BirthDateTime has a type that is not catered for (DateTimeType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactPhoneCommunicationTypeV1':
      return flaskRestPlusAPI.model('ContactPhoneCommunicationTypeV1', {
        #Element  has a type that is not catered for () 0
        'PreferredMediaFormatCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactPhoneCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactFaxCommunicationTypeV1':
      return flaskRestPlusAPI.model('ContactFaxCommunicationTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactFaxCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactEmailCommunicationTypeV1':
      return flaskRestPlusAPI.model('ContactEmailCommunicationTypeV1', {
        #Element  has a type that is not catered for () 0
        'PreferredMediaFormatCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactEmailCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactTelexCommunicationTypeV1':
      return flaskRestPlusAPI.model('ContactTelexCommunicationTypeV1', {
        #Element  has a type that is not catered for () 0
        'PreferredMediaFormatCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactTelexCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactWebsiteCommunicationTypeV1':
      return flaskRestPlusAPI.model('ContactWebsiteCommunicationTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactWebsiteCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContainerReferenceTypeV1':
      return flaskRestPlusAPI.model('ContainerReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContainerReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreditCardTypeV1':
      return flaskRestPlusAPI.model('CreditCardTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Number': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'CardHolderName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'CompanyName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element ExpirationDate has a type that is not catered for (DateType) 0
        #Element ExpirationMonth has a type that is not catered for (MonthType) 0
        #Element ExpirationYear has a type that is not catered for (YearType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'SecurityCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditCardTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DebitCardTypeV1':
      return flaskRestPlusAPI.model('DebitCardTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Number': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'CardHolderName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'CompanyName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element ExpirationDate has a type that is not catered for (DateType) 0
        #Element ExpirationMonth has a type that is not catered for (MonthType) 0
        #Element ExpirationYear has a type that is not catered for (YearType) 0
        #Element  has a type that is not catered for () 0
        #Element PIN has a type that is not catered for (StringType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDebitCardTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DebitCardPaymentTypeV1':
      return flaskRestPlusAPI.model('DebitCardPaymentTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DebitChargeAuthorizationTypeV1':
      return flaskRestPlusAPI.model('DebitChargeAuthorizationTypeV1', {
        #Element  has a type that is not catered for () 0
        'TransactionTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ChargeAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element ChargeDateTime has a type that is not catered for (DateTimeType) 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDebitChargeAuthorizationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DebitChargeAuthorizationResponseTypeV1':
      return flaskRestPlusAPI.model('DebitChargeAuthorizationResponseTypeV1', {
        #Element  has a type that is not catered for () 0
        'ActionTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TraceNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'ResponseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'PaymentSystemCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'DebitNetworkCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDebitChargeAuthorizationResponseTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DataElementTypeV1':
      return flaskRestPlusAPI.model('DataElementTypeV1', {
        'Name': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1')),
        'DataTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element Value has a type that is not catered for (StringType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DependentTypeV1':
      return flaskRestPlusAPI.model('DependentTypeV1', {
        'RelationshipCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDependentTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DependentPersonPartyTypeV1':
      return flaskRestPlusAPI.model('DependentPersonPartyTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDependentPersonPartyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EffectivityTypeV1':
      return flaskRestPlusAPI.model('EffectivityTypeV1', {
        #Element ActiveIndicator has a type that is not catered for (IndicatorType) 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EmploymentGradeReferenceTypeV1':
      return flaskRestPlusAPI.model('EmploymentGradeReferenceTypeV1', {
        #Element EmploymentGradeIdentification has a type that is not catered for (xsd:anyType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEmploymentGradeReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EmploymentAssignmentReferenceTypeV1':
      return flaskRestPlusAPI.model('EmploymentAssignmentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEmploymentAssignmentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FinancialProfileTypeV1':
      return flaskRestPlusAPI.model('FinancialProfileTypeV1', {
        'BalanceAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element BalanceVerificationDateTime has a type that is not catered for (DateTimeType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FinancialAccountTypeV1':
      return flaskRestPlusAPI.model('FinancialAccountTypeV1', {
        #Element  has a type that is not catered for () 0
        'AccountNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element JointHoldingIndicator has a type that is not catered for (IndicatorType) 0
        'JointOperationTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'CurrencyCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankAccountReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FinancialAccountHolderTypeV1':
      return flaskRestPlusAPI.model('FinancialAccountHolderTypeV1', {
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element OwnershipPercent has a type that is not catered for (PercentType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialAccountHolderTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FinancialAccountPersonHolderTypeV1':
      return flaskRestPlusAPI.model('FinancialAccountPersonHolderTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialAccountPersonHolderTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FinancialAccountOrganizationHolderTypeV1':
      return flaskRestPlusAPI.model('FinancialAccountOrganizationHolderTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialAccountOrganizationHolderTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FinancialAccountBalanceTypeV1':
      return flaskRestPlusAPI.model('FinancialAccountBalanceTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Amount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element BalanceDateTime has a type that is not catered for (DateTimeType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialAccountBalanceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:GeographicalCoordinateTypeV1':
      return flaskRestPlusAPI.model('GeographicalCoordinateTypeV1', {
        'AltitudeMeasure': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),
        'LatitudeMeasure': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),
        'LongitudeMeasure': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),
        'LatitudeDirectionCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'LongitudeDirectionCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'SystemID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:GLAccountTypeV1':
      return flaskRestPlusAPI.model('GLAccountTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomGLAccountTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:GLElementTypeV1':
      return flaskRestPlusAPI.model('GLElementTypeV1', {
        #Element SequenceNumber has a type that is not catered for (NumericType) 0
        #Element GLElement has a type that is not catered for (StringType) 0
        'GLElementCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemInstanceTypeV1':
      return flaskRestPlusAPI.model('ItemInstanceTypeV1', {
        'SerialNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'LotNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element ExpirationDateTime has a type that is not catered for (DateTimeType) 0
        'RFID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemInstanceReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemInstanceRangeTypeV1':
      return flaskRestPlusAPI.model('ItemInstanceRangeTypeV1', {
        'StartingSerialNumberID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'EndingSerialNumberID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemInstanceRangeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemInstanceGenealogyTypeV1':
      return flaskRestPlusAPI.model('ItemInstanceGenealogyTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemInstanceGenealogyCompositionTypeV1':
      return flaskRestPlusAPI.model('ItemInstanceGenealogyCompositionTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemInstanceGenealogyCompositionTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NoteTypeV1':
      return flaskRestPlusAPI.model('NoteTypeV1', {
        'Author': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element EntryDateTime has a type that is not catered for (DateTimeType) 0
        'LanguageCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element Content has a type that is not catered for (StringType) 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SignatureNoteTypeV1':
      return flaskRestPlusAPI.model('SignatureNoteTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentTermTypeV1':
      return flaskRestPlusAPI.model('PaymentTermTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Code': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element EffectiveDateTime has a type that is not catered for (DateTimeType) 0
        #Element ProxMonth has a type that is not catered for (NumericType) 0
        #Element ProxDayofMonth has a type that is not catered for (NumericType) 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayerTypeV1':
      return flaskRestPlusAPI.model('PayerTypeV1', {
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayerTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayerPersonPartyTypeV1':
      return flaskRestPlusAPI.model('PayerPersonPartyTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayerPersonPartyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayerOrganizationPartyTypeV1':
      return flaskRestPlusAPI.model('PayerOrganizationPartyTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayerOrganizationPartyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonNameTypeV1':
      return flaskRestPlusAPI.model('PersonNameTypeV1', {
        #Element  has a type that is not catered for () 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'FullName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'FirstName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'MiddleName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'FamilyName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'MaidenName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Title': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Salutation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element Prefix has a type that is not catered for (StringType) 0
        #Element Suffix has a type that is not catered for (StringType) 0
        #Element MilitaryRank has a type that is not catered for (StringType) 0
        'PreferredName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Alias': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProcurementCardTypeV1':
      return flaskRestPlusAPI.model('ProcurementCardTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Number': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'CardHolderName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'CompanyName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element ExpirationDate has a type that is not catered for (DateType) 0
        #Element ExpirationMonth has a type that is not catered for (MonthType) 0
        #Element ExpirationYear has a type that is not catered for (YearType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'SecurityCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditCardTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PreferenceTypeV1':
      return flaskRestPlusAPI.model('PreferenceTypeV1', {
        #Element PriorityRanking has a type that is not catered for (NumericType) 0
        #Element PreferredIndicator has a type that is not catered for (IndicatorType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PrivacyPreferenceTypeV1':
      return flaskRestPlusAPI.model('PrivacyPreferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element SystemDefaultIndicator has a type that is not catered for (IndicatorType) 0
        'CommunicationChannelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'RecordingSystemTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PrivacyProfileTypeV1':
      return flaskRestPlusAPI.model('PrivacyProfileTypeV1', {
        #Element OptOutIndicator has a type that is not catered for (IndicatorType) 0
        'SourceCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ReasonCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PriceTypeV1':
      return flaskRestPlusAPI.model('PriceTypeV1', {
        'Amount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'PerQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PlannedUnitPriceTypeV1':
      return flaskRestPlusAPI.model('PlannedUnitPriceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:UnitPriceTypeV1':
      return flaskRestPlusAPI.model('UnitPriceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MarketUnitPriceTypeV1':
      return flaskRestPlusAPI.model('MarketUnitPriceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RemarkTypeV1':
      return flaskRestPlusAPI.model('RemarkTypeV1', {
        'Code': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Comment': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ReasonTypeV1':
      return flaskRestPlusAPI.model('ReasonTypeV1', {
        'Code': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:UpdateReasonTypeV1':
      return flaskRestPlusAPI.model('UpdateReasonTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FailureReasonTypeV1':
      return flaskRestPlusAPI.model('FailureReasonTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesCommissionTypeV1':
      return flaskRestPlusAPI.model('SalesCommissionTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element Percentage has a type that is not catered for (PercentType) 0
        'Quantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'Amount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'QuotaCreditQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesQuotaTypeV1':
      return flaskRestPlusAPI.model('SalesQuotaTypeV1', {
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'TargetQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesCreditTypeV1':
      return flaskRestPlusAPI.model('SalesCreditTypeV1', {
        'RevenueTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element SplitPercent has a type that is not catered for (PercentType) 0
        'PostSplitQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'PostSplitRevenueAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentSetTypeV1':
      return flaskRestPlusAPI.model('ShipmentSetTypeV1', {
        'SetID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentSetTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SpecificationGroupTypeV1':
      return flaskRestPlusAPI.model('SpecificationGroupTypeV1', {
        'Name': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1')),
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationGroupTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SpecificationTypeV1':
      return flaskRestPlusAPI.model('SpecificationTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StatusTypeV1':
      return flaskRestPlusAPI.model('StatusTypeV1', {
        'Code': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element EffectiveDateTime has a type that is not catered for (DateTimeType) 0
        #Element EffectiveEndDateTime has a type that is not catered for (DateTimeType) 0
        'ReasonCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'SubStatusCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:HiringStatusTypeV1':
      return flaskRestPlusAPI.model('HiringStatusTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StatusHistoryTypeV1':
      return flaskRestPlusAPI.model('StatusHistoryTypeV1', {
        'FromStatusCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ToStatusCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element EffectiveDateTime has a type that is not catered for (DateTimeType) 0
        'ReasonCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ChangeByUserId': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StatusChangeHistoryTypeV1':
      return flaskRestPlusAPI.model('StatusChangeHistoryTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AuditHistoryTypeV1':
      return flaskRestPlusAPI.model('AuditHistoryTypeV1', {
        'CreatedBy': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element CreatedDateTime has a type that is not catered for (DateTimeType) 0
        'UpdatedBy': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element UpdatedDateTime has a type that is not catered for (DateTimeType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StopPaymentInstructionTypeV1':
      return flaskRestPlusAPI.model('StopPaymentInstructionTypeV1', {
        #Element RequestDateTime has a type that is not catered for (DateTimeType) 0
        'ReasonCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TaxTypeV1':
      return flaskRestPlusAPI.model('TaxTypeV1', {
        'Code': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TaxJurisdictionCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TaxAuthorityAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'Amount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element DeclarationDateTime has a type that is not catered for (DateTimeType) 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        'TaxRate': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RateTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TimeDurationTypeV1':
      return flaskRestPlusAPI.model('TimeDurationTypeV1', {
        #Element StartTime has a type that is not catered for (TimeType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StandardWorkingHoursTimeDurationTypeV1':
      return flaskRestPlusAPI.model('StandardWorkingHoursTimeDurationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TimePeriodTypeV1':
      return flaskRestPlusAPI.model('TimePeriodTypeV1', {
        #Element StartDateTime has a type that is not catered for (DateTimeType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SeasonTimePeriodTypeV1':
      return flaskRestPlusAPI.model('SeasonTimePeriodTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StartTimePeriodTypeV1':
      return flaskRestPlusAPI.model('StartTimePeriodTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RelativeEffectiveTimePeriodTypeV1':
      return flaskRestPlusAPI.model('RelativeEffectiveTimePeriodTypeV1', {
        #Element RelativeStartDuration has a type that is not catered for (DurationType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WeeklyWorkingHoursTypeV1':
      return flaskRestPlusAPI.model('WeeklyWorkingHoursTypeV1', {
        #Element MondayDuration has a type that is not catered for (DurationType) 0
        #Element TuesdayDuration has a type that is not catered for (DurationType) 0
        #Element WednesdayDuration has a type that is not catered for (DurationType) 0
        #Element ThursdayDuration has a type that is not catered for (DurationType) 0
        #Element FridayDuration has a type that is not catered for (DurationType) 0
        #Element SaturdayDuration has a type that is not catered for (DurationType) 0
        #Element SundayDuration has a type that is not catered for (DurationType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PositionReferenceTypeV1':
      return flaskRestPlusAPI.model('PositionReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPositionReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:JobReferenceTypeV1':
      return flaskRestPlusAPI.model('JobReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomJobReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:JobFamilyReferenceTypeV1':
      return flaskRestPlusAPI.model('JobFamilyReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomJobFamilyReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DurationToleranceTypeV1':
      return flaskRestPlusAPI.model('DurationToleranceTypeV1', {
        #Element UnderDuration has a type that is not catered for (DurationType) 0
        #Element OverDuration has a type that is not catered for (DurationType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PercentToleranceTypeV1':
      return flaskRestPlusAPI.model('PercentToleranceTypeV1', {
        #Element UnderPercent has a type that is not catered for (PercentType) 0
        #Element OverPercent has a type that is not catered for (PercentType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchasingClosePercentToleranceTypeV1':
      return flaskRestPlusAPI.model('PurchasingClosePercentToleranceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityToleranceTypeV1':
      return flaskRestPlusAPI.model('QuantityToleranceTypeV1', {
        'UnderQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'OverQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentToleranceTypeV1':
      return flaskRestPlusAPI.model('ShipmentToleranceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:UsageTypeV1':
      return flaskRestPlusAPI.model('UsageTypeV1', {
        'UsageCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element PreferredIndicator has a type that is not catered for (IndicatorType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ActivityReferenceTypeV1':
      return flaskRestPlusAPI.model('ActivityReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomActivityReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AssignmentGradeReferenceTypeV1':
      return flaskRestPlusAPI.model('AssignmentGradeReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAssignmentGradeReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AssignmentGradeStepReferenceTypeV1':
      return flaskRestPlusAPI.model('AssignmentGradeStepReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAssignmentGradeStepReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BargainingUnitReferenceTypeV1':
      return flaskRestPlusAPI.model('BargainingUnitReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBargainingUnitReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BatchProductionOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('BatchProductionOrderReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBatchProductionOrderReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:VehicleReferenceTypeV1':
      return flaskRestPlusAPI.model('VehicleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'ManufacturerCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ModelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element ModelYear has a type that is not catered for (YearType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomVehicleReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:VolumeDiscountPlanReferenceTypeV1':
      return flaskRestPlusAPI.model('VolumeDiscountPlanReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomVolumeDiscountPlanReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkerReferenceTypeV1':
      return flaskRestPlusAPI.model('WorkerReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWorkerReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkersCompensationBoardRateGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('WorkersCompensationBoardRateGroupReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWorkersCompensationBoardRateGroupReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkersCompensationBoardRateGroupClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('WorkersCompensationBoardRateGroupClassificationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWorkersCompensationBoardRateGroupClassificationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkerUnionReferenceTypeV1':
      return flaskRestPlusAPI.model('WorkerUnionReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWorkerUnionReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WorkOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('WorkOrderLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWorkOrderLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyReferenceTypeV1':
      return flaskRestPlusAPI.model('PartyReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('OrganizationPartyReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'OrganizationName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('PersonPartyReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:HouseholdPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('HouseholdPartyReferenceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BankPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('BankPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BankAccountHolderPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('BankAccountHolderPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BankChargeBearerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('BankChargeBearerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BidderPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('BidderPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillFromPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('BillFromPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillToPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('BillToPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SoldToPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('SoldToPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OutsourcerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('OutsourcerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BuyerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('BuyerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CarrierPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CarrierPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreditRatingPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CreditRatingPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerPartyAccountReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomerPartyAccountReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerPartyAccountReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerPartyContactReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomerPartyContactReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerPartyContactReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerAgentPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomerAgentPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CustomerServiceRepresentativePersonPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomerServiceRepresentativePersonPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DeliverToPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('DeliverToPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DriverPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('DriverPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EducationalInstitutionReferenceTypeV1':
      return flaskRestPlusAPI.model('EducationalInstitutionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EmployeePartyReferenceTypeV1':
      return flaskRestPlusAPI.model('EmployeePartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EmployerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('EmployerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EstablishmentReferenceTypeV1':
      return flaskRestPlusAPI.model('EstablishmentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEstablishmentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FinancialAccountReferenceTypeV1':
      return flaskRestPlusAPI.model('FinancialAccountReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialAccountReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FinancialInstitutionReferenceTypeV1':
      return flaskRestPlusAPI.model('FinancialInstitutionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MandateSignerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('MandateSignerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ManufacturerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('ManufacturerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MediatorPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('MediatorPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OwnerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('OwnerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartnerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('PartnerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayeePartyReferenceTypeV1':
      return flaskRestPlusAPI.model('PayeePartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayFromPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('PayFromPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:VendorPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('VendorPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CompetitorPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CompetitorPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PrimarySalespersonPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('PrimarySalespersonPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PublisherPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('PublisherPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ReceivingPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('ReceivingPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RemitToPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('RemitToPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequesterPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('RequesterPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequiredByPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('RequiredByPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ResponsiblePartyReferenceTypeV1':
      return flaskRestPlusAPI.model('ResponsiblePartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalespersonPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('SalespersonPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipFromPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('ShipFromPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipToPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('ShipToPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SubscriberPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('SubscriberPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SupplierPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('SupplierPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WarrantySupplierPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('WarrantySupplierPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SupplierPartyTradingLocationProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('SupplierPartyTradingLocationProfileReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSupplierPartyTradingLocationProfileReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BeneficiaryPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('BeneficiaryPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AdjusterPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('AdjusterPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ParticipatingPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('ParticipatingPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyAccountReferenceTypeV1':
      return flaskRestPlusAPI.model('PartyAccountReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayeePartyAccountReferenceTypeV1':
      return flaskRestPlusAPI.model('PayeePartyAccountReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AcademicRankReferenceTypeV1':
      return flaskRestPlusAPI.model('AcademicRankReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAcademicRankReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AccountBalanceAdjustmentReferenceTypeV1':
      return flaskRestPlusAPI.model('AccountBalanceAdjustmentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAccountBalanceAdjustmentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AccountingPeriodReferenceTypeV1':
      return flaskRestPlusAPI.model('AccountingPeriodReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAccountingPeriodReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AccountingRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('AccountingRuleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAccountingRuleReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AdvanceShipmentNoticeReferenceTypeV1':
      return flaskRestPlusAPI.model('AdvanceShipmentNoticeReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAdvanceShipmentNoticeReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AttributeBasedPricingMatrixReferenceTypeV1':
      return flaskRestPlusAPI.model('AttributeBasedPricingMatrixReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAttributeBasedPricingMatrixReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillOfLadingReferenceTypeV1':
      return flaskRestPlusAPI.model('BillOfLadingReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBillOfLadingReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillOfMaterialsReferenceTypeV1':
      return flaskRestPlusAPI.model('BillOfMaterialsReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBillOfMaterialsReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillOfMaterialsComponentItemReferenceTypeV1':
      return flaskRestPlusAPI.model('BillOfMaterialsComponentItemReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBillOfMaterialsComponentItemReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BudgetReferenceTypeV1':
      return flaskRestPlusAPI.model('BudgetReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBudgetReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ClassificationSpecificationGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('ClassificationSpecificationGroupReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomClassificationSpecificationGroupReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IncentiveCompensationPlanComponentReferenceTypeV1':
      return flaskRestPlusAPI.model('IncentiveCompensationPlanComponentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomIncentiveCompensationPlanComponentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemCatalogReferenceTypeV1':
      return flaskRestPlusAPI.model('ItemCatalogReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemCatalogReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ChartOfAccountsStructureReferenceTypeV1':
      return flaskRestPlusAPI.model('ChartOfAccountsStructureReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomChartOfAccountsStructureReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('ClassificationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomClassificationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EnterpriseProjectStructureClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('EnterpriseProjectStructureClassificationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContractReferenceTypeV1':
      return flaskRestPlusAPI.model('ContractReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContractReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContractLineReferenceTypeV1':
      return flaskRestPlusAPI.model('ContractLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContractLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchasingContractReferenceTypeV1':
      return flaskRestPlusAPI.model('PurchasingContractReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchasingContractReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchasingContractLineReferenceTypeV1':
      return flaskRestPlusAPI.model('PurchasingContractLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchasingContractLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceContractLineReferenceTypeV1':
      return flaskRestPlusAPI.model('ServiceContractLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceContractLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreditMemoReferenceTypeV1':
      return flaskRestPlusAPI.model('CreditMemoReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditMemoReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EngineeringChangeOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('EngineeringChangeOrderReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element TypeCode has a type that is not catered for (xsd:anyType) 0
        #Element InitiationDate has a type that is not catered for (xsd:anyType) 0
        #Element ImplementationDate has a type that is not catered for (xsd:anyType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEngineeringChangeOrderReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EngineeringChangeOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('EngineeringChangeOrderLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEngineeringChangeOrderLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemATPRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('ItemATPRuleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemATPRuleReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemPickingRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('ItemPickingRuleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemPickingRuleReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemFormulaReferenceTypeV1':
      return flaskRestPlusAPI.model('ItemFormulaReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemFormulaReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InvoiceReferenceTypeV1':
      return flaskRestPlusAPI.model('InvoiceReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInvoiceReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InvoiceLineReferenceTypeV1':
      return flaskRestPlusAPI.model('InvoiceLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInvoiceLineReferenceTypeV1')),
        'Quantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayableInvoiceReferenceTypeV1':
      return flaskRestPlusAPI.model('PayableInvoiceReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayableInvoiceReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayableInvoiceLineReferenceTypeV1':
      return flaskRestPlusAPI.model('PayableInvoiceLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayableInvoiceLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PositionStandardClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('PositionStandardClassificationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPositionStandardClassificationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ExternalInvoiceReferenceTypeV1':
      return flaskRestPlusAPI.model('ExternalInvoiceReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'TotalAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomExternalInvoiceLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FreightInvoiceReferenceTypeV1':
      return flaskRestPlusAPI.model('FreightInvoiceReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFreightInvoiceReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InvoicingRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('InvoicingRuleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInvoicingRuleReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LaborAgreementReferenceTypeV1':
      return flaskRestPlusAPI.model('LaborAgreementReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLaborAgreementReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LaborAgreementFirstLevelEmployeeClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('LaborAgreementFirstLevelEmployeeClassificationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLaborAgreementFirstLevelEmployeeClassificationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LaborAgreementSecondLevelEmployeeClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('LaborAgreementSecondLevelEmployeeClassificationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLaborAgreementSecondLevelEmployeeClassificationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LaborAgreementThirdLevelEmployeeClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('LaborAgreementThirdLevelEmployeeClassificationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLaborAgreementThirdLevelEmployeeClassificationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LedgerReferenceTypeV1':
      return flaskRestPlusAPI.model('LedgerReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLedgerReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationReferenceTypeV1':
      return flaskRestPlusAPI.model('OrganizationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationUnitReferenceTypeV1':
      return flaskRestPlusAPI.model('OrganizationUnitReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationUnitReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PayEquityJobClassReferenceTypeV1':
      return flaskRestPlusAPI.model('PayEquityJobClassReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayEquityJobClassReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PerformanceReviewRatingReferenceTypeV1':
      return flaskRestPlusAPI.model('PerformanceReviewRatingReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPerformanceReviewRatingReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PerformanceReviewRatingModelReferenceTypeV1':
      return flaskRestPlusAPI.model('PerformanceReviewRatingModelReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPerformanceReviewRatingModelReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonReferenceTypeV1':
      return flaskRestPlusAPI.model('PersonReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceSpecialistPersonReferenceTypeV1':
      return flaskRestPlusAPI.model('ServiceSpecialistPersonReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PositionPoolReferenceTypeV1':
      return flaskRestPlusAPI.model('PositionPoolReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPositionPoolReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PriceListReferenceTypeV1':
      return flaskRestPlusAPI.model('PriceListReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriceListReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PriceListLineReferenceTypeV1':
      return flaskRestPlusAPI.model('PriceListLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriceListLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PricingAgreementReferenceTypeV1':
      return flaskRestPlusAPI.model('PricingAgreementReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPricingAgreementReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProjectNonSchedulableResourceReferenceTypeV1':
      return flaskRestPlusAPI.model('ProjectNonSchedulableResourceReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProjectNonSchedulableResourceReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProjectSchedulableResourceReferenceTypeV1':
      return flaskRestPlusAPI.model('ProjectSchedulableResourceReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProjectSchedulableResourceReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseAgreementReferenceTypeV1':
      return flaskRestPlusAPI.model('PurchaseAgreementReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseAgreementReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseAgreementPriceBreakReferenceTypeV1':
      return flaskRestPlusAPI.model('PurchaseAgreementPriceBreakReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseAgreementPriceBreakReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BlanketPurchaseAgreementReferenceTypeV1':
      return flaskRestPlusAPI.model('BlanketPurchaseAgreementReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBlanketPurchaseAgreementReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('PurchaseOrderReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentificationTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseOrderReferenceTypeV1')),
        #Element OrderDate has a type that is not catered for (DateType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('PurchaseOrderLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Quantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseOrderLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PurchaseOrderShipmentReferenceTypeV1':
      return flaskRestPlusAPI.model('PurchaseOrderShipmentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseOrderShipmentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuoteReferenceTypeV1':
      return flaskRestPlusAPI.model('QuoteReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomQuoteReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuoteLineReferenceTypeV1':
      return flaskRestPlusAPI.model('QuoteLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomQuoteLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuotePriceQualificationReferenceTypeV1':
      return flaskRestPlusAPI.model('QuotePriceQualificationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomQuotePriceQualificationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ReportingPeriodReferenceTypeV1':
      return flaskRestPlusAPI.model('ReportingPeriodReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomReportingPeriodReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ResourceReferenceTypeV1':
      return flaskRestPlusAPI.model('ResourceReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomResourceReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequestForQuoteReferenceTypeV1':
      return flaskRestPlusAPI.model('RequestForQuoteReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequestForQuoteReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequestForQuoteLineReferenceTypeV1':
      return flaskRestPlusAPI.model('RequestForQuoteLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequestForQuoteLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequestForQuotePriceBreakReferenceTypeV1':
      return flaskRestPlusAPI.model('RequestForQuotePriceBreakReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequestForQuotePriceBreakReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequisitionReferenceTypeV1':
      return flaskRestPlusAPI.model('RequisitionReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequisitionReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequisitionLineReferenceTypeV1':
      return flaskRestPlusAPI.model('RequisitionLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequisitionLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RequisitionDistributionReferenceTypeV1':
      return flaskRestPlusAPI.model('RequisitionDistributionReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequisitionDistributionReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RMAReferenceTypeV1':
      return flaskRestPlusAPI.model('RMAReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRMAReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalaryIncreaseMatrixReferenceTypeV1':
      return flaskRestPlusAPI.model('SalaryIncreaseMatrixReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalaryIncreaseMatrixReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalaryPlanReferenceTypeV1':
      return flaskRestPlusAPI.model('SalaryPlanReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalaryPlanReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('SalesOrderReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesOrderReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('SalesOrderLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesOrderLineReferenceTypeV1')),
        'Quantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesOrderScheduleReferenceTypeV1':
      return flaskRestPlusAPI.model('SalesOrderScheduleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesOrderScheduleReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentRequestOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('ShipmentRequestOrderLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentRequestOrderLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TrainingProgramReferenceTypeV1':
      return flaskRestPlusAPI.model('TrainingProgramReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTrainingProgramReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProvisioningOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('ProvisioningOrderReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProvisioningOrderReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProvisioningOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('ProvisioningOrderLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProvisioningOrderLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FulfillmentOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('FulfillmentOrderReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFulfillmentOrderReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FulfillmentOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('FulfillmentOrderLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFulfillmentOrderLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TransportationSalesOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('TransportationSalesOrderReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTransportationSalesOrderReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TransportationSalesOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('TransportationSalesOrderLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTransportationSalesOrderLineReferenceTypeV1')),
        'Quantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesOpportunityReferenceTypeV1':
      return flaskRestPlusAPI.model('SalesOpportunityReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesOpportunityReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceContractCoverageTemplateReferenceTypeV1':
      return flaskRestPlusAPI.model('ServiceContractCoverageTemplateReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceContractCoverageTemplateReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceContractSubscriptionTemplateReferenceTypeV1':
      return flaskRestPlusAPI.model('ServiceContractSubscriptionTemplateReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceContractSubscriptionTemplateReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceRequestReferenceTypeV1':
      return flaskRestPlusAPI.model('ServiceRequestReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceRequestReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RelatedServiceRequestReferenceTypeV1':
      return flaskRestPlusAPI.model('RelatedServiceRequestReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'RelationshipCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRelatedServiceRequestReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SalesTerritoryReferenceTypeV1':
      return flaskRestPlusAPI.model('SalesTerritoryReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesTerritoryReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AccountingEntryIdentificationTypeV1':
      return flaskRestPlusAPI.model('AccountingEntryIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AccountingEntryReferenceTypeV1':
      return flaskRestPlusAPI.model('AccountingEntryReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAccountingEntryReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BankBranchReferenceTypeV1':
      return flaskRestPlusAPI.model('BankBranchReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankBranchReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BillingProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('BillingProfileReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBillingProfileReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BusinessUnitFunctionReferenceTypeV1':
      return flaskRestPlusAPI.model('BusinessUnitFunctionReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBusinessUnitFunctionReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FinancialBusinessUnitReferenceTypeV1':
      return flaskRestPlusAPI.model('FinancialBusinessUnitReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CalendarReferenceTypeV1':
      return flaskRestPlusAPI.model('CalendarReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCalendarReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CareerPathReferenceTypeV1':
      return flaskRestPlusAPI.model('CareerPathReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCareerPathReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ChartOfAccountsReferenceTypeV1':
      return flaskRestPlusAPI.model('ChartOfAccountsReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomChartOfAccountsReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CompensationPackageRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('CompensationPackageRuleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCompensationPackageRuleReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CompensationPackageTemplateReferenceTypeV1':
      return flaskRestPlusAPI.model('CompensationPackageTemplateReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCompensationPackageTemplateReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ConfigurationReferenceTypeV1':
      return flaskRestPlusAPI.model('ConfigurationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomConfigurationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DirectDebitMandateReferenceTypeV1':
      return flaskRestPlusAPI.model('DirectDebitMandateReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDirectDebitMandateReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FestivalAdvancePayProgramReferenceTypeV1':
      return flaskRestPlusAPI.model('FestivalAdvancePayProgramReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFestivalAdvancePayProgramReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FundReferenceTypeV1':
      return flaskRestPlusAPI.model('FundReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFundReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:GovernmentAgencyReferenceTypeV1':
      return flaskRestPlusAPI.model('GovernmentAgencyReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomGovernmentAgencyReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:INAILRiskProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('INAILRiskProfileReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomINAILRiskProfileReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InstalledProductReferenceTypeV1':
      return flaskRestPlusAPI.model('InstalledProductReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'SerialNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'AlternateTrackingNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInstalledProductReferenceTypeV1')),
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WarrantyItemReferenceTypeV1':
      return flaskRestPlusAPI.model('WarrantyItemReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemFormulaMaterialReferenceTypeV1':
      return flaskRestPlusAPI.model('ItemFormulaMaterialReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemFormulaMaterialReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemLotReferenceTypeV1':
      return flaskRestPlusAPI.model('ItemLotReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemLotReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemStructureReferenceTypeV1':
      return flaskRestPlusAPI.model('ItemStructureReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemStructureReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemStructureComponentItemReferenceTypeV1':
      return flaskRestPlusAPI.model('ItemStructureComponentItemReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemStructureComponentItemReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LegalEntityReferenceTypeV1':
      return flaskRestPlusAPI.model('LegalEntityReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLegalEntityReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LegislativeDataGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('LegislativeDataGroupReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLegislativeDataGroupReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LocationReferenceTypeV1':
      return flaskRestPlusAPI.model('LocationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Directions': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        'TimeZoneIdentifier': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLocationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LocationParentTypeV1':
      return flaskRestPlusAPI.model('LocationParentTypeV1', {
        #Element SequenceNumber has a type that is not catered for (NumericType) 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLocationParentTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:InventoryTransactionReferenceTypeV1':
      return flaskRestPlusAPI.model('InventoryTransactionReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInventoryTransactionReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ManufacturingRoutingReferenceTypeV1':
      return flaskRestPlusAPI.model('ManufacturingRoutingReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomManufacturingRoutingReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ManufacturingRoutingActivityReferenceTypeV1':
      return flaskRestPlusAPI.model('ManufacturingRoutingActivityReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomManufacturingRoutingActivityReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ManufacturingRoutingOperationReferenceTypeV1':
      return flaskRestPlusAPI.model('ManufacturingRoutingOperationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomManufacturingRoutingOperationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MarketingEventReferenceTypeV1':
      return flaskRestPlusAPI.model('MarketingEventReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Objective': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMarketingEventReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MarketingOfferReferenceTypeV1':
      return flaskRestPlusAPI.model('MarketingOfferReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMarketingOfferReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MarketingTreatmentReferenceTypeV1':
      return flaskRestPlusAPI.model('MarketingTreatmentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMarketingTreatmentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ObjectReferenceTypeV1':
      return flaskRestPlusAPI.model('ObjectReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomObjectReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OperationReferenceTypeV1':
      return flaskRestPlusAPI.model('OperationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOperationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentReferenceTypeV1':
      return flaskRestPlusAPI.model('PaymentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DisbursedPaymentReferenceTypeV1':
      return flaskRestPlusAPI.model('DisbursedPaymentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'PaymentAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element ClearedDate has a type that is not catered for (DateType) 0
        'ClearedAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDisbursedPaymentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaymentLineReferenceTypeV1':
      return flaskRestPlusAPI.model('PaymentLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PriceFormulaReferenceTypeV1':
      return flaskRestPlusAPI.model('PriceFormulaReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriceFormulaReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProductionOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('ProductionOrderReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProductionOrderReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProductionOrderActivityReferenceTypeV1':
      return flaskRestPlusAPI.model('ProductionOrderActivityReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProductionOrderActivityReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProductionOrderMaterialReferenceTypeV1':
      return flaskRestPlusAPI.model('ProductionOrderMaterialReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProductionOrderMaterialReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProductionOrderOperationReferenceTypeV1':
      return flaskRestPlusAPI.model('ProductionOrderOperationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProductionOrderOperationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProductionOrderResourceReferenceTypeV1':
      return flaskRestPlusAPI.model('ProductionOrderResourceReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProductionOrderResourceReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProjectReferenceTypeV1':
      return flaskRestPlusAPI.model('ProjectReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProjectReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProjectTaskReferenceTypeV1':
      return flaskRestPlusAPI.model('ProjectTaskReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProjectTaskReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PromotionReferenceTypeV1':
      return flaskRestPlusAPI.model('PromotionReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPromotionReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RecipeReferenceTypeV1':
      return flaskRestPlusAPI.model('RecipeReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRecipeReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RecipeValidityRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('RecipeValidityRuleReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRecipeValidityRuleReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RegionReferenceTypeV1':
      return flaskRestPlusAPI.model('RegionReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRegionReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ResourceAvailabilityCalendarReferenceTypeV1':
      return flaskRestPlusAPI.model('ResourceAvailabilityCalendarReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomResourceAvailabilityCalendarReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ServiceCreditCalculationGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('ServiceCreditCalculationGroupReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceCreditCalculationGroupReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentReferenceTypeV1':
      return flaskRestPlusAPI.model('ShipmentReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentItemReferenceTypeV1':
      return flaskRestPlusAPI.model('ShipmentItemReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SpecificationReferenceTypeV1':
      return flaskRestPlusAPI.model('SpecificationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SpecificationGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('SpecificationGroupReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationGroupReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SpecificationValueSetReferenceTypeV1':
      return flaskRestPlusAPI.model('SpecificationValueSetReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationValueSetReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SpecificationValueSetLineReferenceTypeV1':
      return flaskRestPlusAPI.model('SpecificationValueSetLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Value': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationValueSetLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SupportTeamReferenceTypeV1':
      return flaskRestPlusAPI.model('SupportTeamReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSupportTeamReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SettlementReferenceTypeV1':
      return flaskRestPlusAPI.model('SettlementReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSettlementReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SignatoryGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('SignatoryGroupReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSignatoryGroupReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BusinessCalendarReferenceTypeV1':
      return flaskRestPlusAPI.model('BusinessCalendarReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBusinessCalendarReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('TalentProfileReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileInstanceQualifierReferenceTypeV1':
      return flaskRestPlusAPI.model('TalentProfileInstanceQualifierReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileInstanceQualifierReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileInstanceQualifierSetReferenceTypeV1':
      return flaskRestPlusAPI.model('TalentProfileInstanceQualifierSetReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileInstanceQualifierSetReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileTypeReferenceTypeV1':
      return flaskRestPlusAPI.model('TalentProfileTypeReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileTypeReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileContentItemCatalogReferenceTypeV1':
      return flaskRestPlusAPI.model('TalentProfileContentItemCatalogReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileContentItemCatalogReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileContentItemReferenceTypeV1':
      return flaskRestPlusAPI.model('TalentProfileContentItemReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileContentItemReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileContentTypeReferenceTypeV1':
      return flaskRestPlusAPI.model('TalentProfileContentTypeReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileContentTypeReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TalentProfileContentTypePropertyReferenceTypeV1':
      return flaskRestPlusAPI.model('TalentProfileContentTypePropertyReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileContentTypePropertyReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TeamReferenceTypeV1':
      return flaskRestPlusAPI.model('TeamReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTeamReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ValueSetReferenceTypeV1':
      return flaskRestPlusAPI.model('ValueSetReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomValueSetReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:GLElementValueSetReferenceTypeV1':
      return flaskRestPlusAPI.model('GLElementValueSetReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CostCenterGLElementValueSetReferenceTypeV1':
      return flaskRestPlusAPI.model('CostCenterGLElementValueSetReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LegalEntityGLElementValueSetReferenceTypeV1':
      return flaskRestPlusAPI.model('LegalEntityGLElementValueSetReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WIPEntityReferenceTypeV1':
      return flaskRestPlusAPI.model('WIPEntityReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWIPEntityReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WIPEntityLineReferenceTypeV1':
      return flaskRestPlusAPI.model('WIPEntityLineReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWIPEntityLineReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WIPOperationReferenceTypeV1':
      return flaskRestPlusAPI.model('WIPOperationReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWIPOperationReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WIPOperationResourceReferenceTypeV1':
      return flaskRestPlusAPI.model('WIPOperationResourceReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWIPOperationResourceReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentChargeTypeV1':
      return flaskRestPlusAPI.model('ShipmentChargeTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentItemTypeV1':
      return flaskRestPlusAPI.model('ShipmentItemTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ItemLotNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'OrderedQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'StagedQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'ShippedQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'BackorderedQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'CanceledQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'ItemNetWeight': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),
        'ItemVolume': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),
        'HazardClassCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element RequestedDate has a type that is not catered for (DateType) 0
        #Element PromisedDate has a type that is not catered for (DateType) 0
        'ContainerSealNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'TrackingID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'PackingInstruction': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'EndingSerialNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'StartingSerialNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element ActualShipDateTime has a type that is not catered for (DateTimeType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentChargeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentFulfillmentOrderScheduleTypeV1':
      return flaskRestPlusAPI.model('ShipmentFulfillmentOrderScheduleTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentFulfillmentOrderScheduleTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentItemLotTypeV1':
      return flaskRestPlusAPI.model('ShipmentItemLotTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element ExpirationDate has a type that is not catered for (DateType) 0
        #Element RetestDateTime has a type that is not catered for (DateTimeType) 0
        #Element BestByDate has a type that is not catered for (DateType) 0
        #Element SellByDate has a type that is not catered for (DateType) 0
        #Element CreationDateTime has a type that is not catered for (DateTimeType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemLotTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentItemInstanceGenealogyTypeV1':
      return flaskRestPlusAPI.model('ShipmentItemInstanceGenealogyTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:ShipmentItemInstanceGenealogyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentItemInstanceTypeV1':
      return flaskRestPlusAPI.model('ShipmentItemInstanceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemInstanceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentItemInstanceRangeTypeV1':
      return flaskRestPlusAPI.model('ShipmentItemInstanceRangeTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemInstanceRangeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ShipmentItemChargeTypeV1':
      return flaskRestPlusAPI.model('ShipmentItemChargeTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemChargeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyTypeV1':
      return flaskRestPlusAPI.model('PartyTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyRelatedPartyTypeV1':
      return flaskRestPlusAPI.model('PartyRelatedPartyTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyRelatedPartyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyRelationshipTypeV1':
      return flaskRestPlusAPI.model('PartyRelationshipTypeV1', {
        #Element  has a type that is not catered for () 0
        'RelationshipCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyRelationshipTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyRelatedPersonPartyTypeV1':
      return flaskRestPlusAPI.model('PartyRelatedPersonPartyTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyRelatedPersonPartyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyRelatedHouseholdPartyTypeV1':
      return flaskRestPlusAPI.model('PartyRelatedHouseholdPartyTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyRelatedHouseholdPartyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyRelatedOrganizationPartyTypeV1':
      return flaskRestPlusAPI.model('PartyRelatedOrganizationPartyTypeV1', {
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyRelatedOrganizationPartyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyContactTypeV1':
      return flaskRestPlusAPI.model('PartyContactTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyContactTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationTypeV1':
      return flaskRestPlusAPI.model('OrganizationTypeV1', {
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'ShortName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Salutation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'IncorporationLocation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'IncorporationCountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'DUNSInquiryIdentifier': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'LegalStructureCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element ControlYear has a type that is not catered for (YearType) 0
        #Element TotalEmployeeCount has a type that is not catered for (PositiveIntegerType) 0
        'LocationUsageCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element OutOfBusinessIndicator has a type that is not catered for (IndicatorType) 0
        'LineOfBusiness': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'CongressionalDistrictCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element ImportIndicator has a type that is not catered for (IndicatorType) 0
        #Element ExportIndicator has a type that is not catered for (IndicatorType) 0
        #Element LaborSurplusIndicator has a type that is not catered for (IndicatorType) 0
        #Element MinorityOwnedIndicator has a type that is not catered for (IndicatorType) 0
        'MinorityOwnedTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element WonamOwnedIndicator has a type that is not catered for (IndicatorType) 0
        #Element DisadvantagedIndicator has a type that is not catered for (IndicatorType) 0
        #Element SmallBusinessIndicator has a type that is not catered for (IndicatorType) 0
        'FacilityOccupancyCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element DunBradstreetCreditRating has a type that is not catered for (NumericType) 0
        'TaxPayerRegistrationID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'TaxPayerIdentificationNumberID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'TaxPayerRegistrationNumberID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element FinancialAnalysisFiscalYear has a type that is not catered for (YearType) 0
        #Element FiscalYearEndMonth has a type that is not catered for (MonthType) 0
        'CurrentFiscalYearPotentitalRevenue': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'NextFiscalYearPotentitalRevenue': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element EstablishmentYear has a type that is not catered for (YearType) 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'OperationalScopeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TaxationClassificationCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'LocalBusinessID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'PreferredFunctionalCurrencyCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'RegistrationCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element SubsidiaryIndicator has a type that is not catered for (IndicatorType) 0
        'SICCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element PrivateOwnershipIndicator has a type that is not catered for (IndicatorType) 0
        'LocalActivityClassificationCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element InternalIndicator has a type that is not catered for (IndicatorType) 0
        #Element SimilarSoundingBusiness has a type that is not catered for (StringType) 0
        'HomeCountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element StockSymbol has a type that is not catered for (StringType) 0
        'GrowthStrategyDescription': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'MissionStatement': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationCertificationTypeV1':
      return flaskRestPlusAPI.model('OrganizationCertificationTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationCertificationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationCreditRatingTypeV1':
      return flaskRestPlusAPI.model('OrganizationCreditRatingTypeV1', {
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'RatingCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element RatingDate has a type that is not catered for (DateType) 0
        #Element DebarmentIndicator has a type that is not catered for (IndicatorType) 0
        #Element DebarmentCount has a type that is not catered for (PositiveIntegerType) 0
        #Element LastDebarmentDate has a type that is not catered for (DateType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationCreditRatingTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationFinancialProfileTypeV1':
      return flaskRestPlusAPI.model('OrganizationFinancialProfileTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationFinancialProfileTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationFinancialStatementTypeV1':
      return flaskRestPlusAPI.model('OrganizationFinancialStatementTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element IssueDate has a type that is not catered for (DateType) 0
        'EffectiveTimePeriodDescription': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element AuditIndicator has a type that is not catered for (IndicatorType) 0
        #Element ConsolidationIndicator has a type that is not catered for (IndicatorType) 0
        #Element EstimateIndicator has a type that is not catered for (IndicatorType) 0
        #Element FiscalPeriodIndicator has a type that is not catered for (IndicatorType) 0
        #Element FinalStatementIndicator has a type that is not catered for (IndicatorType) 0
        #Element ForecastIndicator has a type that is not catered for (IndicatorType) 0
        #Element OpeningStatementIndicator has a type that is not catered for (IndicatorType) 0
        #Element ProformaIndicator has a type that is not catered for (IndicatorType) 0
        #Element AuditorQualifiedIndicator has a type that is not catered for (IndicatorType) 0
        #Element RestatementIndicator has a type that is not catered for (IndicatorType) 0
        #Element PrincipalSignatureIndicator has a type that is not catered for (IndicatorType) 0
        #Element TrialBalanceIndicator has a type that is not catered for (IndicatorType) 0
        #Element UnbalancedIndicator has a type that is not catered for (IndicatorType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationFinancialStatementTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationEmploymentStatisticsTypeV1':
      return flaskRestPlusAPI.model('OrganizationEmploymentStatisticsTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEmploymentStatisticsTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PrimaryAddressEmploymentDetailTypeV1':
      return flaskRestPlusAPI.model('PrimaryAddressEmploymentDetailTypeV1', {
        #Element EmployeeCount has a type that is not catered for (PositiveIntegerType) 0
        #Element EstimatedCountIndicator has a type that is not catered for (IndicatorType) 0
        #Element MinimumCountIndicator has a type that is not catered for (IndicatorType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPrimaryAddressEmploymentDetailTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TotalEmploymentTypeV1':
      return flaskRestPlusAPI.model('TotalEmploymentTypeV1', {
        #Element EmployeeCount has a type that is not catered for (PositiveIntegerType) 0
        #Element SubsidiaryCountIncludedIndicator has a type that is not catered for (IndicatorType) 0
        #Element EstimatedCountIndicator has a type that is not catered for (IndicatorType) 0
        'EmploymentCountCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTotalEmploymentTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CommercialCreditScoreTypeV1':
      return flaskRestPlusAPI.model('CommercialCreditScoreTypeV1', {
        #Element Score has a type that is not catered for (NumericType) 0
        'ScoreExplanation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element CalculationDate has a type that is not catered for (DateType) 0
        'ClassExplanation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element Percentile has a type that is not catered for (PercentType) 0
        #Element MonthDuration has a type that is not catered for (MonthType) 0
        'AverageHighCreditAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'HighestCreditAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'MaximumRecommendedCreditAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element TradeExperienceCount has a type that is not catered for (PositiveIntegerType) 0
        'OverrideCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCommercialCreditScoreTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreditScoreCommentaryTypeV1':
      return flaskRestPlusAPI.model('CreditScoreCommentaryTypeV1', {
        'Commentary': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'SlowTradeExplanation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'NegativePaymentExplanation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'PublicRecordsExplanation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element DetrimentalHistoryIndicator has a type that is not catered for (IndicatorType) 0
        #Element FinancialTroubleIndicator has a type that is not catered for (IndicatorType) 0
        #Element CriminalProceedingIndicator has a type that is not catered for (IndicatorType) 0
        #Element OpenClaimIndicator has a type that is not catered for (IndicatorType) 0
        #Element SecuredFilingIndicator has a type that is not catered for (IndicatorType) 0
        #Element SpecialDetrimentalHistoryIndicator has a type that is not catered for (IndicatorType) 0
        #Element DisasterIndicator has a type that is not catered for (IndicatorType) 0
        #Element OperationalChangeIndicator has a type that is not catered for (IndicatorType) 0
        #Element MiscellaneousEventIndicator has a type that is not catered for (IndicatorType) 0
        #Element LegalSuitIndicator has a type that is not catered for (IndicatorType) 0
        #Element LienIndicator has a type that is not catered for (IndicatorType) 0
        #Element JudgementIndicator has a type that is not catered for (IndicatorType) 0
        #Element BankruptcyIndicator has a type that is not catered for (IndicatorType) 0
        #Element TradeExperienceIndicator has a type that is not catered for (IndicatorType) 0
        #Element BusinessDiscontinuedIndicator has a type that is not catered for (IndicatorType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditScoreCommentaryTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EstimatedDelinquentPaymentIncidenceTypeV1':
      return flaskRestPlusAPI.model('EstimatedDelinquentPaymentIncidenceTypeV1', {
        #Element RangePercent has a type that is not catered for (PercentType) 0
        #Element AllFirmsPercent has a type that is not catered for (PercentType) 0
        #Element LowRangeScore has a type that is not catered for (IntegerType) 0
        #Element HighRangeScore has a type that is not catered for (IntegerType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEstimatedDelinquentPaymentIncidenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FailureRiskTypeV1':
      return flaskRestPlusAPI.model('FailureRiskTypeV1', {
        #Element Score has a type that is not catered for (NumericType) 0
        #Element Age has a type that is not catered for (PositiveIntegerType) 0
        'ClassificationCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element CalculationDate has a type that is not catered for (DateType) 0
        #Element ScoreRangeFailureProbabilityPercent has a type that is not catered for (PercentType) 0
        #Element NationalPercentile has a type that is not catered for (NumericType) 0
        'OverrideCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element GlobalScore has a type that is not catered for (NumericType) 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFailureRiskTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BankruptcyTypeV1':
      return flaskRestPlusAPI.model('BankruptcyTypeV1', {
        #Element BankruptcyIndicator has a type that is not catered for (IndicatorType) 0
        #Element FilingCount has a type that is not catered for (PositiveIntegerType) 0
        'FilingTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'FilingChapterCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element FilingDate has a type that is not catered for (DateType) 0
        #Element ConversionCount has a type that is not catered for (PositiveIntegerType) 0
        #Element ConversionDate has a type that is not catered for (DateType) 0
        'ConvertedFilingChapterCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomParentBankruptcyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PassportTypeV1':
      return flaskRestPlusAPI.model('PassportTypeV1', {
        'NumberID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element IssueDate has a type that is not catered for (DateType) 0
        #Element ExpirationDate has a type that is not catered for (DateType) 0
        'IssuingCountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'IssuingStateCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'IssuingLocation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'IssuingAuthority': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPassportTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaydexTypeV1':
      return flaskRestPlusAPI.model('PaydexTypeV1', {
        #Element Score has a type that is not catered for (NumericType) 0
        #Element ThreeMonthEarlierScore has a type that is not catered for (NumericType) 0
        #Element FirmDays has a type that is not catered for (DurationType) 0
        'FirmComment': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element IndustryDays has a type that is not catered for (DurationType) 0
        'IndustryComment': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Comment': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaydexTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PaydexNormTypeV1':
      return flaskRestPlusAPI.model('PaydexNormTypeV1', {
        #Element UpperScore has a type that is not catered for (NumericType) 0
        #Element MedianScore has a type that is not catered for (NumericType) 0
        #Element LowerScore has a type that is not catered for (NumericType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaydexNormTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProcessParameterTypeV1':
      return flaskRestPlusAPI.model('ProcessParameterTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'MinimumValue': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),
        'MaximumValue': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:OrganizationFinancialNumberTypeV1':
      return flaskRestPlusAPI.model('OrganizationFinancialNumberTypeV1', {
        #Element  has a type that is not catered for () 0
        'NumberLabel': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Amount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        #Element ActualIndicator has a type that is not catered for (IndicatorType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationFinancialNumberTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonTypeV1':
      return flaskRestPlusAPI.model('PersonTypeV1', {
        'PrimaryClassificationCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element NameInitial has a type that is not catered for (StringType) 0
        'GenderCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'MaritalStatusCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element BirthDateTime has a type that is not catered for (DateTimeType) 0
        #Element DeathDateTime has a type that is not catered for (DateTimeType) 0
        #Element DeathPlace has a type that is not catered for (StringType) 0
        'DeathCertificateID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element VeteranBenefitEligibilityIndicator has a type that is not catered for (IndicatorType) 0
        #Element Age has a type that is not catered for (PositiveIntegerType) 0
        'LanguageCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'NationalityCountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TaxPayerRegistrationNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'TaxPayerIdentificationNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'PrimaryLocationTimezoneCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element BirthPlace has a type that is not catered for (StringType) 0
        'EthnicityCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element MaritalStatusEffectiveDate has a type that is not catered for (DateType) 0
        'PersonalIncomeAmount': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1')),
        'RentOrOwnCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element DeceasedIndicator has a type that is not catered for (IndicatorType) 0
        #Element BankruptcyIndicator has a type that is not catered for (IndicatorType) 0
        #Element ProblematicAccountIndicator has a type that is not catered for (IndicatorType) 0
        #Element TaxLienIndicator has a type that is not catered for (IndicatorType) 0
        #Element EmployedIndicator has a type that is not catered for (IndicatorType) 0
        #Element TotalDependentCount has a type that is not catered for (NonNegativeIntegerType) 0
        #Element MinorIndicator has a type that is not catered for (IndicatorType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonNameUsageTypeV1':
      return flaskRestPlusAPI.model('PersonNameUsageTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'DisplayName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'LegislationCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonNameUsageTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DriversLicenseClassTypeV1':
      return flaskRestPlusAPI.model('DriversLicenseClassTypeV1', {
        #Element  has a type that is not catered for () 0
        'LicenseClassCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDriversLicenseClassTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonDriversLicenseTypeV1':
      return flaskRestPlusAPI.model('PersonDriversLicenseTypeV1', {
        #Element  has a type that is not catered for () 0
        'LegislationAuthorityCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'IssuingAuthority': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'IssuingCountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element SuspendedIndicator has a type that is not catered for (IndicatorType) 0
        #Element SuspendedFromDate has a type that is not catered for (DateType) 0
        #Element PenaltyPointCount has a type that is not catered for (IntegerType) 0
        #Element ViolationCount has a type that is not catered for (IntegerType) 0
        'IssuingLocation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Comment': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonDriversLicenseTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonAffiliationTypeV1':
      return flaskRestPlusAPI.model('PersonAffiliationTypeV1', {
        #Element  has a type that is not catered for () 0
        'AffiliationCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element PriorityRanking has a type that is not catered for (NumericType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonAffiliationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonNationalIdentityTypeV1':
      return flaskRestPlusAPI.model('PersonNationalIdentityTypeV1', {
        #Element  has a type that is not catered for () 0
        'IssuingCountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element PrimaryIndicator has a type that is not catered for (IndicatorType) 0
        #Element TaxIDIndicator has a type that is not catered for (IndicatorType) 0
        #Element IssueDate has a type that is not catered for (DateType) 0
        #Element ExpirationDate has a type that is not catered for (DateType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonNationalIdentityTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonProfessionalLicenseTypeV1':
      return flaskRestPlusAPI.model('PersonProfessionalLicenseTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'NumberID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'IssuingStateCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonProfessionalLicenseTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CitizenshipTypeV1':
      return flaskRestPlusAPI.model('CitizenshipTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element CitizenByBirthIndicator has a type that is not catered for (IndicatorType) 0
        'CountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element DisownmentDate has a type that is not catered for (DateType) 0
        #Element RecognitionDate has a type that is not catered for (DateType) 0
        #Element EndDate has a type that is not catered for (DateType) 0
        'CitizenshipDocumentID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCitizenshipTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EducationRecordTypeV1':
      return flaskRestPlusAPI.model('EducationRecordTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element ClassYear has a type that is not catered for (YearType) 0
        #Element MajorCourseCategory has a type that is not catered for (StringType) 0
        #Element AbbreviatedEducationalDegree has a type that is not catered for (StringType) 0
        #Element AttendanceLastDate has a type that is not catered for (DateType) 0
        #Element AttendanceStartDate has a type that is not catered for (DateType) 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEducationRecordTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EmploymentRecordTypeV1':
      return flaskRestPlusAPI.model('EmploymentRecordTypeV1', {
        #Element  has a type that is not catered for () 0
        'EmployerOrganizationName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'EmployerDivisionName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'JobTitleCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'JobTitle': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element StartDate has a type that is not catered for (DateType) 0
        #Element EndDate has a type that is not catered for (DateType) 0
        #Element EmploymentDuration has a type that is not catered for (DurationType) 0
        'PositionTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'SupervisorName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'ResponsibilityName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'TenureCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element WeeklyWorkDuration has a type that is not catered for (DurationType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEmploymentRecordTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonInterestTypeV1':
      return flaskRestPlusAPI.model('PersonInterestTypeV1', {
        #Element  has a type that is not catered for () 0
        'InterestTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'InterestLevelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ParticipationLevelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element EffectiveStartDate has a type that is not catered for (DateType) 0
        #Element SportIndicator has a type that is not catered for (IndicatorType) 0
        'FavoriteSportsTeamName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonInterestTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LanguageProficiencyTypeV1':
      return flaskRestPlusAPI.model('LanguageProficiencyTypeV1', {
        #Element  has a type that is not catered for () 0
        'LanguageCodeType': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element NativeLanguageIndicator has a type that is not catered for (IndicatorType) 0
        #Element PrimaryLanguageIndicator has a type that is not catered for (IndicatorType) 0
        'ReadingAbilityLevelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'WritingAbilityLevelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'SpeakingAbilityLevelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'SpeechComprehensibilityCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLanguageProficiencyTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonCertificationTypeV1':
      return flaskRestPlusAPI.model('PersonCertificationTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonCertificationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonFinancialProfileTypeV1':
      return flaskRestPlusAPI.model('PersonFinancialProfileTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonFinancialProfileTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MilitaryEmploymentTypeV1':
      return flaskRestPlusAPI.model('MilitaryEmploymentTypeV1', {
        #Element Rank has a type that is not catered for (StringType) 0
        'MilitaryBranchCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'MilitaryServiceLocationName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'MilitaryStationName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMilitaryEmploymentTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:VisaTypeV1':
      return flaskRestPlusAPI.model('VisaTypeV1', {
        'NumberID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ClassificationCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'IssuingCountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element IssueDate has a type that is not catered for (DateType) 0
        #Element ExpirationDate has a type that is not catered for (DateType) 0
        'IssuingLocation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'IssuingAuthority': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomVisaTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemStructureTypeV1':
      return flaskRestPlusAPI.model('ItemStructureTypeV1', {
        #Element  has a type that is not catered for () 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element AttributeOverrideAllowedIndicator has a type that is not catered for (IndicatorType) 0
        #Element ImplementationDate has a type that is not catered for (DateType) 0
        'EffectivityControlCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element PrimaryIndicator has a type that is not catered for (IndicatorType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ComponentItemTypeV1':
      return flaskRestPlusAPI.model('ComponentItemTypeV1', {
        #Element  has a type that is not catered for () 0
        'StorageUnitCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Quantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'BasisQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'Comment': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element OptionalIndicator has a type that is not catered for (IndicatorType) 0
        'ModelPlanLevelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element OptionalOnModelIndicator has a type that is not catered for (IndicatorType) 0
        #Element MutuallyExclusiveOptionIndicator has a type that is not catered for (IndicatorType) 0
        #Element CostRollupInclusionIndicator has a type that is not catered for (IndicatorType) 0
        #Element ATPCheckRequiredIndicator has a type that is not catered for (IndicatorType) 0
        #Element ShippingAllowedIndicator has a type that is not catered for (IndicatorType) 0
        #Element ShippingDocumentVisibilityIndicator has a type that is not catered for (IndicatorType) 0
        'FromUnitNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'ToUnitNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'FromRevisionNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'ToRevisionNumber': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'MinimumOrderQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        'MaximumOrderQuantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        #Element FractionAllowedIndicator has a type that is not catered for (IndicatorType) 0
        #Element AutoRequestIndicator has a type that is not catered for (IndicatorType) 0
        #Element RequiredToShipIndicator has a type that is not catered for (IndicatorType) 0
        #Element RequiredForRevenueIndicator has a type that is not catered for (IndicatorType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ComponentItemSpecificationGroupTypeV1':
      return flaskRestPlusAPI.model('ComponentItemSpecificationGroupTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomComponentItemSpecificationGroupTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemStructureAttachmentTypeV1':
      return flaskRestPlusAPI.model('ItemStructureAttachmentTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemStructureAttachmentTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ItemStructureSpecificationGroupTypeV1':
      return flaskRestPlusAPI.model('ItemStructureSpecificationGroupTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemStructureSpecificationGroupTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SubstituteComponentItemTypeV1':
      return flaskRestPlusAPI.model('SubstituteComponentItemTypeV1', {
        #Element  has a type that is not catered for () 0
        'Quantity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1')),
        #Element FractionAllowedIndicator has a type that is not catered for (IndicatorType) 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ValueSetTypeV1':
      return flaskRestPlusAPI.model('ValueSetTypeV1', {
        #Element  has a type that is not catered for () 0
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'DataTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element MinimumValue has a type that is not catered for (StringType) 0
        #Element MaximumValue has a type that is not catered for (StringType) 0
        #Element MinimumLength has a type that is not catered for (NonNegativeIntegerType) 0
        #Element MaximumLength has a type that is not catered for (IntegerType) 0
        #Element RestrictedValueIndicator has a type that is not catered for (IndicatorType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ValueSetLineTypeV1':
      return flaskRestPlusAPI.model('ValueSetLineTypeV1', {
        #Element  has a type that is not catered for () 0
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Value': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:GLElementValueSetLineTypeV1':
      return flaskRestPlusAPI.model('GLElementValueSetLineTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationTypeV1':
      return flaskRestPlusAPI.model('CustomSpecificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationGroupTypeV1':
      return flaskRestPlusAPI.model('CustomSpecificationGroupTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationUnitReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomOrganizationUnitReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAuctioneerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAuctioneerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankAccountHolderPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBankAccountHolderPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankChargeBearerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBankChargeBearerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBankPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBidderPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBidderPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBillFromPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBillFromPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBillingProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBillingProfileReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBillToPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBillToPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBuyerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBuyerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSuggestedBuyerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSuggestedBuyerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCarrierPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCarrierPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditRatingPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCreditRatingPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCustomerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerPartyAccountReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCustomerPartyAccountReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerAgentPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCustomerAgentPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerServiceRepresentativePersonPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCustomerServiceRepresentativePersonPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDeliverToPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomDeliverToPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDriverPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomDriverPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEmployeePartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomEmployeePartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEmployerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomEmployerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMandateSignerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomMandateSignerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomManufacturerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomManufacturerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMediatorPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomMediatorPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOwnerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomOwnerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOutsourcerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomOutsourcerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomVendorPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomVendorPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayeePartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPayeePartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayFromPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPayFromPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPOSupplierPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPOSupplierPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPublisherPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPublisherPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomReceivingPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomReceivingPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRemitToPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRemitToPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomResponsiblePartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomResponsiblePartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequesterPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRequesterPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequiredByPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRequiredByPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipFromPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomShipFromPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipToPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomShipToPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSoldToPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSoldToPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSubscriberPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSubscriberPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSupplierPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSupplierPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomParentSupplierPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomParentSupplierPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSuggestedSupplierPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSuggestedSupplierPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTradingPartnerPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTradingPartnerPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerPartyContactReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCustomerPartyContactReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDocumentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomDocumentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDocumentLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomDocumentLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSourceDocumentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSourceDocumentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAdvanceShipmentNoticeReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAdvanceShipmentNoticeReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBillOfLadingReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBillOfLadingReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBillOfMaterialsReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBillOfMaterialsReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCommonBillOfMaterialsReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCommonBillOfMaterialsReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomModelBillOfMaterialsReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomModelBillOfMaterialsReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContractReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomContractReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContractLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomContractLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchasingContractReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPurchasingContractReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceContractLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomServiceContractLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDepartmentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomDepartmentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInvoiceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomInvoiceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomExternalInvoiceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomExternalInvoiceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEmploymentGradeReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomEmploymentGradeReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEmploymentAssignmentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomEmploymentAssignmentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomJobReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomJobReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayableInvoiceLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPayableInvoiceLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomExternalInvoiceLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomExternalInvoiceLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayableInvoiceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPayableInvoiceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPositionReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPositionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPurchaseOrderReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShippingProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomShippingProfileReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriceListReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPriceListReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerPurchaseOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCustomerPurchaseOrderReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSalesOrderReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProvisioningOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProvisioningOrderReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFulfillmentOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomFulfillmentOrderReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTransportationSalesOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTransportationSalesOrderReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemPublicationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemPublicationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriceFormulaReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPriceFormulaReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInvoiceLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomInvoiceLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriceListLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPriceListLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPurchaseOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseOrderLineScheduleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPurchaseOrderLineScheduleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerPurchaseOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCustomerPurchaseOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentReceiptReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPaymentReceiptReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerPurchaseOrderLineScheduleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCustomerPurchaseOrderLineScheduleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProjectTaskReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProjectTaskReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSalesOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProvisioningOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProvisioningOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFulfillmentOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomFulfillmentOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTransportationSalesOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTransportationSalesOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesOrderLineScheduleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSalesOrderLineScheduleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemPublicationLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemPublicationLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankAccountReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBankAccountReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankBranchReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBankBranchReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemCatalogReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemCatalogReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomClaimReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomClaimReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditMemoReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCreditMemoReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDirectDebitMandateReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomDirectDebitMandateReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFundReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomFundReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInstalledProductReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomInstalledProductReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemInstanceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemInstanceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemStructureReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemStructureReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLegalEntityReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomLegalEntityReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLocationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomLocationReferenceTypeV1', {
        'ValidatedFlag': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'AddressLinesPhonetic': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'SalesTaxInsideCtyLimits': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LocationPartyID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'SaoRoomCode': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'OrigSystemReference': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_OrigSystemReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOfferReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomOfferReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPaymentProfileReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProjectReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProjectReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPromotionReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPromotionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRMAReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRMAReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSpecificationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSpecificationGroupReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationValueSetReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSpecificationValueSetReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceRequestReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomServiceRequestReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRelatedServiceRequestReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRelatedServiceRequestReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSupportTeamReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSupportTeamReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSettlementReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSettlementReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomChartOfAccountsStructureReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomChartOfAccountsStructureReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLedgerReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomLedgerReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBudgetReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBudgetReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAccountingPeriodReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAccountingPeriodReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLatestAccountingPeriodReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomLatestAccountingPeriodReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBusinessCalendarReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBusinessCalendarReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesTerritoryReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSalesTerritoryReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWorkerReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomWorkerReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemLotReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemLotReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPersonReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemFormulaReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemFormulaReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOperationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomOperationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomActivityReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomActivityReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRecipeReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRecipeReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRecipeValidityRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRecipeValidityRuleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProductionOrderMaterialReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProductionOrderMaterialReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemFormulaMaterialReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemFormulaMaterialReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomManufacturingRoutingOperationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomManufacturingRoutingOperationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomManufacturingRoutingActivityReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomManufacturingRoutingActivityReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomManufacturingRoutingReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomManufacturingRoutingReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProductionOrderResourceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProductionOrderResourceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBatchProductionOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBatchProductionOrderReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProductionOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProductionOrderReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProductionOrderOperationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProductionOrderOperationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProductionOrderActivityReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProductionOrderActivityReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomObjectReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomObjectReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileTypeReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTalentProfileTypeReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileContentTypeReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTalentProfileContentTypeReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileContentItemReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTalentProfileContentItemReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPerformanceReviewRatingModelReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPerformanceReviewRatingModelReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileInstanceQualifierReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTalentProfileInstanceQualifierReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPerformanceReviewRatingReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPerformanceReviewRatingReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileContentItemCatalogReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTalentProfileContentItemCatalogReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTalentProfileReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileContentTypePropertyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTalentProfileContentTypePropertyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentRequestOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentRequestOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSupplierPartyTradingLocationProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSupplierPartyTradingLocationProfileReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProjectSchedulableResourceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProjectSchedulableResourceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomResourceAvailabilityCalendarReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomResourceAvailabilityCalendarReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTalentProfileInstanceQualifierSetReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTalentProfileInstanceQualifierSetReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInvoicingRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomInvoicingRuleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAccountingRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAccountingRuleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSignatoryGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSignatoryGroupReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMarketingEventReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomMarketingEventReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCompetitorPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCompetitorPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAccountingEntryReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAccountingEntryReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAdjusterPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAdjusterPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomParticipatingPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomParticipatingPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomChartOfAccountsReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomChartOfAccountsReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAccountBalanceAdjustmentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAccountBalanceAdjustmentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCalendarReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCalendarReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomResourceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomResourceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayeePartyAccountReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPayeePartyAccountReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomOrganizationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWorkOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomWorkOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemATPRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemATPRuleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemPickingRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemPickingRuleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomClassificationSpecificationGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomClassificationSpecificationGroupReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSpecificationValueSetLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSpecificationValueSetLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAttributeBasedPricingMatrixReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAttributeBasedPricingMatrixReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalaryPlanReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSalaryPlanReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomClassificationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomProjectNonSchedulableResourceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomProjectNonSchedulableResourceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTeamReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTeamReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEstablishmentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomEstablishmentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomReportingPeriodReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomReportingPeriodReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBusinessUnitFunctionReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBusinessUnitFunctionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInventoryTransactionReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomInventoryTransactionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomIncentiveCompensationPlanComponentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomIncentiveCompensationPlanComponentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWorkerUnionReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomWorkerUnionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomValueSetReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomValueSetReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomVolumeDiscountPlanReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomVolumeDiscountPlanReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRegionReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRegionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBargainingUnitReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBargainingUnitReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCompensationPackageTemplateReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCompensationPackageTemplateReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAssignmentGradeReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAssignmentGradeReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAssignmentGradeStepReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAssignmentGradeStepReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPositionPoolReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPositionPoolReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCompensationPackageRuleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCompensationPackageRuleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomJobFamilyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomJobFamilyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCareerPathReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCareerPathReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceCreditCalculationGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomServiceCreditCalculationGroupReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTrainingProgramReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomTrainingProgramReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomGovernmentAgencyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomGovernmentAgencyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLaborAgreementReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomLaborAgreementReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayEquityJobClassReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPayEquityJobClassReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomINAILRiskProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomINAILRiskProfileReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFestivalAdvancePayProgramReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomFestivalAdvancePayProgramReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAcademicRankReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomAcademicRankReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWorkersCompensationBoardRateGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomWorkersCompensationBoardRateGroupReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalaryIncreaseMatrixReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSalaryIncreaseMatrixReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLegislativeDataGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomLegislativeDataGroupReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLaborAgreementFirstLevelEmployeeClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomLaborAgreementFirstLevelEmployeeClassificationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLaborAgreementSecondLevelEmployeeClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomLaborAgreementSecondLevelEmployeeClassificationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLaborAgreementThirdLevelEmployeeClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomLaborAgreementThirdLevelEmployeeClassificationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPositionStandardClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPositionStandardClassificationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWorkersCompensationBoardRateGroupClassificationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomWorkersCompensationBoardRateGroupClassificationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialAccountReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomFinancialAccountReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMarketingOfferReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomMarketingOfferReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMarketingTreatmentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomMarketingTreatmentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceContractCoverageTemplateReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomServiceContractCoverageTemplateReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceContractSubscriptionTemplateReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomServiceContractSubscriptionTemplateReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomApplicationAreaTypeV1':
      return flaskRestPlusAPI.model('CustomApplicationAreaTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEBMReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomEBMReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDocumentInformationTypeV1':
      return flaskRestPlusAPI.model('CustomDocumentInformationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequestTypeV1':
      return flaskRestPlusAPI.model('CustomRequestTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomResponseTypeV1':
      return flaskRestPlusAPI.model('CustomResponseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomQueryTypeV1':
      return flaskRestPlusAPI.model('CustomQueryTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreateTypeV1':
      return flaskRestPlusAPI.model('CustomCreateTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaidInvoiceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPaidInvoiceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFreightInvoiceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomFreightInvoiceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditCardTypeV1':
      return flaskRestPlusAPI.model('CustomCreditCardTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDebitCardTypeV1':
      return flaskRestPlusAPI.model('CustomDebitCardTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomItemIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerItemIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomCustomerItemIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomManufacturerItemIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomManufacturerItemIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSupplierItemIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomSupplierItemIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomInvoiceIdentificationTypeV1':
      return flaskRestPlusAPI.model('CustomInvoiceIdentificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankPaymentAuthorizationReferenceTypeTypeV1':
      return flaskRestPlusAPI.model('CustomBankPaymentAuthorizationReferenceTypeTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditChargeAuthorizationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCreditChargeAuthorizationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDebitChargeAuthorizationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomDebitChargeAuthorizationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContainerReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomContainerReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentPlanUnitTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentPlanUnitTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentUnitChargeTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentUnitChargeTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentContainerTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentContainerTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentContainerChargeTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentContainerChargeTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentContainerItemTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentContainerItemTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEducationalInstitutionReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomEducationalInstitutionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialInstitutionReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomFinancialInstitutionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPrimarySalespersonPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPrimarySalespersonPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBeneficiaryPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBeneficiaryPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBillOfMaterialsComponentItemReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBillOfMaterialsComponentItemReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEngineeringChangeOrderReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomEngineeringChangeOrderReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEngineeringChangeOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomEngineeringChangeOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPricingAgreementReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPricingAgreementReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseAgreementReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPurchaseAgreementReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseAgreementPriceBreakReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPurchaseAgreementPriceBreakReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomQuoteReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomQuoteReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomQuoteLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomQuoteLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomQuotePriceQualificationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomQuotePriceQualificationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequestForQuoteReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRequestForQuoteReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequestForQuoteLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRequestForQuoteLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequestForQuotePriceBreakReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRequestForQuotePriceBreakReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequisitionReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRequisitionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequisitionLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRequisitionLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRequisitionDistributionReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRequisitionDistributionReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesOrderScheduleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSalesOrderScheduleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesOpportunityReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSalesOpportunityReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBusinessUnitReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBusinessUnitReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomConfigurationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomConfigurationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemStructureComponentItemReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomItemStructureComponentItemReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayeeLegalEntityReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPayeeLegalEntityReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPaymentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPaymentLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDisbursedPaymentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomDisbursedPaymentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentItemReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomVehicleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomVehicleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWIPEntityReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomWIPEntityReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWIPEntityLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomWIPEntityLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWIPOperationReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomWIPOperationReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomWIPOperationResourceReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomWIPOperationResourceReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSalesPersonPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomSalesPersonPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemStructureTypeV1':
      return flaskRestPlusAPI.model('CustomItemStructureTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomComponentItemTypeV1':
      return flaskRestPlusAPI.model('CustomComponentItemTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomComponentItemSpecificationGroupTypeV1':
      return flaskRestPlusAPI.model('CustomComponentItemSpecificationGroupTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemStructureAttachmentTypeV1':
      return flaskRestPlusAPI.model('CustomItemStructureAttachmentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemStructureSpecificationGroupTypeV1':
      return flaskRestPlusAPI.model('CustomItemStructureSpecificationGroupTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSubstituteComponentItemTypeV1':
      return flaskRestPlusAPI.model('CustomSubstituteComponentItemTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSubstituteComponentItemSpecificationGroupTypeV1':
      return flaskRestPlusAPI.model('CustomSubstituteComponentItemSpecificationGroupTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFreightInvoiceLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomFreightInvoiceLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchaseOrderShipmentReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPurchaseOrderShipmentReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationCertificationTypeV1':
      return flaskRestPlusAPI.model('CustomOrganizationCertificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationCreditRatingTypeV1':
      return flaskRestPlusAPI.model('CustomOrganizationCreditRatingTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationFinancialProfileTypeV1':
      return flaskRestPlusAPI.model('CustomOrganizationFinancialProfileTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationFinancialStatementTypeV1':
      return flaskRestPlusAPI.model('CustomOrganizationFinancialStatementTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTotalEmploymentTypeV1':
      return flaskRestPlusAPI.model('CustomTotalEmploymentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEmploymentStatisticsTypeV1':
      return flaskRestPlusAPI.model('CustomEmploymentStatisticsTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPrimaryAddressEmploymentDetailTypeV1':
      return flaskRestPlusAPI.model('CustomPrimaryAddressEmploymentDetailTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCommercialCreditScoreTypeV1':
      return flaskRestPlusAPI.model('CustomCommercialCreditScoreTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditScoreCommentaryTypeV1':
      return flaskRestPlusAPI.model('CustomCreditScoreCommentaryTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEstimatedDelinquentPaymentIncidenceTypeV1':
      return flaskRestPlusAPI.model('CustomEstimatedDelinquentPaymentIncidenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFailureRiskTypeV1':
      return flaskRestPlusAPI.model('CustomFailureRiskTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomParentBankruptcyTypeV1':
      return flaskRestPlusAPI.model('CustomParentBankruptcyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaydexTypeV1':
      return flaskRestPlusAPI.model('CustomPaydexTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaydexNormTypeV1':
      return flaskRestPlusAPI.model('CustomPaydexNormTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationFinancialNumberTypeV1':
      return flaskRestPlusAPI.model('CustomOrganizationFinancialNumberTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCitizenshipTypeV1':
      return flaskRestPlusAPI.model('CustomCitizenshipTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEducationRecordTypeV1':
      return flaskRestPlusAPI.model('CustomEducationRecordTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEmploymentRecordTypeV1':
      return flaskRestPlusAPI.model('CustomEmploymentRecordTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonInterestTypeV1':
      return flaskRestPlusAPI.model('CustomPersonInterestTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLanguageProficiencyTypeV1':
      return flaskRestPlusAPI.model('CustomLanguageProficiencyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonCertificationTypeV1':
      return flaskRestPlusAPI.model('CustomPersonCertificationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonFinancialProfileTypeV1':
      return flaskRestPlusAPI.model('CustomPersonFinancialProfileTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMilitaryEmploymentTypeV1':
      return flaskRestPlusAPI.model('CustomMilitaryEmploymentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomGLAccountTypeV1':
      return flaskRestPlusAPI.model('CustomGLAccountTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPurchasingContractLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPurchasingContractLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBlanketPurchaseAgreementReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBlanketPurchaseAgreementReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomLocationParentTypeV1':
      return flaskRestPlusAPI.model('CustomLocationParentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentChargeTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentChargeTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentItemTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemChargeTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentItemChargeTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyLocationTypeV1':
      return flaskRestPlusAPI.model('CustomPartyLocationTypeV1', {
        'PartySite': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_PartySiteV1')),
        'PartySiteUse': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_PartySiteUseV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankPaymentAuthorizationTypeV1':
      return flaskRestPlusAPI.model('CustomBankPaymentAuthorizationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentDebitCommunicationTypeV1':
      return flaskRestPlusAPI.model('CustomPaymentDebitCommunicationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentDirectDebitMandateTypeV1':
      return flaskRestPlusAPI.model('CustomPaymentDirectDebitMandateTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentRemittanceCommunicationTypeV1':
      return flaskRestPlusAPI.model('CustomPaymentRemittanceCommunicationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditChargeAuthorizationTypeV1':
      return flaskRestPlusAPI.model('CustomCreditChargeAuthorizationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCreditChargeAuthorizationResponseTypeV1':
      return flaskRestPlusAPI.model('CustomCreditChargeAuthorizationResponseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDebitChargeAuthorizationTypeV1':
      return flaskRestPlusAPI.model('CustomDebitChargeAuthorizationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDebitChargeAuthorizationResponseTypeV1':
      return flaskRestPlusAPI.model('CustomDebitChargeAuthorizationResponseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentRegulatoryReportTypeV1':
      return flaskRestPlusAPI.model('CustomPaymentRegulatoryReportTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomOrganizationTypeV1':
      return flaskRestPlusAPI.model('CustomOrganizationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonTypeV1':
      return flaskRestPlusAPI.model('CustomPersonTypeV1', {
        'PersonType': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_PersonTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCheckTypeV1':
      return flaskRestPlusAPI.model('CustomCheckTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEFTTypeV1':
      return flaskRestPlusAPI.model('CustomEFTTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankDraftTypeV1':
      return flaskRestPlusAPI.model('CustomBankDraftTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBankPaymentTypeV1':
      return flaskRestPlusAPI.model('CustomBankPaymentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentSetTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentSetTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomActivityTypeV1':
      return flaskRestPlusAPI.model('CustomActivityTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemInstanceRangeTypeV1':
      return flaskRestPlusAPI.model('CustomItemInstanceRangeTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomVisaTypeV1':
      return flaskRestPlusAPI.model('CustomVisaTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPassportTypeV1':
      return flaskRestPlusAPI.model('CustomPassportTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDriversLicenseClassTypeV1':
      return flaskRestPlusAPI.model('CustomDriversLicenseClassTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonDriversLicenseTypeV1':
      return flaskRestPlusAPI.model('CustomPersonDriversLicenseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonNationalIdentityTypeV1':
      return flaskRestPlusAPI.model('CustomPersonNationalIdentityTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonAffiliationTypeV1':
      return flaskRestPlusAPI.model('CustomPersonAffiliationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemLotTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentItemLotTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemInstanceRangeTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentItemInstanceRangeTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemInstanceTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentItemInstanceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:ShipmentItemInstanceGenealogyTypeV1':
      return flaskRestPlusAPI.model('ShipmentItemInstanceGenealogyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemInstanceGenealogyCompositionTypeV1':
      return flaskRestPlusAPI.model('CustomItemInstanceGenealogyCompositionTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialAccountBalanceTypeV1':
      return flaskRestPlusAPI.model('CustomFinancialAccountBalanceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialAccountPersonHolderTypeV1':
      return flaskRestPlusAPI.model('CustomFinancialAccountPersonHolderTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialAccountOrganizationHolderTypeV1':
      return flaskRestPlusAPI.model('CustomFinancialAccountOrganizationHolderTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomFinancialAccountHolderTypeV1':
      return flaskRestPlusAPI.model('CustomFinancialAccountHolderTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyRelatedPartyTypeV1':
      return flaskRestPlusAPI.model('CustomPartyRelatedPartyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyRelationshipTypeV1':
      return flaskRestPlusAPI.model('CustomPartyRelationshipTypeV1', {
        'RelationshipID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ParentObjectType': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'RelatedObjectType': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'RelationshipType': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ParentObjectID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'RelatedObjectID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'RoleType': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'PrimaryFlag': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'RelationshipStatus': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyRelatedPersonPartyTypeV1':
      return flaskRestPlusAPI.model('CustomPartyRelatedPersonPartyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyRelatedOrganizationPartyTypeV1':
      return flaskRestPlusAPI.model('CustomPartyRelatedOrganizationPartyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyRelatedHouseholdPartyTypeV1':
      return flaskRestPlusAPI.model('CustomPartyRelatedHouseholdPartyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBeneficiaryTypeV1':
      return flaskRestPlusAPI.model('CustomBeneficiaryTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBeneficiaryOrganizationPartyTypeV1':
      return flaskRestPlusAPI.model('CustomBeneficiaryOrganizationPartyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBeneficiaryPersonPartyTypeV1':
      return flaskRestPlusAPI.model('CustomBeneficiaryPersonPartyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayerOrganizationPartyTypeV1':
      return flaskRestPlusAPI.model('CustomPayerOrganizationPartyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayerPersonPartyTypeV1':
      return flaskRestPlusAPI.model('CustomPayerPersonPartyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPayerTypeV1':
      return flaskRestPlusAPI.model('CustomPayerTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDependentPersonPartyTypeV1':
      return flaskRestPlusAPI.model('CustomDependentPersonPartyTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDependentTypeV1':
      return flaskRestPlusAPI.model('CustomDependentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPaymentTermTypeV1':
      return flaskRestPlusAPI.model('CustomPaymentTermTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPlanTypeV1':
      return flaskRestPlusAPI.model('CustomPlanTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriceTypeV1':
      return flaskRestPlusAPI.model('CustomPriceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomCustomerPartyBillingProfileReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomCustomerPartyBillingProfileReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBalanceGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBalanceGroupReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomItemInstanceTypeV1':
      return flaskRestPlusAPI.model('CustomItemInstanceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomChargeParentLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomChargeParentLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriorMarketingBundleSalesOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPriorMarketingBundleSalesOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMarketingBundleSalesOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomMarketingBundleSalesOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriorMarketingBundleProvisioningOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPriorMarketingBundleProvisioningOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMarketingBundleProvisioningOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomMarketingBundleProvisioningOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriorMarketingBundleFulfillmentOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPriorMarketingBundleFulfillmentOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMarketingBundleFulfillmentOrderLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomMarketingBundleFulfillmentOrderLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomParentInvoiceLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomParentInvoiceLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomParentServiceUsageLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomParentServiceUsageLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomServiceUsageLineReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomServiceUsageLineReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBalanceSummaryReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomBalanceSummaryReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomUsageAllocationResourceBaseTypeV1':
      return flaskRestPlusAPI.model('CustomUsageAllocationResourceBaseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPriorPayFromPartyReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomPriorPayFromPartyReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDocumentGroupReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomDocumentGroupReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomRelatedTroubleTicketReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomRelatedTroubleTicketReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAppointmentWindowTypeV1':
      return flaskRestPlusAPI.model('CustomAppointmentWindowTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonNameUsageTypeV1':
      return flaskRestPlusAPI.model('CustomPersonNameUsageTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSWOTAnalysisTypeV1':
      return flaskRestPlusAPI.model('CustomSWOTAnalysisTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPersonProfessionalLicenseTypeV1':
      return flaskRestPlusAPI.model('CustomPersonProfessionalLicenseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentFulfillmentOrderScheduleTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentFulfillmentOrderScheduleTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentAttachmentTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentAttachmentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomShipmentItemAttachmentTypeV1':
      return flaskRestPlusAPI.model('CustomShipmentItemAttachmentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_PersonTypeV1':
      return flaskRestPlusAPI.model('IC_PersonTypeV1', {
        'PersonTypeCode': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'EffectiveTimePeriod': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TimePeriodTypeLOWERV1')),
        'DeleteFlag': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_PartySiteV1':
      return flaskRestPlusAPI.model('IC_PartySiteV1', {
        'PartySiteID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'IdentifyingAddressFlag': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Status': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'PartySiteName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Addressee': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ParentObjectID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'PartyLocationContact': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyContactTypeLOWERV1')),
        'OrigSystemReference': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_OrigSystemReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_PartySiteUseV1':
      return flaskRestPlusAPI.model('IC_PartySiteUseV1', {
        'PartySiteUseIdentification': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LocationIdentificationTypeLOWERV1'))),
        'PartySiteID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Status': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'SiteUseType': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'PrimaryPerType': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomDocumentScheduleReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomDocumentScheduleReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EBMTypeV1':
      return flaskRestPlusAPI.model('EBMTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EBMHeaderTypeV1':
      return flaskRestPlusAPI.model('EBMHeaderTypeV1', {
        'EBMID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'EBMName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'EBOName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element CreationDateTime has a type that is not catered for (DateTimeType) 0
        'RequestEBMID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'VerbCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEBMHeaderTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ApplicationTypeV1':
      return flaskRestPlusAPI.model('ApplicationTypeV1', {
        'ID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element Version has a type that is not catered for (StringType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MessageProcessingInstructionTypeV1':
      return flaskRestPlusAPI.model('MessageProcessingInstructionTypeV1', {
        'EnvironmentCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'DefinitionID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'InstanceID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMessageProcessingInstructionTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ObjectCrossReferenceTypeV1':
      return flaskRestPlusAPI.model('ObjectCrossReferenceTypeV1', {
        #Element  has a type that is not catered for () 0
        'EBOID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SenderTypeV1':
      return flaskRestPlusAPI.model('SenderTypeV1', {
        'ID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element IPAddress has a type that is not catered for (URIType) 0
        'SenderMessageID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'TransactionCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'CallingServiceName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element  has a type that is not catered for () 0
        'ContactName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element ContactEmail has a type that is not catered for (URIType) 0
        #Element ContactPhoneNumber has a type that is not catered for (StringType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSenderTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WSAddressTypeV1':
      return flaskRestPlusAPI.model('WSAddressTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IntermediateMessageHopTypeV1':
      return flaskRestPlusAPI.model('IntermediateMessageHopTypeV1', {
        'SenderResourceTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'SenderResourceID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'SenderMessageID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomIntermediateMessageHopTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EBMTrackingTypeV1':
      return flaskRestPlusAPI.model('EBMTrackingTypeV1', {
        #Element SequenceNumber has a type that is not catered for (NumericType) 0
        'ExecutionUnitID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'ExecutionUnitName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        #Element ImplementationCode has a type that is not catered for (ImplementationCodeType) 0
        #Element ActivityDateTime has a type that is not catered for (DateTimeType) 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEBMTrackingTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TargetTypeV1':
      return flaskRestPlusAPI.model('TargetTypeV1', {
        'ID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element OverrideRoutingIndicator has a type that is not catered for (IndicatorType) 0
        'ServiceName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'ApplicationTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element EndPointURI has a type that is not catered for (URIType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTargetTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BusinessScopeTypeV1':
      return flaskRestPlusAPI.model('BusinessScopeTypeV1', {
        'ID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'InstanceID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'BusinessScopeTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'EnterpriseServiceName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'EnterpriseServiceOperationName': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBusinessScopeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ESBHeaderExtensionTypeV1':
      return flaskRestPlusAPI.model('ESBHeaderExtensionTypeV1', {
        'Name': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'DataTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element Value has a type that is not catered for (StringType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreateTypeV1':
      return flaskRestPlusAPI.model('CreateTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CreateResponseTypeV1':
      return flaskRestPlusAPI.model('CreateResponseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DeleteTypeV1':
      return flaskRestPlusAPI.model('DeleteTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:DeleteResponseTypeV1':
      return flaskRestPlusAPI.model('DeleteResponseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProcessTypeV1':
      return flaskRestPlusAPI.model('ProcessTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ProcessResponseTypeV1':
      return flaskRestPlusAPI.model('ProcessResponseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ComplexQueryTypeV1':
      return flaskRestPlusAPI.model('ComplexQueryTypeV1', {
        'QueryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ResponseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QueryCriteriaTypeV1':
      return flaskRestPlusAPI.model('QueryCriteriaTypeV1', {
        #Element QualifiedElementPath has a type that is not catered for (StringType) 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ValueExpressionTypeV1':
      return flaskRestPlusAPI.model('ValueExpressionTypeV1', {
        #Element ElementPath has a type that is not catered for (StringType) 0
        #Element Value has a type that is not catered for (StringType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ResponseFilterTypeV1':
      return flaskRestPlusAPI.model('ResponseFilterTypeV1', {
        #Element QualifiedElementPath has a type that is not catered for (StringType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SortCriteriaTypeV1':
      return flaskRestPlusAPI.model('SortCriteriaTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SortElementTypeV1':
      return flaskRestPlusAPI.model('SortElementTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QueryExpressionTypeV1':
      return flaskRestPlusAPI.model('QueryExpressionTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QueryResponseTypeV1':
      return flaskRestPlusAPI.model('QueryResponseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SimpleQueryTypeV1':
      return flaskRestPlusAPI.model('SimpleQueryTypeV1', {
        'QueryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ResponseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:UpdateTypeV1':
      return flaskRestPlusAPI.model('UpdateTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:UpdateResponseTypeV1':
      return flaskRestPlusAPI.model('UpdateResponseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SyncTypeV1':
      return flaskRestPlusAPI.model('SyncTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SyncResponseTypeV1':
      return flaskRestPlusAPI.model('SyncResponseTypeV1', {
        'StatusCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ResponseMessage': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ValidateTypeV1':
      return flaskRestPlusAPI.model('ValidateTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ValidateResponseTypeV1':
      return flaskRestPlusAPI.model('ValidateResponseTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FaultTypeV1':
      return flaskRestPlusAPI.model('FaultTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FaultNotificationTypeV1':
      return flaskRestPlusAPI.model('FaultNotificationTypeV1', {
        'BusinessComponentID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element ReportingDateTime has a type that is not catered for (DateTimeType) 0
        'CorrectiveAction': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FaultMessageTypeV1':
      return flaskRestPlusAPI.model('FaultMessageTypeV1', {
        'Code': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Text': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Severity': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Stack': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element ApplicationFaultData has a type that is not catered for (xsd:anyType) 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FaultingServiceTypeV1':
      return flaskRestPlusAPI.model('FaultingServiceTypeV1', {
        'ID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element ImplementationCode has a type that is not catered for (ImplementationCodeType) 0
        'InstanceID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'ExecutionContextID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SenderReferenceTypeV1':
      return flaskRestPlusAPI.model('SenderReferenceTypeV1', {
        'ID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'SenderMessageID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'TransactionCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BusinessScopeReferenceTypeV1':
      return flaskRestPlusAPI.model('BusinessScopeReferenceTypeV1', {
        'ID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'InstanceID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'EnterpriseServiceName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'EnterpriseServiceOperationName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EBMReferenceTypeV1':
      return flaskRestPlusAPI.model('EBMReferenceTypeV1', {
        'EBMID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'EBMName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'EBOName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'VerbCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'BusinessComponentID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'ID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'ContextID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeIdentificationTypeV1':
      return flaskRestPlusAPI.model('CodeIdentificationTypeV1', {
        'BusinessComponentID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Code': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ContextID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1'))),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ObjectKeyTypeV1':
      return flaskRestPlusAPI.model('ObjectKeyTypeV1', {
        'ID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'ContextID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RevisionTypeV1':
      return flaskRestPlusAPI.model('RevisionTypeV1', {
        'Number': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Code': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element EffectiveDate has a type that is not catered for (DateType) 0
        #Element EffectiveEndDate has a type that is not catered for (DateType) 0
        'Label': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Reason': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BatchParameterTypeV1':
      return flaskRestPlusAPI.model('BatchParameterTypeV1', {
        'Name': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1')),
        'DataTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element Value has a type that is not catered for (StringType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MessageBatchTypeV1':
      return flaskRestPlusAPI.model('MessageBatchTypeV1', {
        'ID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'Name': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1')),
        'StatusCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ResponseMessage': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1')),
        #Element  has a type that is not catered for () 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:B2BDocumentTypeTypeV1':
      return flaskRestPlusAPI.model('B2BDocumentTypeTypeV1', {
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element Version has a type that is not catered for (StringType) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomB2BDocumentTypeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:B2BMHeaderTypeV1':
      return flaskRestPlusAPI.model('B2BMHeaderTypeV1', {
        'B2BMID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'CollaborationID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'ReplyToMessageID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'GatewayID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomB2BMHeaderTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:B2BMReferenceTypeV1':
      return flaskRestPlusAPI.model('B2BMReferenceTypeV1', {
        'B2BMID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'CollaborationID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'ReplyToMessageID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element  has a type that is not catered for () 0
        'GatewayID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomB2BMReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:B2BMTypeV1':
      return flaskRestPlusAPI.model('B2BMTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element Payload has a type that is not catered for (xsd:anyType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:B2BProfileTypeV1':
      return flaskRestPlusAPI.model('B2BProfileTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomB2BProfileTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SenderTradingPartnerTypeV1':
      return flaskRestPlusAPI.model('SenderTradingPartnerTypeV1', {
        'TradingPartnerID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSenderTradingPartnerTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ReceiverTradingPartnerTypeV1':
      return flaskRestPlusAPI.model('ReceiverTradingPartnerTypeV1', {
        'TradingPartnerID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1'))),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomReceiverTradingPartnerTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEBMHeaderTypeV1':
      return flaskRestPlusAPI.model('CustomEBMHeaderTypeV1', {
        #Element PhaseID has a type that is not catered for (corecom:StringType) 0
        #Element ResponseTimeout has a type that is not catered for (corecom:StringType) 0
        #Element ChangeOrigin has a type that is not catered for (corecom:StringType) 0
        #Element BatchID has a type that is not catered for (corecom:StringType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomMessageProcessingInstructionTypeV1':
      return flaskRestPlusAPI.model('CustomMessageProcessingInstructionTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSenderTypeV1':
      return flaskRestPlusAPI.model('CustomSenderTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomEBMTrackingTypeV1':
      return flaskRestPlusAPI.model('CustomEBMTrackingTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomTargetTypeV1':
      return flaskRestPlusAPI.model('CustomTargetTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomBusinessScopeTypeV1':
      return flaskRestPlusAPI.model('CustomBusinessScopeTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomIntermediateMessageHopTypeV1':
      return flaskRestPlusAPI.model('CustomIntermediateMessageHopTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomB2BProfileTypeV1':
      return flaskRestPlusAPI.model('CustomB2BProfileTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSenderTradingPartnerTypeV1':
      return flaskRestPlusAPI.model('CustomSenderTradingPartnerTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomReceiverTradingPartnerTypeV1':
      return flaskRestPlusAPI.model('CustomReceiverTradingPartnerTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomB2BMHeaderTypeV1':
      return flaskRestPlusAPI.model('CustomB2BMHeaderTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomB2BDocumentTypeTypeV1':
      return flaskRestPlusAPI.model('CustomB2BDocumentTypeTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomB2BMReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomB2BMReferenceTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AmountTypeV1':
      return flaskRestPlusAPI.model('AmountTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:BinaryObjectTypeV1':
      return flaskRestPlusAPI.model('BinaryObjectTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1':
      return flaskRestPlusAPI.model('CodeTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1':
      return flaskRestPlusAPI.model('IdentifierTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:MeasureTypeV1':
      return flaskRestPlusAPI.model('MeasureTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1':
      return flaskRestPlusAPI.model('NameTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:QuantityTypeV1':
      return flaskRestPlusAPI.model('QuantityTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:RateTypeV1':
      return flaskRestPlusAPI.model('RateTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1':
      return flaskRestPlusAPI.model('TextTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AnyDateTimePointTypeV1':
      return flaskRestPlusAPI.model('AnyDateTimePointTypeV1', {

      })
    if typeName=='http://schemas.xmlsoap.org/ws/2003/03/addressing:EndpointReferenceTypeV1':
      return flaskRestPlusAPI.model('EndpointReferenceTypeV1', {
        'Address': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://schemas.xmlsoap.org/ws/2003/03/addressing:AttributedURIV1')),
        'ReferenceProperties': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://schemas.xmlsoap.org/ws/2003/03/addressing:ReferencePropertiesTypeV1')),
        'PortType': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://schemas.xmlsoap.org/ws/2003/03/addressing:AttributedQNameV1')),
        'ServiceName': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://schemas.xmlsoap.org/ws/2003/03/addressing:ServiceNameTypeV1')),

      })
    if typeName=='http://schemas.xmlsoap.org/ws/2003/03/addressing:ReferencePropertiesTypeV1':
      return flaskRestPlusAPI.model('ReferencePropertiesTypeV1', {

      })
    if typeName=='http://schemas.xmlsoap.org/ws/2003/03/addressing:ServiceNameTypeV1':
      return flaskRestPlusAPI.model('ServiceNameTypeV1', {

      })
    if typeName=='http://schemas.xmlsoap.org/ws/2003/03/addressing:RelationshipV1':
      return flaskRestPlusAPI.model('RelationshipV1', {

      })
    if typeName=='http://schemas.xmlsoap.org/ws/2003/03/addressing:AttributedQNameV1':
      return flaskRestPlusAPI.model('AttributedQNameV1', {

      })
    if typeName=='http://schemas.xmlsoap.org/ws/2003/03/addressing:AttributedURIV1':
      return flaskRestPlusAPI.model('AttributedURIV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:RequestTypeV1':
      return flaskRestPlusAPI.model('RequestTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:ResponseTypeV1':
      return flaskRestPlusAPI.model('ResponseTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:SubjectTypeV1':
      return flaskRestPlusAPI.model('SubjectTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:ResourceTypeV1':
      return flaskRestPlusAPI.model('ResourceTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:ResourceContentTypeV1':
      return flaskRestPlusAPI.model('ResourceContentTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:ActionTypeV1':
      return flaskRestPlusAPI.model('ActionTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:EnvironmentTypeV1':
      return flaskRestPlusAPI.model('EnvironmentTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:AttributeTypeV1':
      return flaskRestPlusAPI.model('AttributeTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:AttributeValueTypeV1':
      return flaskRestPlusAPI.model('AttributeValueTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:ResultTypeV1':
      return flaskRestPlusAPI.model('ResultTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:StatusTypeV1':
      return flaskRestPlusAPI.model('StatusTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:StatusCodeTypeV1':
      return flaskRestPlusAPI.model('StatusCodeTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:StatusDetailTypeV1':
      return flaskRestPlusAPI.model('StatusDetailTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:context:schema:cd:04:MissingAttributeDetailTypeV1':
      return flaskRestPlusAPI.model('MissingAttributeDetailTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:PolicySetTypeV1':
      return flaskRestPlusAPI.model('PolicySetTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:CombinerParametersTypeV1':
      return flaskRestPlusAPI.model('CombinerParametersTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:CombinerParameterTypeV1':
      return flaskRestPlusAPI.model('CombinerParameterTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:RuleCombinerParametersTypeV1':
      return flaskRestPlusAPI.model('RuleCombinerParametersTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:PolicyCombinerParametersTypeV1':
      return flaskRestPlusAPI.model('PolicyCombinerParametersTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:PolicySetCombinerParametersTypeV1':
      return flaskRestPlusAPI.model('PolicySetCombinerParametersTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:DefaultsTypeV1':
      return flaskRestPlusAPI.model('DefaultsTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:IdReferenceTypeV1':
      return flaskRestPlusAPI.model('IdReferenceTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:PolicyTypeV1':
      return flaskRestPlusAPI.model('PolicyTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:RuleTypeV1':
      return flaskRestPlusAPI.model('RuleTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:TargetTypeV1':
      return flaskRestPlusAPI.model('TargetTypeV1', {
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:SubjectsTypeV1':
      return flaskRestPlusAPI.model('SubjectsTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:SubjectTypeV1':
      return flaskRestPlusAPI.model('SubjectTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ResourcesTypeV1':
      return flaskRestPlusAPI.model('ResourcesTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ResourceTypeV1':
      return flaskRestPlusAPI.model('ResourceTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ActionsTypeV1':
      return flaskRestPlusAPI.model('ActionsTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ActionTypeV1':
      return flaskRestPlusAPI.model('ActionTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:EnvironmentsTypeV1':
      return flaskRestPlusAPI.model('EnvironmentsTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:EnvironmentTypeV1':
      return flaskRestPlusAPI.model('EnvironmentTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:SubjectMatchTypeV1':
      return flaskRestPlusAPI.model('SubjectMatchTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ResourceMatchTypeV1':
      return flaskRestPlusAPI.model('ResourceMatchTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ActionMatchTypeV1':
      return flaskRestPlusAPI.model('ActionMatchTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:EnvironmentMatchTypeV1':
      return flaskRestPlusAPI.model('EnvironmentMatchTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:VariableDefinitionTypeV1':
      return flaskRestPlusAPI.model('VariableDefinitionTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ExpressionTypeV1':
      return flaskRestPlusAPI.model('ExpressionTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:VariableReferenceTypeV1':
      return flaskRestPlusAPI.model('VariableReferenceTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:AttributeSelectorTypeV1':
      return flaskRestPlusAPI.model('AttributeSelectorTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:AttributeDesignatorTypeV1':
      return flaskRestPlusAPI.model('AttributeDesignatorTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:SubjectAttributeDesignatorTypeV1':
      return flaskRestPlusAPI.model('SubjectAttributeDesignatorTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:AttributeValueTypeV1':
      return flaskRestPlusAPI.model('AttributeValueTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:FunctionTypeV1':
      return flaskRestPlusAPI.model('FunctionTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ConditionTypeV1':
      return flaskRestPlusAPI.model('ConditionTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ApplyTypeV1':
      return flaskRestPlusAPI.model('ApplyTypeV1', {

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ObligationsTypeV1':
      return flaskRestPlusAPI.model('ObligationsTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:ObligationTypeV1':
      return flaskRestPlusAPI.model('ObligationTypeV1', {
        #Element  has a type that is not catered for () 0

      })
    if typeName=='urn:oasis:names:tc:xacml:2.0:policy:schema:cd:04:AttributeAssignmentTypeV1':
      return flaskRestPlusAPI.model('AttributeAssignmentTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TimePeriodTypeLOWERV1':
      return flaskRestPlusAPI.model('TimePeriodTypeLOWERV1', {
        #Element StartDateTime has a type that is not catered for (DateTimeType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PartyContactTypeLOWERV1':
      return flaskRestPlusAPI.model('PartyContactTypeLOWERV1', {
        #Element  has a type that is not catered for () 0
        'Contact': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactTypeLOWERV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyContactTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactTypeLOWERV1':
      return flaskRestPlusAPI.model('ContactTypeLOWERV1', {
        #Element  has a type that is not catered for () 0
        #Element PreferredLanguageCode has a type that is not catered for (LanguageCodeType) 0
        'Department': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'JobTitle': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Responsibility': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element OrganizationIndicator has a type that is not catered for (IndicatorType) 0
        'PreferredCommunicationChannelCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'OrganizationName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'ContactTelexCommunication': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactTelexCommunicationTypeLOWERV1'))),
        'PersonName': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonNameTypeLOWERV1')),
        #Element BirthDateTime has a type that is not catered for (DateTimeType) 0
        'ContactAddressCommunication': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactAddressCommunicationTypeLOWERV1'))),
        'ContactPhoneCommunication': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactPhoneCommunicationTypeLOWERV1'))),
        'ContactFaxCommunication': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactFaxCommunicationTypeLOWERV1'))),
        'ContactEmailCommunication': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactEmailCommunicationTypeLOWERV1'))),
        'ContactWebsiteCommunication': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactWebsiteCommunicationTypeLOWERV1'))),
        'Preference': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PreferenceTypeLOWERV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactPhoneCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('ContactPhoneCommunicationTypeLOWERV1', {
        #Element  has a type that is not catered for () 0
        'PreferredMediaFormatCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'PhoneCommunication': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PhoneCommunicationTypeLOWERV1')),
        'Status': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StatusTypeLOWERV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactPhoneCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactFaxCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('ContactFaxCommunicationTypeLOWERV1', {
        #Element  has a type that is not catered for () 0
        'FaxCommunication': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FaxCommunicationTypeLOWERV1')),
        'Status': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StatusTypeLOWERV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactFaxCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactEmailCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('ContactEmailCommunicationTypeLOWERV1', {
        #Element  has a type that is not catered for () 0
        'PreferredMediaFormatCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'EmailCommunication': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EmailCommunicationTypeLOWERV1')),
        'Status': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StatusTypeLOWERV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactEmailCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactTelexCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('ContactTelexCommunicationTypeLOWERV1', {
        #Element  has a type that is not catered for () 0
        'PreferredMediaFormatCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Status': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StatusTypeLOWERV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactTelexCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactWebsiteCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('ContactWebsiteCommunicationTypeLOWERV1', {
        #Element  has a type that is not catered for () 0
        'WebsiteCommunication': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WebsiteCommunicationTypeLOWERV1')),
        'Status': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StatusTypeLOWERV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactWebsiteCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:ContactAddressCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('ContactAddressCommunicationTypeLOWERV1', {
        #Element  has a type that is not catered for () 0
        'PreferredMediaTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'PreferredMediaFormatCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element SeasonalIndicator has a type that is not catered for (IndicatorType) 0
        'SeasonalEffectivePeriod': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SeasonalEffectivePeriodTypeLOWERV1')),
        'AddressCommunication': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AddressCommunicationTypeLOWERV1')),
        'Status': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StatusTypeLOWERV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactAddressCommunicationTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PersonNameTypeLOWERV1':
      return flaskRestPlusAPI.model('PersonNameTypeLOWERV1', {
        #Element  has a type that is not catered for () 0
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'FullName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'FirstName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'MiddleName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'FamilyName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'MaidenName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Title': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Salutation': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element Prefix has a type that is not catered for (StringType) 0
        #Element Suffix has a type that is not catered for (StringType) 0
        #Element MilitaryRank has a type that is not catered for (StringType) 0
        'PreferredName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'Alias': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'EffectiveTimePeriod': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TimePeriodTypeLOWERV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PreferenceTypeLOWERV1':
      return flaskRestPlusAPI.model('PreferenceTypeLOWERV1', {
        #Element PriorityRanking has a type that is not catered for (NumericType) 0
        #Element PreferredIndicator has a type that is not catered for (IndicatorType) 0

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PhoneCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('PhoneCommunicationTypeLOWERV1', {
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'TypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Preference': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PreferenceTypeLOWERV1')),
        'PrivacyProfile': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PrivacyProfileTypeLOWERV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:StatusTypeLOWERV1':
      return flaskRestPlusAPI.model('StatusTypeLOWERV1', {
        'Code': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element EffectiveDateTime has a type that is not catered for (DateTimeType) 0
        #Element EffectiveEndDateTime has a type that is not catered for (DateTimeType) 0
        'ReasonCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Description': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'SubStatusCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:FaxCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('FaxCommunicationTypeLOWERV1', {
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Preference': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PreferenceTypeLOWERV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:EmailCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('EmailCommunicationTypeLOWERV1', {
        #Element HTMLPreferredIndicator has a type that is not catered for (IndicatorType) 0
        #Element URI has a type that is not catered for (URIType) 0
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Preference': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PreferenceTypeLOWERV1')),
        'PrivacyProfile': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PrivacyProfileTypeLOWERV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:WebsiteCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('WebsiteCommunicationTypeLOWERV1', {
        #Element WebsiteURI has a type that is not catered for (URIType) 0
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Preference': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PreferenceTypeLOWERV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:SeasonalEffectivePeriodTypeLOWERV1':
      return flaskRestPlusAPI.model('SeasonalEffectivePeriodTypeLOWERV1', {
        #Element StartMonthDay has a type that is not catered for (MonthDayTypeLOWER) 0
        #Element EndMonthDay has a type that is not catered for (MonthDayTypeLOWER) 0
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSeasonalEffectivePeriodTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AddressCommunicationTypeLOWERV1':
      return flaskRestPlusAPI.model('AddressCommunicationTypeLOWERV1', {
        'Address': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AddressTypeLOWERV1')),
        'UseCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Preference': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PreferenceTypeLOWERV1')),
        'EffectiveTimePeriod': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TimePeriodTypeLOWERV1')),
        'PrivacyProfile': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PrivacyProfileTypeLOWERV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:PrivacyProfileTypeLOWERV1':
      return flaskRestPlusAPI.model('PrivacyProfileTypeLOWERV1', {
        #Element OptOutIndicator has a type that is not catered for (IndicatorType) 0
        'SourceCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ReasonCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:AddressTypeLOWERV1':
      return flaskRestPlusAPI.model('AddressTypeLOWERV1', {
        #Element  has a type that is not catered for () 0
        'FormatCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'LineOne': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineTwo': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineThree': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineFour': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineFive': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineSix': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineSeven': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineEight': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'LineNine': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'Building': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        #Element Floor has a type that is not catered for (StringType) 0
        'Area': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'CityName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'StateName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'ProvinceName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'RuralRoute': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'CountyName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'CountryCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'CountrySubDivisionID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        'CitySubDivisionName': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'DeliveryPointCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'DeliveryPointBarCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'DeliveryPointTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'ProcessingCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'MoveTypeCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        #Element MoveEffectiveDate has a type that is not catered for (DateType) 0
        'AttentionOf': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'CareOf': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:NameTypeV1'))),
        'PostalCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'LongPostalCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'GEOCodeID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:IdentifierTypeV1')),
        #Element InCityLimitIndicator has a type that is not catered for (IndicatorType) 0
        'TimeZoneCode': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:CodeTypeV1')),
        'Custom': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAddressTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:LocationIdentificationTypeLOWERV1':
      return flaskRestPlusAPI.model('LocationIdentificationTypeLOWERV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomPartyContactTypeV1':
      return flaskRestPlusAPI.model('CustomPartyContactTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactTypeV1':
      return flaskRestPlusAPI.model('CustomContactTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactPhoneCommunicationTypeV1':
      return flaskRestPlusAPI.model('CustomContactPhoneCommunicationTypeV1', {
        'PrimaryByPurpose': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ParentObjectID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'OrigSystemReference': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_OrigSystemReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactFaxCommunicationTypeV1':
      return flaskRestPlusAPI.model('CustomContactFaxCommunicationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactEmailCommunicationTypeV1':
      return flaskRestPlusAPI.model('CustomContactEmailCommunicationTypeV1', {
        'PrimaryByPurpose': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'EmailFormat': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ParentObjectID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'OrigSystemReference': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_OrigSystemReferenceTypeV1')),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactTelexCommunicationTypeV1':
      return flaskRestPlusAPI.model('CustomContactTelexCommunicationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactWebsiteCommunicationTypeV1':
      return flaskRestPlusAPI.model('CustomContactWebsiteCommunicationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomContactAddressCommunicationTypeV1':
      return flaskRestPlusAPI.model('CustomContactAddressCommunicationTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomSeasonalEffectivePeriodTypeV1':
      return flaskRestPlusAPI.model('CustomSeasonalEffectivePeriodTypeV1', {

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:CustomAddressTypeV1':
      return flaskRestPlusAPI.model('CustomAddressTypeV1', {
        'ValidatedFlag': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'AddressLinesPhonetic': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'SalesTaxInsideCtyLimits': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://xmlns.oracle.com/EnterpriseObjects/Core/Custom/Common/V2:IC_OrigSystemReferenceTypeV1':
      return flaskRestPlusAPI.model('IC_OrigSystemReferenceTypeV1', {
        'SystemID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),
        'ReferenceID': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://xmlns.oracle.com/EnterpriseObjects/Core/Common/V2:TextTypeV1'))),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1/HROrganizatinUnitRBO:HROrganizationUnitReferenceTypeV1':
      return flaskRestPlusAPI.model('HROrganizationUnitReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1/HROrganizatinUnitRBO:IdentificationTypeV1')),
        'Name': fields.String(default='',description=''),
        'Description': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1/HROrganizatinUnitRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'OrgCode': fields.String(default='',description=''),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('HROrganizationUnitEBOV1', {
    'HROrganizationUnitEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1:HROrganizationUnitEBOTypeV1')),

  })

