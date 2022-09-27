# Triangle567

___

testing the initial classifyTriangle() implementation

| Test ID            | Input         |  Expected Results   |  Actual Result   |  Pass or Fail   |
|--------------------|---------------|-----|-----|-----|
| testInvalidInput1  | "3", "", ""   |  "InvalidInput"   |  Error   |   Error  |
| testInvalidInput2  | -1, -1, -1    |  "InvalidInput"   |   "InvalidInput"  |  Pass   |
| testInvalidInput3  | 999, 999, 999 |  "InvalidInput"   |   "InvalidInput"  |  Pass   |
| testRightTriangle1 | 3, 4, 5       |  "Right"   |   "InvalidInput"  |  Fail   |
| testRightTriangle2 | 50, 30, 40    |  "Right"   |   "InvalidInput"  |  Fail   |
| testRightTriangle3 | 3, 5, 4    |  "Right"   |   "InvalidInput"  |  Fail   |
| testNotTriangle1   | 1, 1, 2       |  "NotATriangle"   |   "InvalidInput"  |  Fail   |
| testNotTriangle1   | 1, 1, 3       |  "NotATriangle"   |   "InvalidInput"  |  Fail   |
| testIsoceles1      | 2, 2, 3       |  "Isoceles"   |   "InvalidInput"  |  Fail   |
| testIsoceles2      | 3, 2, 2       |  "Isoceles"   |   "InvalidInput"  |  Fail   |
| testIsoceles3      | 2, 3, 2       |  "Isoceles"   |   "InvalidInput"  |  Fail   |
| testEquilateral1   | 2, 2, 2       |  "Equilateral"   |   "InvalidInput"  |  Fail   |
| testScalene1       | 2, 3, 4       |  "Scalene"   |   "InvalidInput"  |  Fail   |


___
testing the improved classifyTriangle() implementation

| Test ID            | Input         |  Expected Results   |  Actual Result   |  Pass or Fail   |
|--------------------|---------------|-----|-----|-----|
| testInvalidInput1  | "3", "", ""   |  "InvalidInput"   |  "InvalidInput"   |   Pass  |
| testInvalidInput2  | -1, -1, -1    |  "InvalidInput"   |   "InvalidInput"  |  Pass   |
| testInvalidInput3  | 999, 999, 999 |  "InvalidInput"   |   "InvalidInput"  |  Pass   |
| testRightTriangle1 | 3, 4, 5       |  "Right"   |   "Right"  |  Pass   |
| testRightTriangle2 | 50, 30, 40    |  "Right"   |   "Right"  |  Pass   |
| testRightTriangle3 | 3, 5, 4    |  "Right"   |   "Right"  |  Pass   |
| testNotTriangle1   | 1, 1, 2       |  "NotATriangle"   |   "NotATriangle"  |  Pass   |
| testNotTriangle1   | 1, 1, 3       |  "NotATriangle"   |   "NotATriangle"  |  Pass   |
| testIsoceles1      | 2, 2, 3       |  "Isoceles"   |   "Isoceles"  |  Pass   |
| testIsoceles2      | 3, 2, 2       |  "Isoceles"   |   "Isoceles"  |  Pass   |
| testIsoceles3      | 2, 3, 2       |  "Isoceles"   |   "Isoceles"  |  Pass   |
| testEquilateral1   | 2, 2, 2       |  "Equilateral"   |   "Equilateral"  |  Pass   |
| testScalene1       | 2, 3, 4       |  "Scalene"   |   "Scalene"  |  Pass   |

___



| Test ID            | Test Run 1 | Test Run2 |
|--------------------|------------|-----------|
| Tests Planned  | 13         | 13        |
| Tests Executed  | 13         | 13        |
| Tests Passed  | 2          | 13        |
| Defects Found | 6          | 0         |
| Defects Fixed | 0          | 6         |



___

Report

1. Assignment Description: test and improve classifyTriangle()

2. Author: Xingjian Wu

3. Summary: 

- as the table above shows

5. “I affirm that I will not give or receive any unauthorized help on this assignment, and that all work will be my own.”



ci