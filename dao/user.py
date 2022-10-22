from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(User).get(bid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        user = self.get_one(rid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        user.name = user_d.get("name")

        self.session.add(user)
        self.session.commit()

    def get_by_username(self, username):
        try:
            user = self.session.query(User).filter(User.username == username).all()
            if len(user) > 0:
                return user[0]
            else:
                return None
        except Exception as e:
            self.session.rollback()
            print(e)
            user = None
        return user
