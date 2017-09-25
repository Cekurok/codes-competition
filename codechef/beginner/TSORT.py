testcase = int(input())
iResult = []
for i in range(testcase):
  iResult.append(int(input()))
iResult = sorted(iResult)
for x in iResult:
  print(x)