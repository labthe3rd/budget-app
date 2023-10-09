class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.total = 0
    
    #String representation
    def __str__(self):
        #We wnat 30 characters and to center the name
        #First get length of name
        max_length = 30
        name_length = len(self.name)
        #We do not want a remainder we will account for that
        border_length = (max_length - name_length) // 2
        border_remainder = (max_length - name_length) % 2
        border_front = border_length
        border_end = border_length
        #add the remaining astericks needed to the end
        if border_remainder > 0:
            border_end += border_remainder
        #Now create the border strings
        border1_str = "*"*border_front
        border2_str = "*"*border_end
        top_line = border1_str + self.name + border2_str
        
        #Let us now handle the categories
        def write_line(description,amount):
            
            result = ""
            max_length_str1 = 23
            max_length_str2 = 7
            str1 = str(description)
            str1_length = len(str1)
            str2 = f'{amount:.2f}'
            str2_length = len(str2)
   
            if str1_length < 23:
                str1_remaining = 23 - str1_length
                str1 = str1 + (" "*str1_remaining)         
            if str1_length > 23:
                print("str1_length > 23:"+str1)
                str1 = str1[0:23]
                print("result str1_length > 23:"+str1)
            if str2_length < 7:
                str2_remaining = 7 - str2_length
                str2 = (" "*str2_remaining) +str2     
            if str2_length > 7:
                str2 = str2[0:6]
            result = str1 + str2
            return result
        
        output = top_line
        total_amount = 0
        for entry in self.ledger:
            print(entry)
            line = write_line(entry["description"],entry["amount"])
            output = output + "\n" + line
            total_amount += float(entry["amount"])
        total_line = f'Total: {total_amount:.2f}'
        output = output + "\n" + total_line
        return output
    
    def deposit(self, amount, description=""):
        
        newEntry = {
            "amount": amount,
            "description": description
        }
        self.ledger.append(newEntry)
        self.balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount) == True:
            newEntry = {
                "amount": -amount,
                "description": description
            }
            self.ledger.append(newEntry)
            self.balance -= amount
            self.total += amount
            return True
        return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, target):
        if self.check_funds(amount) == True:
            target.deposit(amount,"Transfer from " + self.name)
            self.withdraw(amount, "Transfer to " + target.name)
            return True
        return False
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        if amount == 0:
            return False
        return True
        



def create_spend_chart(categories):
    total_amount = 0
    total_category = []
    max_name_length = 0
    for category in categories:
        total_amount += category.total
        name_length = len(category.name)
        if name_length > max_name_length:
            max_name_length = name_length
    
    for category in categories:
        total_category.append({
            "name": category.name,
            "percent": int(int((category.total/total_amount)*10)*10)
        })


    #define nested function to write the lines
    
    
    #define the output ahead of time
    output = ""
    
    #Create the title
    title_line = "Percentage spent by category"
    output = title_line + "\n"
    
    #Create the data points of the chart
    for i in range(100,-1,-10):
        print("writing percentage title: ", i)
        if i != 100:
            output += " "
        if i < 10:
            output += " "
        output += str(i) + "|" + " "
        for category in total_category:
            if category["percent"] >= i:
                output += "o"
            else:
                output += " "
            output += "  "
        output += "\n"
    
    #Create line below data
    output += "    "
    output += "---"*len(categories)
    output += "-\n"
    
    #Now write the y axis label
    print("Max name length is ", max_name_length)
    for row in range(0,max_name_length,1):
        output += " "*5
        for category in categories:
            name_length = len(category.name)
            if row < name_length:
                output+=category.name[row]
            else:
                output+=" "
            output+=" "*2
        if row < max_name_length-1:
            output += "\n"
    #create function for 
    print(output)
    return output