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

    @classmethod
    def get_all_names(cls, page, page_size):
        all_names = cls.query.limit(page_size).offset((page - 1) * page_size).all()
        all_names_list = []
        for name_dict in all_names:
            name = [v for k, v in name_dict.__dict__.items() if k == "name"]
            all_names_list.append(name[0])
        return all_names_list

    @classmethod
    def names_count(cls):
        return cls.query.count()
