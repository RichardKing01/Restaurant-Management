# This can be shrunken down substantially
class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.Total = 0
    self.Negative = 0

  def deposit(self, amount, description=""):
    self.Total = self.Total + amount
    L = {"amount": amount, "description": description}
    self.ledger.append(L)

  def withdraw(self, amount, description=""):
    if amount > self.Total:
      return False
    else:
      Negative_amount = -1 * amount
      self.Total = self.Total + Negative_amount
      self.Negative += Negative_amount
      L = {"amount": Negative_amount, "description": description}
      self.ledger.append(L)
      return True

  def get_balance(self):
    return (self.Total)

  def transfer(self, amount, Other_Category):
    if amount > self.Total:
      return False
    else:
      self.withdraw(amount, f"Transfer to {Other_Category.name}")
      Other_Category.deposit(amount, f"Transfer from {self.name}")
      return True

  def check_funds(self, amount):
    if self.Total < amount:
      return False
    else:
      return True

  def __str__(self):
    A = len(self.name)
    Heading_length = 30-A
    Complete = []

    if Heading_length % 2 == 0:
     Heading_length = int(Heading_length)
     Border_Length = int(Heading_length/2)
     Star = "*"
     Heading = (Star*Border_Length).strip() + (self.name).strip() + (Star*Border_Length).strip()

    else:
     Heading_length += 1
     Border_Length = int(Heading_length/2)
     Star = "*"
     Heading = (Star*(Border_Length - 1)).strip() + (self.name).strip() + (Star*Border_Length).strip()

    Output = Heading

    for Dictionary in self.ledger:
        count = self.ledger.count(Dictionary)

        if Dictionary in Complete:
            continue

        if count > 1:
            AMOUNT = Dictionary["amount"]
            AMOUNT = AMOUNT * 2
            AMOUNT = str(format(AMOUNT, ".2f")).strip()
            DESCRIPTION = (Dictionary["description"]).strip()
            Gap = " "
            TOTAL_INIT_LENGTH = len(AMOUNT) + len(DESCRIPTION) + len(str(count)) + 2

            if len(DESCRIPTION) > (29-len(AMOUNT)):
                length = 29 - len(AMOUNT)
                DESCRIPTION = DESCRIPTION[0:length]
                DESCRIPTION = DESCRIPTION + " " + "x" + str(count)
                TOTAL_INIT_LENGTH = len(DESCRIPTION) + len(AMOUNT)

            if TOTAL_INIT_LENGTH <= 29:
                REMAIN = 29 - TOTAL_INIT_LENGTH
                LINE = DESCRIPTION + " " + "x" + str(count) + Gap*(REMAIN + 1) + AMOUNT
                Output = Output +"\n" + LINE

        else:
            AMOUNT = Dictionary["amount"]
            AMOUNT = str(format(AMOUNT, ".2f")).strip()
            DESCRIPTION = (Dictionary["description"]).strip()
            Gap = " "
            TOTAL_INIT_LENGTH = len(AMOUNT) + len(DESCRIPTION)

            if len(DESCRIPTION) > (29-len(AMOUNT)):
                length = 29 - len(AMOUNT)
                DESCRIPTION = DESCRIPTION[0:length]
                TOTAL_INIT_LENGTH = len(DESCRIPTION) + len(AMOUNT)

            if TOTAL_INIT_LENGTH <= 29:
                REMAIN = 29 - TOTAL_INIT_LENGTH
                LINE = DESCRIPTION + Gap*(REMAIN + 1) + AMOUNT
                Output = Output +"\n" + LINE


        Complete.append(Dictionary)

    Output =  Output + "\n"  + "Total: " + str(format(self.Total, ".2f")) + "\n"  + Star*30
    return Output


