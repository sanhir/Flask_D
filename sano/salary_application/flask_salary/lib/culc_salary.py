import math

def get_breakdown(salary):
    # 100万円を超えた分は20%, 超えない分は10%の課税
    if salary >= 100 * 10000:
        tax = (salary - 100 * 10000) * 0.20 + 100 * 10000 * 0.10
    else:
        tax = salary * 0.10

    # 税額は小数第一位を四捨五入し、整数とする
    tax = math.floor(tax)
    pay_amount = salary - tax
    
    return pay_amount, tax
