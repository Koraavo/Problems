"""
In progressive tax systems, tax rates change according to the income.
Tax brackets are divisions that regulate those changes.

Here's an example of tax brackets in a certain tax system:

0 — 15,527: 0% tax

15,528 — 42,707: 15% tax

42,708 — 132,406: 25% tax

132,407 and more: 28% tax

Suppose we use a simplified version of taxation and apply one tax rate to the entire amount of money.
Write a program that calculates the tax that a person's going to pay based on their income.

"""
tax = int(input())
tax_percent = [0, 15, 25, 28]

if tax <= 15527:
    per = tax_percent[0]
elif 15528 <= tax <= 42707:
    per = tax_percent[1]
elif 42708 <= tax <= 132406:
    per = tax_percent[2]
elif tax >= 132407:
    per = tax_percent[3]

tax_dollar = round((per * tax) / 100)
print(f"The tax for {tax} is {per}%. That is {tax_dollar} dollars!")