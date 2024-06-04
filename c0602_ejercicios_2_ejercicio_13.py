# ===================================================================================================================================================================
# 13. Calculadora de conversión de pesos a dólares, euros, libras y yenes
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
from decimal import *
print("")
print("="*80)
print("")
print('CONVERTIDOR DE DIVISAS')
print("")
print("="*80)
mxn_rate = 1
usd_rate = 16.97
eur_rate = 18.40
gbp_rate = 21.61
jpy_rate = 0.11
# -----------------------------------------------------------------------------------------------------------------------Data Input----
print("CODIGOS DE MONEDA \n\t - Para pesos: MXN\n\t - Para Dolares: USD\n\t - Para Euros: EUR\n\t - Para Libras: GBP\n\t - Para Yenes: JPY\n")
ammount2convert = Decimal(input("\t\t\tIngresa el monto a convertir: "))
from_currency = input("\t\t\tSelecciona el codigo de moneda inicial: ")
from_currency = from_currency.upper()
to_currency = input("\t\t\tIngresa el codigo de moneda objetivo: ")
to_currency = to_currency.upper()
divider = ("-"*80)
# --------------------------------------------------------------------------------------------------------------------Convert From MXN---

if from_currency == "MXN":
    if to_currency == "MXN":
        converted = Decimal(ammount2convert)/Decimal(mxn_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "USD":
        converted = Decimal(ammount2convert)/Decimal(usd_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "EUR":
        converted = Decimal(ammount2convert)/Decimal(eur_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "GBP":
        converted = Decimal(ammount2convert)/Decimal(gbp_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "JPY":
        converted = Decimal(ammount2convert)/Decimal(jpy_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    else:
        print(f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda destino: \'{
              to_currency}\' que ingresaste no es soportado\n")
elif from_currency == "USD":
    if to_currency == "MXN":
        converted = Decimal(ammount2convert)*Decimal(usd_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "USD":
        converted = ammount2convert
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "EUR":
        convert_to_mxn = Decimal(ammount2convert)*Decimal(usd_rate)
        converted = Decimal(convert_to_mxn)/Decimal(eur_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "GBP":
        convert_to_mxn = Decimal(
            ammount2convert)*Decimal(usd_rate)
        converted = Decimal(convert_to_mxn)/Decimal(gbp_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "JPY":
        convert_to_mxn = Decimal(ammount2convert)*Decimal(usd_rate)
        converted = Decimal(convert_to_mxn)/Decimal(jpy_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    else:
        print(f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda destino: \'{
              to_currency}\' que ingresaste no es soportado\n")
elif from_currency == "EUR":
    if to_currency == "MXN":
        converted = Decimal(ammount2convert)*Decimal(eur_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "USD":
        convert_to_mxn = Decimal(ammount2convert)*Decimal(eur_rate)
        converted = Decimal(convert_to_mxn)/Decimal(usd_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "EUR":
        convert_to_mxn = Decimal(
            ammount2convert)*Decimal(eur_rate)
        converted = Decimal(convert_to_mxn)/Decimal(eur_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "GBP":
        convert_to_mxn = Decimal(
            ammount2convert)*Decimal(eur_rate)
        converted = Decimal(convert_to_mxn)/Decimal(gbp_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "JPY":
        convert_to_mxn = Decimal(
            ammount2convert)*Decimal(eur_rate)
        converted = Decimal(convert_to_mxn)/Decimal(jpy_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    else:
        print(f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda destino: \'{
              to_currency}\' que ingresaste no es soportado\n")
elif from_currency == "GBP":
    if to_currency == "MXN":
        converted = Decimal(ammount2convert)*Decimal(gbp_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "USD":
        convert_to_mxn = Decimal(
            ammount2convert)*Decimal(gbp_rate)
        converted = Decimal(convert_to_mxn)/Decimal(usd_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "EUR":
        convert_to_mxn = Decimal(ammount2convert)*Decimal(gbp_rate)
        converted = Decimal(convert_to_mxn)/Decimal(eur_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "GBP":
        convert_to_mxn = Decimal(ammount2convert)*Decimal(gbp_rate)
        converted = Decimal(convert_to_mxn)/Decimal(gbp_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
            converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "JPY":
        convert_to_mxn = Decimal(ammount2convert)*Decimal(gbp_rate)
        converted = Decimal(convert_to_mxn)/Decimal(jpy_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
            converted:,.4f} {to_currency}\n\n{divider}")
    else:
        print(f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda destino: \'{
              to_currency}\' que ingresaste no es soportado\n")
elif from_currency == "JPY":
    if to_currency == "MXN":
        converted = Decimal(ammount2convert)*Decimal(jpy_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
            converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "USD":
        convert_to_mxn = Decimal(
            ammount2convert)*Decimal(jpy_rate)
        converted = Decimal(convert_to_mxn)/Decimal(usd_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
            converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "EUR":
        convert_to_mxn = Decimal(ammount2convert)*Decimal(jpy_rate)
        converted = Decimal(convert_to_mxn)/Decimal(eur_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
              converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "GBP":
        convert_to_mxn = Decimal(ammount2convert)*Decimal(jpy_rate)
        converted = Decimal(convert_to_mxn)/Decimal(gbp_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
            converted:,.4f} {to_currency}\n\n{divider}")
    elif to_currency == "JPY":
        convert_to_mxn = Decimal(
            ammount2convert)*Decimal(jpy_rate)
        converted = Decimal(convert_to_mxn)/Decimal(jpy_rate)
        print(f"\n\t\t\t${ammount2convert:,.4f} {from_currency} = ${
            converted:,.4f} {to_currency}\n\n{divider}")
    else:
        print(f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda destino: \'{
              to_currency}\' que ingresaste no es soportado\n")
else:
    print(f"\n\t\t\tVuelve a ejecutar el programa, el codigo de moneda origen: \'{
        from_currency}\' que ingresaste no es soportado\n")
