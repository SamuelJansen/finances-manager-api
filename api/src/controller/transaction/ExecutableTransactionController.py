from python_framework import Controller, ControllerMethod, HttpStatus

# from ApiKeyContext import ApiKeyContext
from dto import TransactionDto

@Controller(
    url = '/transaction',
    tag = 'Transaction',
    description = 'Transaction controller'
    , logRequest = True
    , logResponse = True
)
class ExecutableTransactionController:

    @ControllerMethod(url = '/execute',
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.API, ApiKeyContext.USER],
        requestClass=[TransactionDto.ExecutableTransactionRequestDto],
        responseClass=[TransactionDto.TransactionResponseDto]
    )
    def put(self, dto):
        return self.service.transaction.execute(dto), HttpStatus.CREATED