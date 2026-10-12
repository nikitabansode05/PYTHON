
# from app.repositories.user_repository import UserRepository
# from dataclasses import asdict


# class UserService:

#       def __init__(self, repository: UserRepository ):
#             self.repository = repository


#       def get_all_users(self):
#                users = self.repository.get_users()
#                return [asdict(user) for user in users]     


    #   def get_users(self, user_id: int):
    #           user = self.repository.get_by_id(user_id)
      
    #           if user is None:
    #               return None
      
    #           return asdict(user)


    # #   def create_users(self, user_id:int):
    # #         if user_id["user_id"] < 0:
    # #             raise ValueError("Minimum  user id must be 0 ")

    # #         user = self.repository.create(user_id)
    # #         return asdict(user)

    #   def update_user(self, user_id:int):
    #         user = self.repository.update(user_id)

    #         if user is None:
    #             return None

    #         return asdict(user)

    #   def delete_user(self, user_id: int):
    #         user_id = self.repository.delete(user_id)

    #         if user_id is None:
    #             return None

    #         return asdict(user_id)
        

from app.repositories.user_repository import UserRepository
from app.models.user import User


class UserService:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_all_users(self):
        users = self.repository.get_users()
        return users

    def create_user(self, user:User):
        return self.repository.add_users(user)