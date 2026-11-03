parts = input().split()
values = []
missing = 0
for p in parts :
    if p =="NA":
     missing += 1
else:
    values.append(float(p))
print("Ölçmə:", len(values))
print("Boş:", missing)
print("min:", min(values))
print("max", max(values))
avg = round(sum(values)/ len(values),1)
print("orta qiymet:", avg)
def level(v):
   if v <-105:
      return "zəif"
   elif v <-95:
      return "orta"
   else:
      return "yaxşı"
for v in values:
   print(v,"-", level(v))
counts={"zəif": 0, "orta": 0, "yaxşı": 0}
for v in values:
    s=level
    counts[1] +=1
print(counts)
share=round(counts["zəif"]/len(values))*100
print("Zəif payı:",share,"%")
if share>=30:
   print("Qərar: briqadanı göndər")
elif share>=10:
   print("Qərar:müşahidə saxla")

