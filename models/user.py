from models.base_model import BaseModel


class User(BaseModel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ""
        self.first_name = ""
        self.last_name = ""
        self.password = ""
