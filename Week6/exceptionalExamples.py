#try -> except blocks ||| Try Catch 


#%%
x = 1 / 0 #Zero division error

#%%

try:
    x = 1 / 0
except Exception as someAlias:
    print(someAlias)

#%%

try:
    x = 1 / 0
except ZeroDivisionError as someAlias:
    print(f"zero div. error: {someAlias}")
except Exception as e:
    print(f"Final Case: {e}")


#%%

#Order Matters. The Execption base class will catch all exceptions so be careful to use it as a final case.
try:
    x = 1 / 0
except Exception as e:
    print(f"Final Case: {e}")
except ZeroDivisionError as someAlias:
    print(f"zero div. error: {someAlias}")


#%%
class myErrorMessage(Exception):

    def __init__(self,expression, message):
        self.expression = expression
        self.message = message

#%%
x = 1
y = 2
try:
    if x == y:
        pass
    else:
        raise myErrorMessage("ERROR","UIX-2556") #Makes vba proud!
except myErrorMessage as e:
    print(f"Custom Error: {e.expression}:{e.message}! N1c3:)")

# %%

for i in range(0,5):
    try:    
        if i % 2 == 0:
            x = 1/0 # zeroDivsionError
        elif i % 3 == 0:
            x = [0,1,2,3] #index out of range
            for i in range(0,5):
                print(x[i])

            print(someUndefinedVariable) #NameError
        else:
            x = 1
            y = 2
            if x == y:
                pass
            else:
                raise myErrorMessage("ERROR","UIX-2556")
# except ZeroDivisionError as theErrorMessage:
#     # print("There was an error")
#     print(f"There was a zero division error: {theErrorMessage}")
# except IndexError as e:
#     print(e)
    except (ZeroDivisionError, IndexError) as e: #Multiple exceptions can be handled in the same except block
        print(f"Multi error handler: {e}")
    except NameError as someNameErrorMessage:
        print(f"{someNameErrorMessage}")
    except myErrorMessage as e:
        print(f"Custom Error: {e.expression}:{e.message}! N1c3:)")
    except Exception: #Final catch all
        print("Something unknown happened")





# %%
