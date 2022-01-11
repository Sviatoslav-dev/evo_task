from core import db


def commit(obj):
    db.session.add(obj)
    db.session.commit()
    db.session.refresh(obj)
    return obj


class Name(db.Model):
    __tablename__ = 'names'
    name = db.Column(db.String(50), primary_key=True)

    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        return commit(obj)

    @classmethod
    def get_name(cls, name):
        try:
            obj = cls.query.filter_by(name=name).first()
        except Exception:
            return -1

        return obj
