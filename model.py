from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Information for users, to store access tokens"""

    __tablename__ = 'users'

    user_table_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.String(75), nullable=False)


    def __repr__(self):
        """Provide helpful information when printed to the console"""

        return "<user_id: %s, email: %s, access_token: %s"\
            % (self.user_table_id, self.user_id)

##############################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///muse'
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB"
