from repository.user_repository import UserRepository

class UserService:
    """
    Service component that contains business logic.

    Uses dependency injection to receive a repository instance.
    """

    def __init__(self, repository: UserRepository):
        """Initializes the service with a given repository."""
        self.repository = repository

    def list_users(self):
        """Retrieves the list of users from the repository."""
        return self.repository.get_users()