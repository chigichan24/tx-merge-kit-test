from db import Db

def main():
    db = Db()
    result = db.runCreditLimitWithGetAddress(param=125)
    print(result)

if __name__ == '__main__':
    main()