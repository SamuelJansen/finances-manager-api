from python_framework import Service, ServiceMethod

from dto import BalanceDto
from model import Balance
from helper.static import MathStaticHelper


@Service()
class BalanceService:

    @ServiceMethod(requestClass=[[BalanceDto.BalanceRequestDto]])
    def createAll(self, dtoList):
        modelList = self.mapper.balance.fromRequestDtoListToModelList(dtoList)
        self.saveAllModel(modelList)
        return self.mapper.balance.fromModelListToResponseDtoList(modelList)


    @ServiceMethod(requestClass=[str, float])
    def executeTransactionByKey(self, key, value):
        model = self.findModelByKey(key)
        self.validator.balance.validateTransaction(model, value)
        model.value = MathStaticHelper.round(model.value + value)
        return self.mapper.balance.fromModelToResponseDto(self.saveModel(model))


    @ServiceMethod()
    def findAll(self):
        return self.mapper.balance.fromModelListToResponseDtoList(self.findAllModel())


    @ServiceMethod(requestClass=[str])
    def findByKey(self, key):
        return self.mapper.balance.fromModelToResponseDto(self.findModelByKey(key))


    @ServiceMethod(requestClass=[str])
    def findModelByKey(self, key):
        return self.repository.balance.findByKey(key)


    @ServiceMethod(requestClass=[int])
    def findModelById(self, id):
        return self.repository.balance.findById(id)


    @ServiceMethod()
    def findAllModel(self):
        return self.repository.balance.findAll()


    @ServiceMethod(requestClass=[Balance.Balance])
    def saveModel(self, model):
        return self.repository.balance.save(model)


    @ServiceMethod(requestClass=[[Balance.Balance]])
    def saveAllModel(self, modelList):
        return self.repository.balance.saveAll(modelList)


    @ServiceMethod(requestClass=[str])
    def deleteByKey(self, key):
        self.repository.balance.deleteByKey(key)
