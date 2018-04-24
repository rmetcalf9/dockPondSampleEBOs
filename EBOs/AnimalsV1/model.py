from flask_restplus import fields

def getModel(appObj):
  return appObj.flastRestPlusAPIObject.model('Animal', {
      'name': fields.String(default='',description='What is the name of this animal? (Must be unique)'),
      'type': fields.String(default='',description='What type of animal are they?'),
      'LikedByRobert': fields.Boolean(default=False,description='Does Robert like this animal?'),
      'genderGUID': fields.String(default='',description='What gender is the animal'),
      'nextScheduledRun': fields.DateTime(default='',description='When are they next scheduled to run in a race?'),
      'creationDate': fields.DateTime(dt_format=u'iso8601', description='Time job record was created'),
      'lastUpdateDate': fields.DateTime(dt_format=u'iso8601', description='Last time job record was changed (excluding runs)'),
      'lastRunDate': fields.DateTime(dt_format=u'iso8601', description='Last time job record was run')
  }
