from app import app, db
from app.models import User, Weekly_Reflection

@app.shell_context_processor
def make_shell_context():
   return {'db':db, 'User': User, 'Weekly_Reflection': Weekly_Reflection}