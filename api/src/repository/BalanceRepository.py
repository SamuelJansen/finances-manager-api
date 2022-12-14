from python_framework import SqlAlchemyProxy as sap
from python_framework import Repository

from model import Balance


@Repository(model = Balance.Balance)
class BalanceRepository:

    def save(self, model):
        return self.repository.saveAndCommit(model)

    def saveAll(self, modelList):
        return self.repository.saveAllAndCommit(modelList)

    def findAll(self):
        return self.repository.findAllAndCommit(self.model)

    def findByKey(self, key):
        return self.repository.findByKeyAndCommit(key, self.model)

    def findAllByKeyIn(self, keyList):
        return self.repository.findAllByKeyInAndCommit(keyList)

    def existsByKey(self, key):
        return self.repository.existsByKeyAndCommit(key, self.model)

    def notExistsByKey(self, key):
        return not self.existsByKey(key)

    def deleteByKey(self, key):
        self.repository.deleteByKeyAndCommit(key, self.model)

    def findById(self, id):
        return self.repository.findByIdAndCommit(id, self.model)

    def findAllByIdIn(self, idList):
        return self.repository.findAllByIdInAndCommit(idList)

    def existsById(self, id):
        return self.repository.existsByIdAndCommit(id, self.model)

    def notExistsById(self, id):
        return not self.existsById(id)

    def deleteById(self, id):
        self.repository.deleteByIdAndCommit(id, self.model)

    def findAllByTypeIn(self, typeList):
        modelList = self.repository.session.query(self.model).filter(self.model.type.in_(typeList)).all()
        self.repository.session.commit()
        return self.repository.load(modelList)

    def findAllByQuery(self, query):
        return self.repository.findAllByQueryAndCommit(query, self.model)

    def existsByLabelInAndUserKey(self, labelList, userKey):
        objectExists = self.repository.session.query(sap.exists().where(
            sap.and_(
                self.model.userKey == userKey,
                self.model.label.in_(labelList)
            )
        )).one()[0]
        self.repository.session.commit()
        return objectExists

    def findAllByUserKey(self, userKey):
        modelList = self.repository.session.query(self.model).filter(self.model.userKey == userKey).all()
        self.repository.session.commit()
        return self.repository.load(modelList)
