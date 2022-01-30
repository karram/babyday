import sqlalchemy as sa
import sqlalchemy.orm as orm
import babyday.data.__all_models
from babyday.data.modelbase import SqlAlchemyBase

__factory = None


def global_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must supply a db filename")

    conn_str = "sqlite:///" + db_file.strip()
    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    # Create required tables.
    SqlAlchemyBase.metadata.create_all(engine)


def create_session():
    global __factory
    if not __factory:
        raise Exception("DB Not initialized. Use global_init() first.")
    return __factory()


class SessionContext:
    def __init__(self, commit_on_success=False):
        self.commit_on_success: bool = commit_on_success
        self.session: orm.Session = create_session()
        self.session.expire_on_commit = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_val and self.commit_on_success:
            self.session.commit()

        self.session.close()

