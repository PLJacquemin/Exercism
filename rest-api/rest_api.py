import json

class RestAPI:
    def __init__(self, database=None):
        self.database = {}
        for user in database["users"]:
            self.database[user["name"]] = user

    def get(self, url, payload=None):
        result = self.database
        if url == "/users":
            if payload != None:
                result = {"users":[result[user] for user in result if result[user]['name'] in json.loads(payload)["users"]]}
            else:
                result = {"users":[]}
        return json.dumps(result)

    def post(self, url, payload=None):
        input_dict = self.database
        if url == "/add" and payload != None:
            to_add = json.loads(payload)["user"]
            # Creating the new entry
            input_dict[to_add] = {"name": to_add, "owes": {}, "owed_by": {}, "balance": 0.0}

            # updating the database
            self.database = input_dict
            return json.dumps(input_dict[to_add])

        elif url == "/iou" and payload != None:
            # getting 'who', 'to whom' and calculating new balances
            lender = json.loads(payload)["lender"]
            borrower = json.loads(payload)["borrower"]
            amount = json.loads(payload)["amount"]
            input_dict[lender]['balance'] += amount
            input_dict[borrower]['balance'] -= amount

            # checking the differnce between the amount, how much the borrower owes to the lender and how much the lender owes to the borrower
            diff = amount + input_dict[lender]['owed_by'].get(borrower, 0) - input_dict[borrower]['owed_by'].get(lender, 0)

            # Removing all 'owed_by', 'owes'
            if borrower in input_dict[lender]['owed_by']:
                del input_dict[lender]['owed_by'][borrower]
            if borrower in input_dict[lender]['owes']:
                del input_dict[lender]['owes'][borrower]
            if lender in input_dict[borrower]['owed_by']:
                del input_dict[borrower]['owed_by'][lender]
            if lender in input_dict[borrower]['owes']:
                del input_dict[borrower]['owes'][lender]

            # Creating new 'owed_by', 'owes'
            if diff > 0:
                # if the borrower owes money to the lender
                input_dict[lender]['owed_by'][borrower] = diff
                input_dict[borrower]['owes'][lender] = diff
            elif diff < 0:
                # if the lender owes money to the borrower
                input_dict[lender]['owes'][borrower] = - diff
                input_dict[borrower]['owed_by'][lender] = - diff

            # updating the database
            self.database = json.dumps(input_dict)

            iou = {"users":[input_dict[user] for user in input_dict if input_dict[user]['name'] in [lender,borrower]]}
            return json.dumps(iou)
