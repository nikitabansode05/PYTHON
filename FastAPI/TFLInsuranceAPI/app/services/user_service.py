from app.repositories.user_repository import UserRepository

class UserService:
    
    def __init__(self,repository:UserRepository):
        self.repository=repository
        
    def get_all_users(self):
        users=self.repository.get_all_users()
        return users
    
    def get_user_by_id(self,user_id:int):
        user=self.repository.get_all_users(user_id)
        return user