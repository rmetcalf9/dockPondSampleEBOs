from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  return flaskRestPlusAPI.model('AnimalV3', {
      'name': fields.String(default='',description='What is the name of this animal? (Must be unique)'),
      'type': fields.String(default='',description='What type of animal are they?'),
      'genderGUID': fields.String(default='',description='What gender is the animal'),
      'lastUpdateDate': fields.DateTime(dt_format=u'iso8601', description='Last time job record was changed (excluding runs)'),
      'lastRunDate': fields.DateTime(dt_format=u'iso8601', description='Last time job record was run')
  })