import arrow
now = arrow.now()
logClearConfig = {"interval": 12}
print("**************")
end_date = str(now.shift(months=-logClearConfig.get("interval")))[:10]
print(end_date)