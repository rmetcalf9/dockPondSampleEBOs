from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  return flaskRestPlusAPI.model('Plant', {
      'name': fields.String(default='',description='What is the name of this plant? (Must be unique)'),
      'type': fields.String(default='',description='What type of plant are they?'),
      'creationDate': fields.DateTime(dt_format=u'iso8601', description='Time job record was created'),
      'lastUpdateDate': fields.DateTime(dt_format=u'iso8601', description='Last time job record was changed (excluding runs)'),
      'lastRunDate': fields.DateTime(dt_format=u'iso8601', description='Last time job record was run')
  })
