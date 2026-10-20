from sqlalchemy.orm import Session
from src.modules.user.user_model import UserModel


class UserService:
  # Tipamos o parâmetro do construtor com a classe Session
  def __init__(self, db_session: Session):
    self.db: Session = db_session

  def get_user(self, user_id: int):
    existing_user = (
        self.db.query(UserModel).filter(UserModel.id == user_id).first()
    )
    return existing_user if existing_user!= None else "não existe"

  