import sys
from datetime import datetime, timedelta

class reconcile_accounts(object):
  def __call__(self, transactions1, transactions2):
    #insert an index to keep track of original order
    for index,transaction in enumerate(transactions1): transaction.insert(0, str(index))
    for index,transaction in enumerate(transactions2): transaction.insert(0, str(index))

    #sort the transactions based on the date
    sorted_transactions1 = sorted(transactions1, key=lambda date : datetime.strptime(date[1], "%Y-%m-%d"))
    sorted_transactions2 = sorted(transactions2, key=lambda date : datetime.strptime(date[1], "%Y-%m-%d"))

    for transaction1 in sorted_transactions1:
      #only select transactions with valid date and without FOUND parameter
      valid_transactions2 = [t for t in sorted_transactions2 if datetime.strptime(t[1], "%Y-%m-%d") in self._valid_transaction_date_delta(transaction1) and len(t) == 5]
      if len(valid_transactions2) == 0: 
        transactions1[int(transaction1[0])].append('MISSING')
        continue

      #compare valid transactions and insert FOUND
      for transaction2 in valid_transactions2:
        if transaction1[2:] == transaction2[2:]:
          transactions1[int(transaction1[0])].append('FOUND')
          transaction2.append('FOUND')
          break

    #recovering order of second list (doing this to avoid N+1 ordering over second list of transactions inside the loop)
    transactions2 = sorted(sorted_transactions2, key=lambda index: index[0])
    
    return (self._clear_transaction_response(transactions1), self._clear_transaction_response(transactions2))


  def _valid_transaction_date_delta(self, transaction):
    transation_date = datetime.strptime(transaction[1], "%Y-%m-%d")
    transation_date_delta = [transation_date - timedelta(days=1), transation_date, transation_date + timedelta(days=1)]
    return transation_date_delta


  def _clear_transaction_response(self, transactions):
    for transaction in transactions:
      del transaction[0]
      if len(transaction) == 4:
        transaction.append('MISSING')
    return transactions

sys.modules[__name__] = reconcile_accounts()
